from sqlalchemy import create_engine
import pandas as pd
import streamlit as st

@st.cache_data
def lecture_bdd(DATABASE, table, colonnes=None, condition=None):
    SERVER = 'vestathena.database.windows.net'
    USERNAME = 'login_MAM_read'
    PASSWORD = 'MonceauAM2021!'
    DRIVER = 'ODBC+Driver+17+for+SQL+Server'
    connection_string = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}:1433/{DATABASE}?driver={DRIVER}'
    engine = create_engine(connection_string)
    
    # Construire la requête SQL
    query = f"SELECT {', '.join(colonnes) if colonnes else '*'} FROM {table}"
    if condition:
        query += f" WHERE {condition}"
    
    # Lire toute la table en une seule fois
    df = pd.read_sql(query, engine)
    return df

# Exemple d'utilisation
df = lecture_bdd("vestathena_db", "benchmark_main")
df

