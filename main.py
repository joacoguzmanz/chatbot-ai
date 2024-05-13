import os
# import pandas as pd
from chat_utils import answer_with_completion

if __name__ == '__main__':
    # Document to use
    PDF_DOC = os.path.join(os.path.expanduser('~'), 'Desktop/maure-4040-presupuesto.pdf')

    # pdf_to_csv_plus_embeddings(PDF_DOC)

    user_query = input('Ingresa una pregunta: ')
    comp_message = answer_with_completion(user_query)
    print(comp_message)
