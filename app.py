# pip install streamlit plotly
# streamlit : Python framework for building web apps for data science and machine learning
# plotly : Interactive graphing library
# app.py is indepent from main.py file
# It reads the processed and deploy in visually(dashboard)

import streamlit as st
from backend.processing.pipeline import build_pipeline
from backend.anomaly.detector import detect_anomalies
import plotly.express as px




st.title("Python Based High Throughput Log Analytics Monitoring Engine")
log_df = build_pipeline("data/sample_log.log")
anomaly_df = detect_anomalies(log_df).compute()
print(anomaly_df)

st.subheader("Anomalies Detected in Logs")

fig = px.line(anomaly_df, x='timestamp', y='anomaly_score', title='Anomaly Scores Over Time')

st.plotly_chart(fig)

st.subheader("Anomalous Log Entries")
st.dataframe(anomaly_df)

# Filters

threshold = st.slider("Anomaly Score Threshold", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
print(threshold)
filtered_anomalies = anomaly_df[anomaly_df['anomaly_score'] >= threshold]
print(filtered_anomalies)
st.dataframe(filtered_anomalies)