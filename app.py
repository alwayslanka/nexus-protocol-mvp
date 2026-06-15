{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import engine  # You'll build this next\
\
st.set_page_config(page_title="Nexus Protocol | Ingestion Engine", layout="wide")\
\
st.title("Nexus Protocol Ingestion Engine")\
st.subheader("Automated Compliance Data Normalization")\
\
uploaded_file = st.file_uploader("Drop your Supplier BOM/CSV here", type=['csv', 'xlsx'])\
\
if uploaded_file:\
    df = pd.read_csv(uploaded_file) # or pd.read_excel\
    st.write("### Raw Data Preview")\
    st.dataframe(df.head())\
    \
    if st.button("Process & Generate DPP JSON"):\
        # This calls your normalization logic\
        clean_df, json_output = engine.process_data(df)\
        \
        st.success("Data Normalization Complete!")\
        st.write("### Cleaned Data Preview")\
        st.dataframe(clean_df)\
        \
        st.download_button("Download Compliance JSON", json_output, "dpp_output.json")}