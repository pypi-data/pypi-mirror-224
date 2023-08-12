import json, os, argparse, importlib, sys, traceback
from typing import Any, Dict, List, Literal, Tuple
import dearpygui.dearpygui as dpg
from scared.remote import load_remote_run


# {run name => {config key => config value}}
run_configs: Dict[str, Dict[str, Any]] = {}
# {run name => {metrics name => metrics value}}
run_metrics: Dict[str, Dict[str, Any]] = {}
# {run name => {property name => property value}}
run_props: Dict[str, Dict[Literal["remote"], Any]] = {}


dpg.create_context()
dpg.create_viewport(title="sacred-dpg-dashboard")


config_windows = []


def get_all_possible_metrics() -> List[Tuple[str, str]]:
    """Return all opened metrics

    :return: a list of tuple of form ``(run_name, metrics_name)``
    """
    global run_metrics
    metrics = []
    for run_name, metrics_dict in run_metrics.items():
        for metrics_name in metrics_dict.keys():
            metrics.append((run_name, metrics_name))
    return metrics


# themes
with dpg.theme(tag="hist_theme"):
    with dpg.theme_component(dpg.mvHistogramSeries):
        dpg.add_theme_style(
            dpg.mvPlotStyleVar_FillAlpha, 0.5, category=dpg.mvThemeCat_Plots
        )

with dpg.theme(tag="metrics_list_button_theme"):
    with dpg.theme_component(dpg.mvButton):
        # left align
        dpg.add_theme_style(
            dpg.mvStyleVar_ButtonTextAlign, 0.0, category=dpg.mvThemeCat_Core
        )

with dpg.theme(tag="remote"):
    with dpg.theme_component(dpg.mvTab):
        PURPLE = (124, 36, 179)
        GRAY_PURPLE = (98, 66, 117)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, PURPLE)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, PURPLE)
        dpg.add_theme_color(dpg.mvThemeCol_Tab, GRAY_PURPLE)


# main metrics window
with dpg.window(tag="metrics_window"):

    with dpg.child_window(no_scrollbar=True):
        with dpg.table(header_row=False, resizable=True):
            dpg.add_table_column(init_width_or_weight=0.25)
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_child_window(tag="metrics_list")
                dpg.add_child_window(tag="plots")


def create_plot(tag: str, parent: str):

    yaxis = f"{tag}_plot_y"
    xaxis = f"{tag}_plot_x"

    def fit_axis_data():
        dpg.fit_axis_data(xaxis)
        dpg.fit_axis_data(yaxis)

    def add_series(x, y, label: str, plot_type: Literal["plot", "hist", "scatter"]):
        """Add a series to the plot"""
        assert len(x) == len(y)

        def change_series_plot_type(sender, app_data, user_data):
            """
            :param user_data: ``(series, plot_type)``
            """
            series, plot_type = user_data
            dpg.delete_item(series)
            add_series(x, y, label, plot_type)
            fit_axis_data()

        if plot_type == "plot":
            if len(x) == 1:
                series = dpg.add_hline_series(y, label=label, parent=yaxis)
            else:
                series = dpg.add_line_series(x, y, label=label, parent=yaxis)
            for other_type in ["hist", "scatter"]:
                dpg.add_button(
                    label=f"plot as {other_type}",
                    parent=series,
                    user_data=(series, other_type),
                    callback=change_series_plot_type,
                )

        elif plot_type == "hist":
            series = dpg.add_histogram_series(
                y, label=label, parent=yaxis, min_range=min(y), max_range=max(y)
            )
            dpg.bind_item_theme(series, "hist_theme")
            for other_type in ["plot", "scatter"]:
                dpg.add_button(
                    label=f"plot as {other_type}",
                    parent=series,
                    user_data=(series, other_type),
                    callback=change_series_plot_type,
                )

        elif plot_type == "scatter":
            series = dpg.add_scatter_series(x, y, label=label, parent=yaxis)
            for other_type in ["plot", "hist"]:
                dpg.add_button(
                    label=f"plot as {other_type}",
                    parent=series,
                    user_data=(series, other_type),
                    callback=change_series_plot_type,
                )

        else:
            raise ValueError(f"unknown plot type : {plot_type}")

        def delete_series(sender, app_data, user_data):
            dpg.delete_item(user_data)
            fit_axis_data()

        dpg.add_button(
            label="delete",
            parent=series,
            user_data=series,
            callback=delete_series,
        )

        fit_axis_data()

    with dpg.plot(
        tag=tag,
        parent=parent,
        drop_callback=lambda s, a, u: add_series(a[0], a[1], a[2], "plot"),
        payload_type="plotting",
        width=-1,
        height=-1,
    ):
        dpg.add_plot_axis(dpg.mvXAxis, tag=xaxis)
        dpg.add_plot_axis(dpg.mvYAxis, tag=yaxis)
        dpg.add_plot_legend(show=True)


def set_plot_grid(grid: Literal["1", "2x1", "2x2"]):
    # delete current plots
    dpg.delete_item("plots", children_only=True)

    # create a new grid
    if grid == "1":
        create_plot("plot1", "plots")
    elif grid == "2x1":
        with dpg.subplots(2, 1, width=-1, height=-1, parent="plots") as s:
            create_plot("plot1", s)
            create_plot("plot2", s)
    elif grid == "2x2":
        with dpg.subplots(2, 2, width=-1, height=-1, parent="plots") as s:
            create_plot("plot1", s)
            create_plot("plot2", s)
            create_plot("plot3", s)
            create_plot("plot4", s)
    else:
        raise ValueError(f"unknown grid specification: '{grid}'")


set_plot_grid("1")


def refresh_metrics_list():
    """
    Refresh the metrics list according to the currently opened runs.
    """
    dpg.delete_item("metrics_list", children_only=True)

    with dpg.tab_bar(parent="metrics_list"):

        for run_name in run_metrics.keys():

            with dpg.tab(label=run_name) as t:

                # set "remote" theme if the run is a remote one
                if run_props.get(run_name, {}).get("remote"):
                    dpg.bind_item_theme(t, "remote")

                filter_set = dpg.add_filter_set()

                dpg.add_input_text(
                    label=f"Filter",
                    user_data=filter_set,
                    callback=lambda sender, input_string: dpg.set_value(
                        dpg.get_item_user_data(sender), input_string
                    ),
                    before=filter_set,
                )

                for metrics_name in run_metrics[run_name]:

                    button = dpg.add_button(
                        label=metrics_name,
                        filter_key=metrics_name,
                        width=-1,
                        parent=filter_set,
                    )
                    dpg.bind_item_theme(button, "metrics_list_button_theme")

                    # drag payload
                    x_data = run_metrics[run_name][metrics_name]["steps"]
                    y_data = run_metrics[run_name][metrics_name]["values"]
                    label = f"{run_name}|{metrics_name}"
                    with dpg.drag_payload(
                        parent=dpg.last_item(),
                        drag_data=(x_data, y_data, label),
                        payload_type="plotting",
                    ):
                        # display text and a plot preview when dragging
                        dpg.add_text(label)
                        dpg.add_simple_plot(default_value=y_data)


def config_window_tabbar(w: int) -> str:
    return f"config_window_{w}_tabbar"


def refresh_config_window(w: int):
    """Refresh a config window according to the currently opened runs"""
    tabbar = config_window_tabbar(w)
    dpg.delete_item(tabbar, children_only=True)
    for run_name, run_config in run_configs.items():
        with dpg.tab(label=run_name, parent=tabbar):
            dpg.add_text(json.dumps(run_config, indent=4))


def create_config_window(sender, app_data):
    global config_windows

    with dpg.window(pos=(0, 0), width=400, height=400) as w:
        dpg.add_tab_bar(tag=config_window_tabbar(w))

    config_windows.append(w)
    dpg.configure_item(w, on_close=lambda *args: config_windows.remove(w))

    refresh_config_window(w)


def open_run(run_root_dir: str):
    global run_metrics
    global run_configs

    run_name = os.path.basename(run_root_dir)

    # metrics
    with open(f"{run_root_dir}/metrics.json") as f:
        local_run_metrics = json.load(f)
    run_metrics[run_name] = local_run_metrics

    # config
    with open(f"{run_root_dir}/config.json") as f:
        local_run_config = json.load(f)
    local_run_config = {
        k: v for k, v in local_run_config.items() if not k == "__annotations__"
    }
    run_configs[run_name] = local_run_config

    run_props[run_name] = {}

    refresh_metrics_list()

    for w in config_windows:
        refresh_config_window(w)


def open_remote_run(host: str, run_root_dir: str):
    name, config, metrics = load_remote_run(host, run_root_dir)
    run_configs[name] = config
    run_metrics[name] = metrics
    run_props[name] = {"remote": True}
    refresh_metrics_list()
    for w in config_windows:
        refresh_config_window(w)


# menu bar
def on_open(sender, app_data):
    global run_metrics
    global run_configs

    root_dir = os.path.dirname(app_data["file_path_name"])
    run_names = [selection for selection in app_data["selections"].keys()]

    for run_name in run_names:
        open_run(f"{root_dir}/{run_name}")


with dpg.menu_bar(parent="metrics_window"):

    with dpg.menu(label="Runs"):

        # open local runs
        fs = dpg.add_file_dialog(
            show=False, callback=on_open, directory_selector=True, width=800, height=600
        )
        dpg.add_menu_item(label="Open...", callback=lambda: dpg.show_item(fs))

        # open remote runs
        with dpg.window(
            tag="open_remote_runs_window",
            label="Open remote run",
            modal=True,
            show=False,
            no_title_bar=True,
        ) as remote_runs_w:

            dpg.add_input_text(tag="open_remote_run_host", label="host")
            dpg.add_input_text(tag="open_remote_run_path", label="path")

            def open_remote_runs_window():
                dpg.configure_item(remote_runs_w, show=True, width=200)
                dpg.set_item_pos(remote_runs_w, [200, 200])

            def close_remote_runs_window():
                dpg.configure_item(remote_runs_w, show=False)

            def on_ok():
                open_remote_run(
                    dpg.get_value("open_remote_run_host"),
                    dpg.get_value("open_remote_run_path"),
                )
                close_remote_runs_window()

            with dpg.group(horizontal=True):
                dpg.add_button(label="OK", callback=on_ok)
                dpg.add_button(label="Cancel", callback=close_remote_runs_window)

        dpg.add_menu_item(label="Open remote...", callback=open_remote_runs_window)

        # open configs window
        dpg.add_menu_item(label="Open configs window", callback=create_config_window)

    with dpg.menu(label="Plots"):
        with dpg.menu(label="Set grid"):
            dpg.add_menu_item(label="1", callback=lambda: set_plot_grid("1"))
            dpg.add_menu_item(label="2x1", callback=lambda: set_plot_grid("2x1"))
            dpg.add_menu_item(label="2x2", callback=lambda: set_plot_grid("2x2"))

    with dpg.menu(label="Debug"):
        dpg.add_menu_item(label="open dpg debug window", callback=dpg.show_debug)
        dpg.add_menu_item(
            label="Open item registry",
            callback=lambda: dpg.show_tool(dpg.mvTool_ItemRegistry),
        )


parser = argparse.ArgumentParser()
parser.add_argument(
    "-i", "--input-files", nargs="*", help="List of files to open at startup"
)
parser.add_argument(
    "-c",
    "--custom-metrics",
    nargs="*",
    help="List of modules where custom metrics are defined in a 'custom_metrics' variable. A custom metrics should be a function, taking as input the run_metrics dict and outputting a list of values or a tuple (steps, values)",
)
args = parser.parse_args()

if args.input_files:
    for f in args.input_files:
        if f.startswith("ssh:"):
            host, path, *_ = f[4:].split(":")
            open_remote_run(host, path)
        else:
            open_run(f.rstrip("/"))

if args.custom_metrics:

    run_metrics["custom"] = {}

    for module_path in args.custom_metrics:

        module_root_dir = os.path.abspath(os.path.dirname(module_path))
        sys.path.append(module_root_dir)

        mod_name = os.path.basename(module_path)
        module = importlib.import_module(mod_name)

        for f in module.custom_metrics:
            try:
                metrics = f(run_metrics)
            except Exception:
                print(f"exception computing metrics {f.__name__}")
                traceback.print_exc(file=sys.stderr)
                exit(1)

            neg_error = None
            pos_error = None
            if isinstance(metrics, tuple):
                if len(metrics) == 2:
                    steps, values = metrics
                else:
                    steps, values, neg_error, pos_error = metrics
            else:
                steps, values = (list(range(len(metrics))), metrics)

            run_metrics["custom"][f.__name__] = {"values": values, "steps": steps}
            if not neg_error is None:
                assert not pos_error is None
                run_metrics["custom"][f.__name__]["error"] = (neg_error, pos_error)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("metrics_window", True)
dpg.start_dearpygui()
dpg.destroy_context()
