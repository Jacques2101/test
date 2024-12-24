from sqlalchemy import create_engine
import pandas as pd
import streamlit as st

# @st.cache_data
# # Fonction permettant de lire la base de données SQL
# def lecture_bdd(DATABASE, table, colonnes=None, condition=None):
#     SERVER = 'vestathena.database.windows.net'
#     USERNAME = 'login_MAM_read'
#     PASSWORD = 'MonceauAM2021!'
#     DRIVER = 'ODBC+Driver+17+for+SQL+Server'
#     connection_string = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}:1433/{DATABASE}?driver={DRIVER}'
#     engine = create_engine(connection_string)
#     # Requête SQL
#     query = f"SELECT {', '.join(colonnes) if colonnes else '*'} FROM {table}"
#     if condition:
#         query += f" WHERE {condition}"
#     # Lire et concaténer les chunks de manière progressive
#     df_final = pd.DataFrame()
#     for chunk in pd.read_sql(query, engine, dtype_backend='pyarrow', chunksize=100000):
#         # Filtrer les colonnes vides dans le chunk
#         chunk_filtered = chunk.dropna(how='all', axis=1)
#         df_final = pd.concat([df_final, chunk_filtered], ignore_index=True)
#     return df_final

# df = lecture_bdd("vestathena_db", "benchmark_main")
# df

st.write('Test')