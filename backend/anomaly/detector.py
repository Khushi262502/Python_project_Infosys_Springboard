import dask.dataframe as dd

def detect_anomaly(log_df, z_threshold=3):

    # Force timestamp to string for safe filtering
    log_df = log_df.assign(
        timestamp_str=log_df["timestamp"].astype(str)
    )

    # Keep rows that look like dates
    log_df = log_df[
        log_df["timestamp_str"].str.contains(r"\d{4}-\d{2}-\d{2}", na=False)
    ]

    # Convert to datetime
    log_df = log_df.assign(
        timestamp=dd.to_datetime(
            log_df["timestamp_str"],
            format="%Y-%m-%d %H:%M:%S",
            errors="coerce"
        )
    ).dropna(subset=["timestamp"])

    # Filter ERROR logs
    error_logs = log_df[log_df["level"] == "ERROR"]

    if error_logs.shape[0].compute() == 0:
        print("No ERROR logs found — anomaly detection skipped.")
        return error_logs

    # Bucket per minute
    error_logs = error_logs.assign(
        minute=error_logs["timestamp"].dt.floor("T")
    )

    # Count errors
    error_counts = (
        error_logs
        .groupby("minute")
        .size()
        .rename("error_count")
        .reset_index()
    )

    mean = error_counts["error_count"].mean().compute()
    std = error_counts["error_count"].std().compute()

    if std == 0:
        print("No variance in error counts — anomaly detection skipped.")
        return error_counts

    anomalies = error_counts[
        error_counts["error_count"] > mean + z_threshold * std
    ]

    return anomalies
