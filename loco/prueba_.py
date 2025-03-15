import numpy as np
from flask import Flask

import psycopg2

try:
    # Intentar conectar a la base de datos
    conn = psycopg2.connect(
        dbname="mydatabase_prueba",
        user="myuser",
        password="mypassword",
        host="database",
        port="5432"
    )
    print("Conexión exitosa a la base de datos")
    conn.close()
except Exception as e:
    print(f"Error al conectar: {e}")

