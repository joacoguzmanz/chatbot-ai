import os
from dotenv import load_dotenv
import psycopg2
from embeddings_utils import generate_embedding

load_dotenv()


def connect_to_db():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            port=os.environ.get('DB_PORT')
        )
        cur = conn.cursor()
        return conn, cur
    except psycopg2.Error as e:
        print('Error connecting to database: ', e)


def insert_to_db(df):
    conn, cur = connect_to_db()
    try:
        for index, row in df.iterrows():
            text = row['text']
            embedding = row['embedding']

            cur.execute("INSERT INTO documents (content, embedding) VALUES (%s, %s)", (text, embedding))
        conn.commit()
    except psycopg2.Error as e:
        print('Error inserting into database: ', e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_all():
    conn, cur = connect_to_db()
    try:
        cur.execute("SELECT * FROM documents")
        rows = cur.fetchall()
        return rows
    except psycopg2.Error as e:
        print('Error fetching from database: ', e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_one():
    conn, cur = connect_to_db()
    try:
        cur.execute("SELECT * FROM documents")
        row = cur.fetchone()
        return row
    except psycopg2.Error as e:
        print('Error fetching from database: ', e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def simple_match(embedding, limit=5):
    conn, cur = connect_to_db()
    try:
        cur.execute(
            '''SELECT id, content, 1 - (embedding::vector(1536) <=> %s::vector(1536)) AS cosine_similarity
               FROM documents
               ORDER BY cosine_similarity DESC LIMIT %s;''',
            (embedding, limit)
        )
        rows = cur.fetchall()
        return rows
    except psycopg2.Error as e:
        print('Error fetching from database: ', e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def fetch_from_query(query: str):
    conn, cur = connect_to_db()
    user_input = query.replace('\n', ' ')
    embedding = generate_embedding(user_input)
    try:
        matched_documents = simple_match(embedding, limit=3)
        return matched_documents
    except psycopg2.Error as e:
        print('Error fetching from database: ', e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
