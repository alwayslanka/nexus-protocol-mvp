{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import json\
\
def process_data(df):\
    # 1. Normalize mapping (The "Golden Schema")\
    mapping = \{\
        '8.8 Steel': 'Steel_8.8',\
        'Steel 8.8': 'Steel_8.8',\
        'A4-70': 'SS_A4_70',\
        'A4 70': 'SS_A4_70'\
    \}\
    \
    # Apply logic\
    df['Material_Composition_Code'] = df['Material_Grade'].replace(mapping)\
    \
    # 2. Add Compliance validation\
    df['Compliance_REACH_Status'] = df['REACH_Status'].apply(lambda x: 'OK' if x in ['Compliant', 'OK'] else 'FAIL')\
    \
    # 3. Export to JSON\
    json_output = df.to_json(orient='records')\
    \
    return df, json_output}