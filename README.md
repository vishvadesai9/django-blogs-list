# Personal Blog Site

## Requirements:

1. Create a Django model for a blog post with fields for title, content, author, and publication date.

2. Implement a Django REST Framework API to list, view, and create blog posts.

3. Develop Django templates to display a paginated list of blog posts, view individual blog posts, and create new blog posts.

4. Utilize Django Template Language to ensure a user-friendly and visually appealing blog site.

## Setup:

1. Setup Postgres database

2. Create .env file under the project folder

Populate with the following values:

DATABASE_NAME=""

DATABASE_HOST="127.0.0.1"

DATABASE_PASSWORD=""

DATABASE_PORT="5432"

DATABASE_USER=""

## Run:

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

