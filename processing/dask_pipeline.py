import dask.dataframe as dd
from ingestion.loader import read_logs
from ingestion.parser import parse_log_line

def build_pipeline(file_path):
    bag = read_logs(file_path)

    parsed = (
        bag.map(parse_log_line)
           .filter(lambda x: x is not None)

    )
    meta = {
        "timestamp": "object",
        "level" : "object",
        "service" : "object",
        "message" : "object"
    }
    df = parsed.to_dataframe(meta = meta)
    df["timestamp"] = dd.to_datetime(df["timestamp"])

    return df


    
