import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

def lecture_bdd(DATABASE, table, colonnes=None, condition=None):
    from sqlalchemy.orm import sessionmaker
    SERVER = 'vestathena.database.windows.net'
    USERNAME = 'login_MAM_read'
    PASSWORD = 'MonceauAM2021!'
    DRIVER = 'ODBC Driver 17 for SQL Server'

    connection_url = URL.create(
        drivername="mssql+pyodbc",
        username=USERNAME,
        password=PASSWORD,
        host=SERVER,
        port=1433,
        database=DATABASE,
        query={"driver": DRIVER}
    )

    # Créez un moteur
    engine = create_engine(connection_url)

    # Ouvrez une connexion explicite
    with engine.connect() as connection:
        # Construire la requête SQL
        query = f"SELECT {', '.join(colonnes) if colonnes else '*'} FROM {table}"
        if condition:
            query += f" WHERE {condition}"
        # Lire les données avec Pandas
        df = pd.read_sql(query, connection)
    return df
# Utilisation
df = lecture_bdd("vestathena_db", "benchmark_main")
df