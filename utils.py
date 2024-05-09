import os
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# def generate_embedding(text: str) -> list:
#     response = client.embeddings.create(
#         model='text-embedding-3-small',
#         input=text,
#         encoding_format='float'
#     )
#     return response.data[0].embedding


def split_text(docs_to_split):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(docs_to_split)
    return texts


def generate_embedding(text: str) -> list:
    response = client.embeddings.create(
        model='text-embedding-3-small',
        input=text,
        encoding_format='float'
    )
    return response.data[0].embedding
