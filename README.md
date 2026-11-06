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

## Docker lab

**There is intentionally no Dockerfile in this starter project.** You will create one in Task 3, build and run it in Task 4, investigate networking in Task 5, and mount the app's `/app/data` directory to a named volume in Task 6 (assuming your Dockerfile uses `WORKDIR /app`).

The application listens on `0.0.0.0:5000` and saves its data in `data/tasks.json`. It does not use a database or external API.

**Persistence experiment:** Stopping and restarting *the same container* preserves files in that container. Removing the container and creating a *new container* does not preserve those changes unless the data is stored externally (e.g. a Docker volume). Use a new container in the comparison.

This uses Flask's development server for a local educational exercise, not for production deployment.
