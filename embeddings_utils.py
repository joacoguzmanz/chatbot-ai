import os
from openai import OpenAI
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from helpers import num_tokens_from_string
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


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


def pdf_to_csv_plus_embeddings(pdf_doc: str):
    # Read the PDF
    loader = PyPDFLoader(pdf_doc)
    pages = loader.load()

    texts = split_text(pages)  # Array of document objects

    new_list = []

    for i in range(len(texts)):
        text = texts[i].page_content
        text = text.replace('\n', ' ')
        embedding = generate_embedding(text)
        page_id = texts[i].metadata['page']
        tokens = num_tokens_from_string(text)
        new_list.append([page_id, text, tokens, embedding])

    df = pd.DataFrame(new_list, columns=['page_id', 'text', 'tokens', 'embedding'])
    print(df.head())

    # Save the dataframe to a CSV file
    df.to_csv('output.csv', index=False)
