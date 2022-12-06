import os
import psycopg2
from dotenv import load_dotenv

def dbconn():

    load_dotenv()

    return psycopg2.connect(
        database = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PWD'),
        host = os.getenv('DB_HOST'),
        port = os.getenv('DB_PORT'),
        sslmode='require'
    )