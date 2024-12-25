import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Create a SQLAlchemy engine
def create_engine_url():
    return f"mssql+pyodbc://{st.secrets["username"]}:{st.secrets["username"]}@{st.secrets["server"]}/{st.secrets["database"]}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(create_engine_url())

# Use pandas to read the results of the query into a DataFrame
query = "SELECT * from benchmark_main;"
df = pd.read_sql_query(query, engine)

df
