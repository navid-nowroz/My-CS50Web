# My CS50 Web Projects

This repository contains my solutions and projects from **CS50’s Web Programming with Python and JavaScript (CS50W)**.  
Each folder is a separate assignment or project from the course, built as part of my learning process and not as production-ready software.

---

## Projects in this repository

- `commerce/` – An e-commerce web application built with Django, featuring user authentication, auction listings, watchlists, and bidding functionality. 
- `search/` – A frontend project that recreates core features of Google Search, including standard search, image search, and advanced search pages.    
- `wiki/` – A simple Wikipedia-like encyclopedia with Markdown-based entries, editing, search, and random page functionality.    

> These projects follow the structure and specifications of CS50W problem sets and final project. They are here so people can **see what I built and what I learned**, not to be reused for course credit.  

---

## Technologies used

Across the projects in this repository, I worked with:

- Python (Django)    
- HTML and CSS    
- JavaScript    
- SQLite    

---

## How to run a project locally

Each project lives in its own subdirectory (for example, `commerce/`, `search/`, or `wiki/`). To run one of them locally:  

1. Clone this repository:
   ```bash
   git clone https://github.com/navid-nowroz/My-CS50Web.git
   cd My-CS50Web
   ```
2. Navigate into the project you want to run:
   ```bash
   cd commerce
   # or: cd search
   # or: cd wiki
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

Then open the URL shown in your terminal (usually `http://127.0.0.1:8000/`) in your browser.  

---

## Important note about academic use

This repository contains **my personal solutions** to CS50W assignments and projects.

- If you are currently taking **CS50W** (or any similar course), **do not copy, adapt, or reuse this code** in any way for problem sets, projects, or final submissions.  
- You may **look at this code to learn and be inspired** after you have tried to solve the problems yourself, but using it for grades is academic dishonesty and against the spirit of the course.  
- I share this work so people can **see what I built** and understand my skill level — not so that anyone can shortcut their own learning.

If you want to build something similar, treat this as a reference of what is possible, then close it and write your own version from scratch.

---

## Copyright

**© 2026 Syed Navid Nowroz (Twoki). All rights reserved.**

All software rights for this repository are reserved for **Twoki**.

You may view this code for personal learning and to understand my work, but you **may not** copy, modify, publish, distribute, or use it for graded coursework or other projects without **explicit written permission** from the copyright holder.

---

## About this repository

- Course: CS50’s Web Programming with Python and JavaScript (Harvard / edX)    
- Author: Syed Navid Nowroz Twoki (`@navid-nowroz`)    

For questions or permission requests, please contact me via GitHub.
