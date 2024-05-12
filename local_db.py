import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    host=os.environ.get('DB_HOST'),
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    port=os.environ.get('DB_PORT')
)

# todo - correct cursor closed error
cur = conn.cursor()


def insert_to_db(df):
    for index, row in df.iterrows():
        text = row['text']
        embedding = row['embedding']

        cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (text, embedding))
        conn.commit()
    conn.close()


def fetch_all():
    cur.execute("SELECT * FROM documents")
    rows = cur.fetchall()
    return rows


def fetch_one():
    cur.execute("SELECT * FROM documents")
    row = cur.fetchone()
    return row
