web: flask db upgrade; flask translate compile; gunicorn spotnote:app
worker: rq worker spotnote-tasks
