import datetime
import re
import pandas as pd

param_dict = {"time": [], "pid": [], "value": []}
match_class = "[org.envirocar.obd.adapter.SyncAdapter]"
dt_pattern = "%Y-%m-%dT%H:%M:%S.%f"

def parse_envirocar_log_pids(log_path: str):
    """
    Parses an enviroCar log file for discovering all PID data response log messages in order to extract timestamp, PID
    and value information.

    Parameters
    ----------
    log_path: str
        Path to the enviroCar log file.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame that holds structured PID data response information

    """
    with open(log_path) as log:
        for line in log:
            if match_class in line:
                time = datetime.datetime.strptime(line[0:23], dt_pattern)
                res = line.split(match_class)
                match = re.findall("\{(.*?)\}", res[1])
                if match:
                    kvp = match[0].split("=")
                    param_dict["time"].append(time)
                    param_dict["pid"].append(kvp[0])
                    param_dict["value"].append(float(kvp[1]))
    df = pd.DataFrame.from_dict(param_dict)
    df.time = pd.to_datetime(df.time)
    df.set_index("time", inplace=True)
    df.sort_index(inplace=True)
    return df
