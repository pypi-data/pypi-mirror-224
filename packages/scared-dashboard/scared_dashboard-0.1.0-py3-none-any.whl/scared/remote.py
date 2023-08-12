from typing import Any, Dict, Tuple, Union
import json
from pathlib import Path
from fabric import Connection


def _load_remote_json_file(connection: Connection, path: Path) -> Dict[str, Any]:
    result = connection.run(f"cat {str(path)}", hide=True)
    if not result.ok:
        raise RuntimeError(result.stderr)
    return json.loads(result.stdout)


def load_remote_run(
    host: str, run_path: Union[Path, str]
) -> Tuple[str, Dict[str, Any], Dict[str, Any]]:
    """
    :param host: remote hostname
    :param run_path:

    :return: ``(name, config, metrics)``
    """
    run_path = Path(run_path)

    config_path = run_path / "config.json"
    metrics_path = run_path / "metrics.json"

    connection = Connection(host)
    config = _load_remote_json_file(connection, config_path)
    metrics = _load_remote_json_file(connection, metrics_path)

    return (run_path.name, config, metrics)
