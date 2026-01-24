import dask.dataframe as dd

def detect_anomaly(log_df, z_threshold=3):
   
    # Filter ERROR logs
    log_df["timestamp"] = dd.to_datetime(log_df["timestamp"], errors="coerce")
    log_df = log_df.dropna(subset=["timestamp"])

    # Filter ERROR logs
    error_logs = log_df[log_df["level"] == "ERROR"]

    # Create 1-minute bucket (no resample, works with unknown divisions)
    error_logs["minute"] = error_logs["timestamp"].dt.floor("T")

    # Resample safely
    error_counts = (
        error_logs
        .groupby("minute")
        .size()
        .rename("error_count")
        .reset_index()
    )

    # Compute statistics
    mean = error_counts["error_count"].mean().compute()
    std = error_counts["error_count"].std().compute()

    if std == 0:
        return error_counts.head(0)

    error_counts["z_score"] = (error_counts["error_count"] - mean) / std
    error_counts["is_anomaly"] = error_counts["z_score"].abs() > z_threshold

    return error_counts[error_counts["is_anomaly"]]