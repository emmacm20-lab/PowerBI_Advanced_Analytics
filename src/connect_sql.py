# 📂 src/connect_sql.py - Conexión a SQL Server

import pyodbc

def connect_sql():
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=tu_servidor;DATABASE=tu_db;UID=usuario;PWD=contraseña")
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 * FROM Ventas")
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    print("Conexión a SQL Server exitosa:", connect_sql())
