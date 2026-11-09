# Notes (Docker lab challenge)

Notes is a small Flask app for saving short notes. Your job is to containerize it
without step-by-step instructions. Everything you need is on this page.

## How the app runs

- **Python:** 3.13. Dependencies are listed in `requirements.txt`.
- **Server:** this build has no development server, so `python notes.py` will not
  start it. Run it with [gunicorn](https://gunicorn.org/), which is already in
  `requirements.txt`. The Flask object is called `app` and lives in the module
  `notes`.
- **Port:** the app must listen on port **8000** on **all interfaces**.
- **Data:** the app saves its notes to `notes.json` inside the folder named by the
  `NOTES_DIR` environment variable. The variable is required, and the app exits
  with an error if it isn't set. Use `/srv/notes`.

## Endpoints

| Method | Path | What it does |
| --- | --- | --- |
| GET | `/` | Web page listing all notes |
| GET | `/health` | `{"status": "ok", ...}` once the app is running |
| GET | `/api/notes` | All notes as JSON |
| POST | `/notes` | Adds a note from the form fields `title` (required) and `body` |
| POST | `/notes/<id>/delete` | Deletes a note |

Example request from another container on the same network:

```sh
curl -s -X POST -d "title=Groceries" -d "body=eggs, milk" http://notes:8000/notes
```
