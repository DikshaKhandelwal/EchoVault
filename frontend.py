import os
import time
from typing import List

import requests
import streamlit as st


API_BASE = os.getenv("ECHOVAULT_API", "http://localhost:8000")


def neon_theme():
    st.set_page_config(page_title="EchoVault", layout="wide")
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@600;700&display=swap');
        html,body,[class^="css"]{background:#0a0e1a;color:#ffffff;font:18px 'Rajdhani',sans-serif;}
        .stApp{background:linear-gradient(135deg,#0a0e1a,#0f1729);}
        header[data-testid="stHeader"]{background:#0a0e1a!important;}
        .main .block-container{padding-top:3rem!important;}
        section[data-testid="stSidebar"]{background:linear-gradient(180deg,#1a0b2e,#16213e)!important;border-right:3px solid #00e5ff;box-shadow:5px 0 30px rgba(0,229,255,.4);}
        section[data-testid="stSidebar"]>div{background:transparent!important;padding-top:40px!important;}
        section[data-testid="stSidebar"] *{color:#ffffff!important;}
        section[data-testid="stSidebar"] .stRadio>label{font:900 28px 'Orbitron',sans-serif!important;color:#00e5ff!important;text-shadow:0 0 15px #00e5ffaa;text-align:center!important;display:block!important;margin-bottom:20px!important;letter-spacing:2px!important;}
        section[data-testid="stSidebar"] [role="radiogroup"]{display:flex!important;flex-direction:column!important;gap:12px!important;}
        section[data-testid="stSidebar"] [role="radiogroup"] label{font:700 24px 'Rajdhani'!important;color:#ffffff!important;padding:16px 24px!important;border-radius:12px!important;transition:all .3s!important;text-align:center!important;border:2px solid #00e5ff44!important;background:rgba(0,229,255,.05)!important;}
        section[data-testid="stSidebar"] [role="radiogroup"] label:hover{background:rgba(0,229,255,.25)!important;transform:translateX(8px) scale(1.05);border-color:#00e5ff!important;}
        section[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"]{background:linear-gradient(90deg,#00e5ff,#7cffb2)!important;color:#0a0e1a!important;font-weight:900!important;box-shadow:0 0 25px rgba(0,229,255,.8);transform:translateX(8px) scale(1.08)!important;border-color:#7cffb2!important;}
        section[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] span{color:#0a0e1a!important;}
        h1{color:#00e5ff!important;text-shadow:0 0 20px #00e5ff,0 0 40px #00e5ff66;font:900 56px 'Orbitron',sans-serif!important;letter-spacing:3px;}
        h2,h3{color:#7cffb2!important;text-shadow:0 0 15px #7cffb288;font:700 36px 'Orbitron',sans-serif!important;}
        .stButton>button{background:linear-gradient(135deg,#00e5ff,#7cffb2)!important;color:#0a0e1a!important;border:none!important;box-shadow:0 0 25px #00e5ff88,inset 0 0 10px rgba(255,255,255,.3)!important;font:700 20px 'Rajdhani'!important;padding:14px 28px!important;letter-spacing:1px!important;transition:all .3s!important;}
        .stButton>button:hover{transform:scale(1.05)!important;box-shadow:0 0 35px #00e5ff!important;}
        .stTextInput>div>div>input,.stTextArea textarea{background:#0f1829!important;color:#fff!important;border:2px solid #00e5ff55!important;font:600 18px 'Rajdhani'!important;box-shadow:inset 0 0 10px rgba(0,229,255,.1);}
        .stTextInput>div>div>input:focus,.stTextArea textarea:focus{border-color:#00e5ff!important;box-shadow:0 0 15px #00e5ff66!important;}
        .stTextInput label,.stTextArea label,.stSlider label,.stFileUploader label{color:#ffffff!important;font:700 18px 'Rajdhani'!important;}
        .stSlider [role="slider"]{background:#00e5ff!important;box-shadow:0 0 15px #00e5ff;}
        .stSlider [data-baseweb="slider"] [role="presentation"]{color:#ffffff!important;}
        .stSlider [data-baseweb="slider"] > div > div{color:#ffffff!important;}
        .stTabs [data-baseweb="tab-list"]{gap:16px;}
        .stTabs [data-baseweb="tab"]{background:#1a0b2e!important;color:#00e5ff!important;font:700 20px 'Rajdhani'!important;border:2px solid #00e5ff55!important;border-radius:8px!important;padding:12px 24px!important;}
        .stTabs [aria-selected="true"]{background:linear-gradient(90deg,#00e5ff,#7cffb2)!important;color:#0a0e1a!important;box-shadow:0 0 20px #00e5ff88;}
        .result-card{border:2px solid #00e5ff66!important;padding:20px!important;border-radius:12px!important;background:linear-gradient(135deg,#0f1829,#1a0b2e)!important;box-shadow:0 0 25px #00e5ff33!important;margin-bottom:16px!important;font-size:18px!important;color:#ffffff!important;}
        .result-card b{color:#7cffb2!important;font-size:22px!important;text-shadow:0 0 10px #7cffb288;}
        .result-card pre{color:#ffffff!important;background:transparent!important;border:none!important;padding:12px 0!important;}
        .tag{display:inline-block;padding:6px 16px!important;margin-right:8px!important;border-radius:20px!important;background:linear-gradient(90deg,#00e5ff,#7cffb2)!important;color:#0a0e1a!important;font:700 16px 'Rajdhani'!important;box-shadow:0 0 10px #00e5ff66;}
        pre,code{color:#ffffff!important;font-size:16px!important;background:#0f1829!important;padding:16px!important;border-radius:8px!important;border:1px solid #00e5ff33!important;}
        .stCaption,small{color:#7cffb2!important;font:600 18px 'Rajdhani'!important;text-shadow:0 0 8px #7cffb244;}
        .stFileUploader section{border:2px dashed #00e5ff66!important;border-radius:12px!important;background:#0f1829!important;}
        .stSpinner>div{border-top-color:#00e5ff!important;border-right-color:#7cffb2!important;}
        .stSuccess{background:linear-gradient(90deg,#7cffb2,#00e5ff)!important;color:#0a0e1a!important;font:700 18px 'Rajdhani'!important;box-shadow:0 0 20px #7cffb288;}
        .stError{background:linear-gradient(90deg,#ff0080,#ff6b6b)!important;color:#fff!important;font:700 18px 'Rajdhani'!important;box-shadow:0 0 20px #ff008088;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def header():
    st.markdown(
        """
        <div style='text-align:center; padding: 20px 0;'>
            <h1 style='margin-bottom: 10px;'>EchoVault</h1>
            <p style='font-size: 24px; color: #7cffb2; font-weight: 600; margin: 10px 0; text-shadow: 0 0 15px #7cffb288;'>
                Don't just store files. Remember why they exist.
            </p>
            <p style='font-size: 20px; color: #00e5ff; font-weight: 600; letter-spacing: 3px; text-shadow: 0 0 10px #00e5ff66;'>
                INGEST • RECALL • SYNC
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def mode_selector() -> str:
    return st.sidebar.radio("Modes", ["Ingest", "Recall", "Sync"], index=0)


def ingest_ui():
    st.subheader("Ingest")
    tab1, tab2 = st.tabs(["Folder", "Upload Files"])
    with tab1:
        folder = st.text_input("Folder path", value=str(os.getcwd()))
        if st.button("Ingest Folder", use_container_width=True):
            with st.spinner("Ingesting..."):
                r = requests.post(f"{API_BASE}/ingest/folder", json={"folder": folder})
            if r.ok:
                st.success(f"Added: {len(r.json().get('added', []))}, Updated: {len(r.json().get('updated', []))}")
            else:
                st.error(r.text)
    with tab2:
        files = st.file_uploader("Drop files", type=["txt","md","pdf","docx"], accept_multiple_files=True)
        if files and st.button("Upload & Ingest", use_container_width=True):
            ok = 0
            for f in files:
                r = requests.post(f"{API_BASE}/ingest/upload", files={"file": (f.name, f, f.type or "application/octet-stream")})
                if r.ok:
                    ok += 1
            st.success(f"Ingested {ok} files")


def recall_ui():
    st.subheader("Recall")
    query = st.text_input("Ask EchoVault", placeholder="show me client reports from July")
    col1, col2 = st.columns(2)
    with col1:
        k = st.slider("Top-K", 1, 15, 5)
    with col2:
        decay = st.slider("Memory aging (days)", 7, 365, 120)
    if st.button("Search", use_container_width=True) and query.strip():
        with st.spinner("Thinking..."):
            r = requests.post(f"{API_BASE}/recall", json={"query": query, "top_k": k, "decay_days": decay})
        if not r.ok:
            st.error(r.text)
            return
        for item in r.json().get("results", []):
            st.markdown(f"<div class='result-card'><b>{item['path']}</b><br/><small>score {item['score']}</small><br/><pre style='white-space:pre-wrap'>{item['summary']}</pre>" + " ".join([f"<span class='tag'>#{t}</span>" for t in item.get("tags", [])]) + "</div>", unsafe_allow_html=True)


def sync_ui():
    st.subheader("Sync")
    folder = st.text_input("Folder path", value=str(os.getcwd()))
    days = st.slider("Archive suggestions after X days unused", 7, 365, 60)
    if st.button("Analyze", use_container_width=True):
        with st.spinner("Scanning..."):
            r = requests.get(f"{API_BASE}/sync", params={"folder": folder, "archive_days": days})
        if not r.ok:
            st.error(r.text)
            return
        data = r.json()
        st.write("Diff")
        st.json(data.get("diff", {}))
        st.write("Archive candidates")
        for p in data.get("archive_suggestions", []):
            st.markdown(f"<span class='tag'>archive</span> {p}", unsafe_allow_html=True)


def main():
    neon_theme()
    header()
    mode = mode_selector()
    if mode == "Ingest":
        ingest_ui()
    elif mode == "Recall":
        recall_ui()
    else:
        sync_ui()


if __name__ == "__main__":
    main()

