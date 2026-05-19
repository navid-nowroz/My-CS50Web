# My CS50 Web Projects

This repository contains my solutions and projects from **CS50’s Web Programming with Python and JavaScript (CS50W)**.  
Each folder is a separate assignment or project from the course, built as part of my learning process and not as production-ready software. [page:36][web:22]

## Projects in this repository

- `commerce/` – An e-commerce web application built with Django, featuring user authentication, auction listings, watchlists, and bidding functionality. [page:36][web:22]  
- `search/` – A frontend project that recreates core features of Google Search, including standard search, image search, and advanced search pages. [page:36][web:22]  
- `wiki/` – A simple Wikipedia-like encyclopedia with Markdown-based entries, editing, search, and random page functionality. [page:36][web:22]  

> Note: These projects follow the structure and specifications of CS50W problem sets and are intended **purely for educational and portfolio purposes**. Please use them responsibly and do not submit this code as your own work if you are currently taking the course. [page:36][web:25]

## Technologies used

Across the projects in this repository, I worked with:

- Python (Django) [page:36][web:22]  
- HTML and CSS [page:36][web:22]  
- JavaScript [page:36][web:22]  
- SQLite [page:36][web:22]  

## How to run a project locally

Each project lives in its own subdirectory (for example, `commerce/`, `search/`, or `wiki/`). To run one of them locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/navid-nowroz/My-CS50Web.git
   cd My-CS50Web
   ```
2. Navigate into the project you want to run:
   ```bash
   cd commerce   # or: cd search, cd wiki
   ```
3. (Optional) Create and activate a virtual environment.
4. Install dependencies (if a `requirements.txt` is present):
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations and start the development server (for Django projects):
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Then open the URL shown in your terminal (usually `http://127.0.0.1:8000/`) in your browser. [web:22]

## About this repository

- Course: CS50’s Web Programming with Python and JavaScript (Harvard / edX) [web:22]  
- Author: Syed Navid Nowroz Twoki (`@navid-nowroz`) [page:36]  
- License: MIT – you are free to read, learn from, and adapt the code, but please give appropriate credit and avoid academic dishonesty. [page:36][web:25]
