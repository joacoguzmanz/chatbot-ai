import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(url, key)


def save_to_supabase(df):
    for index, row in df.iterrows():
        page_id = index
        text = row['text']
        embedding = row['embedding']

        (supabase.table('documents')
         .insert({'id': page_id, 'content': text, 'embedding': embedding})
         .execute())
