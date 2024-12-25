import pandas as pd
import pyodbc
import streamlit as st

@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )
conn = init_connection()

# Fonction pour exécuter une requête et récupérer les résultats dans un DataFrame
@st.cache_data
def query_to_dataframe(query):
    with conn.cursor() as cur:
        cur.execute(query)
        # Récupérer les noms des colonnes
        columns = [column[0] for column in cur.description]
        # Récupérer les données (convertir en liste pour correspondre aux colonnes)
        data = [list(row) for row in cur.fetchall()]
    # Vérifier les dimensions des données
    if len(data) > 0 and len(data[0]) == len(columns):
        # Créer un DataFrame
        return pd.DataFrame(data, columns=columns)
    else:
        raise ValueError(
            f"Shape mismatch: Data shape is {len(data)}, expected columns {len(columns)}"
        )

# Exécuter la requête et convertir les résultats
query = "SELECT * FROM benchmark_main;"
df = query_to_dataframe(query)

# Afficher les premières lignes du DataFrame
df
