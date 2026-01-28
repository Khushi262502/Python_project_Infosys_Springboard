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

##  Technologies Used
- Python
- Dask (Bag & DataFrame)
- Regular Expressions
- SMTP (Email Alerts)
- Git & GitHub

##  Project Structure
  log-analytics-engine/
│
├── backend/                 # Backend logic for log processing & analytics
│   ├── __init__.py
│   ├── ingestion/           # Log ingestion modules
│   │   ├── __init__.py
│   │   └── loader.py
│   │
│   ├── processing/          # Log processing & anomaly detection
│   │   ├── __init__.py
│   │   ├── pipeline.py
│   │   └── anomaly.py
│   │
│   └── config/              # Configuration files
│       ├── __init__.py
│       ├── dask_config.py
│       └── email_config.py  # (Ignored via .gitignore)
│
├── frontend/                # Frontend / dashboard UI (if any)
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── log_generation/          # Scripts to generate sample logs
│   └── generate_logs.py
│
├── schema/                  # Log schema definitions
│   └── log_schema.json
│
├── app.py                   # Application entry (API / UI launcher)
├── main.py                  # Main execution script
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── LICENSE                  # License file
└── .gitignore               # Ignored files & secrets
