import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="database1.cm5ge0qyc76x.us-east-1.rds.amazonaws.com",
        user="admin",
        password="Jazib!23",
        database="database1"
    )