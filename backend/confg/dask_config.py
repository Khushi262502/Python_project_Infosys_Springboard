from dask.distributed import LocalCluster, Client

def start_dask():
    """
    Starts a local Dask cluster and returns a client
    """
    cluster = LocalCluster(
        n_workers=4,
        threads_per_worker=2,
        dashboard_address = ":8787"
    )

    client = Client(cluster)
    return client
