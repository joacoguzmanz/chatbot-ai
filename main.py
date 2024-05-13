import os
import pandas as pd
from local_db import fetch_one, insert_to_db, fetch_all, fetch_from_query

if __name__ == '__main__':
    # Document to use
    PDF_DOC = os.path.join(os.path.expanduser('~'), 'Desktop/maure-4040-presupuesto.pdf')

    # pdf_to_csv_plus_embeddings(PDF_DOC)

    user_query = input('Ingresa una pregunta: ')
    fetched_data = fetch_from_query(user_query)
    print(fetched_data)
    # todo - add the ability to return embeddings in text form
