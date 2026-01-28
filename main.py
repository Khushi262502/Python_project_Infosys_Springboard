from backend.confg.dask_config import start_dask
from backend.processing.dask_pipeline import build_pipeline
from backend.confg.email_config import send_email
from backend.anomaly.detector import detect_anomaly 
from fastapi import FastAPI
from backend.router.service import router
import time
import os

app = FastAPI()
app.include_router(router)

ADMIN_EMAIL = "khushijuly2004@gmail.com"
def main():
    client = start_dask()
    print(client)
    print(f"Dashboard link: {client.dashboard_link}")
    print("-" * 50)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOG_FILE = r"C:\Users\khush\OneDrive\Desktop\log_analytics_engine\log_generation\log.py"


    

    start = time.time()
    log_df = build_pipeline(LOG_FILE)
    total_logs = log_df.shape[0].compute()    
    end = time.time()



    print("total logs parsed:", total_logs)
    print("time taken",round(end - start ,2),"seconds")

    print("\n Running anamly detection...")
    anomalies_df = detect_anomaly(log_df)

    anomalies = anomalies_df.compute()

    if anomalies.empty:
        print("No anomalies detected")
    else:
        print(f"{len(anomalies)} anomalies detected!")

        for _, row in anomalies.iterrows():
            anomaly_data = {
                "timestamp" : row["timestamp"],
                "error_count": row["error_count"],
                "z_score" : row["z_score"]
            }

            send_email(
                to_mail = ADMIN_EMAIL,
                anomaly = anomaly_data
            )

            print(
                f"Alert sent | Time: {row['timestamp']} |"
                f"Errors : {row['error_count']}"
            )




    

    input("press enter...")

    

        
if __name__ == "__main__":
    main()
