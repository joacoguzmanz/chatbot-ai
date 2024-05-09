import os
import pandas as pd
from supa_db import save_to_supabase

if __name__ == '__main__':
    # Document to use
    PDF_DOC = os.path.join(os.path.expanduser('~'), 'Desktop/maure-4040-presupuesto.pdf')

    # pdf_to_csv_plus_embeddings(PDF_DOC)

    csv_data = pd.read_csv('output.csv')
    save_to_supabase(csv_data)
