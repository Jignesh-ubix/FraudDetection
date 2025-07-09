import os
from urllib.parse import urlparse
import psycopg2
from dotenv import load_dotenv
load_dotenv()

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

# Database connection parameters
DB_NAME = tmpPostgres.path.replace('/', '')
DB_USER = tmpPostgres.username
DB_PASSWORD = tmpPostgres.password
DB_HOST = tmpPostgres.hostname
DB_PORT = "5432"


def add_data_to_db(entries):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    for entry in entries:
        cur.execute(
            """
            INSERT INTO transactions (customer, age, gender, merchant, category, amount, fraud)
            VALUES (%s, %s, %s, %s, %s, %s, NULL)
            """,
            entry
        )

    conn.commit()
    cur.close()
    conn.close()

def get_new_transactions():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM transactions WHERE fraud IS NULL")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows