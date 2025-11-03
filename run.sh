#!/bin/bash
# Start FastAPI backend in background
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Wait for backend to start
sleep 3

# Start Streamlit frontend
streamlit run frontend.py --server.port 8501
