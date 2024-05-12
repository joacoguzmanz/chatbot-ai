import os
import pandas as pd
from local_db import fetch_one, insert_to_db, fetch_all

if __name__ == '__main__':
    # Document to use
    PDF_DOC = os.path.join(os.path.expanduser('~'), 'Desktop/maure-4040-presupuesto.pdf')

    # pdf_to_csv_plus_embeddings(PDF_DOC)

    csv_data = pd.read_csv('output.csv')
    insert_to_db(csv_data)
    fetched_data = fetch_one()
    print(fetched_data)
    # todo - add the ability to return embeddings in text form
