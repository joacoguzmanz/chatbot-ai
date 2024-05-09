import os
import pandas as pd
from langchain_community.document_loaders import PyPDFLoader
from utils import split_text, generate_embedding
from helpers import num_tokens_from_string

if __name__ == '__main__':
    # Document to use
    PDF_DOC = os.path.join(os.path.expanduser('~'), 'Desktop/maure-4040-presupuesto.pdf')

    # Read the PDF
    loader = PyPDFLoader(PDF_DOC)
    pages = loader.load()

    texts = split_text(pages)  # Array of document objects

    new_list = []

    for i in range(len(texts)):
        text = texts[i].page_content
        embedding = generate_embedding(text)
        pageId = texts[i].metadata['page']
        tokens = num_tokens_from_string(text)
        new_list.append([pageId, text, tokens, embedding])

    df = pd.DataFrame(new_list, columns=['pageId', 'text', 'tokens', 'embedding'])
    print(df.head())

    # Save the dataframe to a CSV file
    df.to_csv('output.csv', index=False)


