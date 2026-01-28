import dask.dataframe as dd
from backend.ingestion.loader import read_logs
from backend.ingestion.parser import parse_log_line

def build_pipeline(file_path):
    bag = read_logs(file_path)

    parsed = (
        bag
        .map(parse_log_line)
        .filter(lambda x: x is not None)
    )

    meta = {
        "timestamp": "object",
        "level": "object",
        "service": "object",
        "message": "object",
    }

    df = parsed.to_dataframe(meta=meta)

    # ✅ SAFE datetime parsing (FINAL FIX)
    df = df.assign(
        timestamp=dd.to_datetime(
            df["timestamp"],
            format="%Y-%m-%d %H:%M:%S",
            errors="coerce"
        )
    )

    # ✅ DROP bad timestamps permanently
    df = df.dropna(subset=["timestamp"])

    return df
