# Docker Lab: Flask Task Tracker

A small Flask application for practicing Docker images, containers, networking, and volumes.

## Files

- `app.py` – Flask routes and JSON storage logic.
- `requirements.txt` – Python dependencies.
- `templates/index.html` – Web page.
- `static/style.css` – Styling.
- `data/` – Task data directory; `tasks.json` is created when a task is added.

## Run locally (optional)

With Python 3.10+ installed:

```sh
python -m pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000 and add or remove tasks.

The current tasks are also available as JSON from `GET /api/tasks`.
