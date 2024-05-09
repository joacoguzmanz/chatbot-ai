import os
from dotenv import load_dotenv
from supabase import create_client, Client
from utils import generate_embedding

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


def get_from_supabase():
    query = input('Ask your question: ')
    user_input = query.replace('\n', ' ')
    embedding = generate_embedding(user_input)
    search_matching_embeddings(match_count=4, match_threshold=0.7, embedding=embedding)


def search_matching_embeddings(match_count, match_threshold, embedding):
    result = supabase.rpc('match_documents', {
        'match_count': match_count,
        'match_threshold': match_threshold,
        'query_embedding': embedding
    })

    print(vars(result))
    # Result structure: session, headers, params, negate_next, path, http_method, json, __orig_class__
    # json structure: match_count, match_threshold, query_embedding
