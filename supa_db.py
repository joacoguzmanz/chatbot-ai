import os
from dotenv import load_dotenv
# from supabase import create_client, Client
import psycopg2
from utils import generate_embedding

load_dotenv()

# def save_to_supabase(df):
#     for index, row in df.iterrows():
#         page_id = index
#         text = row['text']
#         embedding = row['embedding']
#
#         (supabase.table('documents')
#          .insert({'id': page_id, 'content': text, 'embedding': embedding})
#          .execute())


def get_from_supabase():
    query = input('Ask your question: ')
    user_input = query.replace('\n', ' ')
    embedding = generate_embedding(user_input)
    print(embedding)
    # search_matching_embeddings(match_count=4, match_threshold=0.7, embedding=embedding)


# def search_matching_embeddings(match_count, match_threshold, embedding):
#     result = supabase.rpc('match_documents', {
#         'match_count': match_count,
#         'match_threshold': match_threshold,
#         'query_embedding': embedding
#     })
#
#     last_result = supabase.rpc('find_document_by_embedding', {
#         'query_embedding': result.json['query_embedding']
#     })
#
#     print(vars(last_result))
