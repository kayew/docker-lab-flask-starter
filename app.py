"""A small Flask task tracker for the Docker lab.

Tasks are saved to a JSON file in the data/ directory. The directory can
later be mounted to a Docker volume to keep tasks across containers.
"""

import json
import os
from pathlib import Path
from uuid import uuid4

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

# By default, the data folder is beside this file (i.e. /app/data in Docker).
DATA_DIR = Path(os.environ.get("TASK_DATA_DIR", Path(__file__).resolve().parent / "data"))
TASKS_FILE = DATA_DIR / "tasks.json"


def load_tasks():
    """Read tasks from disk, or return an empty list on first launch."""
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    """Write tasks to disk in a human-readable format."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


@app.get("/")
def index():
    return render_template("index.html", tasks=load_tasks())


@app.get("/tasks")
def get_tasks():
    return jsonify(load_tasks())


@app.post("/tasks")
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        tasks = load_tasks()
        tasks.append({"id": str(uuid4()), "title": title})
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.post("/tasks/<task_id>/delete")
def delete_task(task_id):
    tasks = [task for task in load_tasks() if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    # Binding to 0.0.0.0 allows Docker to publish the app's port later.
    app.run(host="0.0.0.0", port=5000)
