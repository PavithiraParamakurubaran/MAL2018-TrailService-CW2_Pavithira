import pyodbc

def create_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};"
            "SERVER=localhost,1433;"
            "DATABASE=CW2;"
            "UID=SA;"
            "PWD=C0mp2001!;"
            "TrustServerCertificate=yes;"
        )
        return conn
    except Exception as e:
        print("Error connecting:", e)
        return None
