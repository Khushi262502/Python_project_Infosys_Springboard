# Python_project_Infosys_Springboard
# High-Throughput Log Analytics & Monitoring Engine

##  Project Overview
This project is a distributed log analytics and monitoring system built using Python and Dask. It processes large-scale system logs in parallel, detects anomalies in error patterns using statistical methods, and enables real-time monitoring through the Dask dashboard.

---

## Features
- Distributed log ingestion using Dask Bag
- Parsing of unstructured logs into structured format
- Error trend analysis and anomaly detection using Z-score
- Real-time execution monitoring via Dask Dashboard
- Email alerting for detected anomalies
- Scalable design for high-volume logs

---

##  Architecture / Workflow
 -Raw Logs → Ingestion → Parsing → Processing → Anomaly Detection → Alerts
