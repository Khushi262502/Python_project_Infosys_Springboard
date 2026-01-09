from confg.dask_config import start_dask
from processing.dask_pipeline import build_pipeline
import time
import os
def main():
    client = start_dask()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("-" * 50)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_FILE = os.path.join(BASE_DIR, "data", "sample_log.log")

    

    start = time.time()
    log_df = build_pipeline("data/sample_log.log")
    total_logs = log_df.count().compute()    
    end = time.time()

    print("total logs parsed:", total_logs)
    print("time taken",end)

    input("press enter...")

    

        
if __name__ == "__main__":
    main()
