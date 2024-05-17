<h1 align="center">AI PDF Chatbot</h1>

---

<p align="center">This project is a chatbot that can answer questions from a PDF file.</p>

## Project status

:construction: This project is currently in development. :construction: \
The program can read a PDF file and extract the text from it. When asking a question,
it can search for the answer in the text.

## About

The idea of this project is to create a chatbot that can answer questions from a PDF file. The chatbot will be able to 
read the PDF file and extract the text from it. When asking a question, the chatbot will search for the answer in the text.

## Technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) \
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) \
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) \
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) \
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white) \
![Next JS](https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white) \
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) \
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Structure

### Frontend

The frontend is built with Next.js and Shadcn components.

### Backend

The backend is built with Python and Postgres. I used Django to create the API and pgvector to create the vector search in Postgres.

## To-do

- [x] Extract text from the PDF file
- [x] Test embedding with pgvector
- [x] Create the database
- [ ] Create the API
- [ ] Create the frontend
- [ ] Deploy the project