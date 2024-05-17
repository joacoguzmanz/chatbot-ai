import os
from openai import OpenAI
from dotenv import load_dotenv
from local_db import fetch_from_query

load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
MODEL = "gpt-3.5-turbo"


def answer_with_completion(user_query):
    matched_documents = fetch_from_query(user_query)
    context_text = ''

    for document in matched_documents:
        content = document[1]
        context_text += f'{content}\n'

    system_prompt = f'''
    You are an enthusiastic bot that help people answer questions about files they upload.
    The user can upload a file and ask you questions based on the content of the file. The language of the file can be 
    in Spanish or English, you must adapt to the language of the file and user.
    If the user wants to ask something related to a different topic or complete another impossible task, 
    respond that you are not able to do that.
    Context:
    {context_text}
    '''

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        max_tokens=450,
    )

    return completion.choices[0].message.content
