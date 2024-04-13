import os
import mysql.connector

os.system('cls')
def conectar_db():
    return mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="farmacia_bienestar"
)

