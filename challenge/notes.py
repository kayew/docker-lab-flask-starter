"""Notes, a small Flask app for the Docker lab challenge (Task 10).

This is a production-style build, so there is no built-in development server.
Run it with gunicorn (see README.md).
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from flask import Flask, abort, jsonify, redirect, render_template, request, url_for

NOTES_DIR = os.environ.get("NOTES_DIR")
if not NOTES_DIR:
    raise RuntimeError("NOTES_DIR is not set. Set it to the folder where notes should be saved.")

NOTES_FILE = Path(NOTES_DIR) / "notes.json"

app = Flask(__name__)


def load_notes():
    if not NOTES_FILE.exists():
        return []
    with NOTES_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_notes(notes):
    NOTES_FILE.parent.mkdir(parents=True, exist_ok=True)
    with NOTES_FILE.open("w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2)


@app.get("/")
def index():
    notes = sorted(load_notes(), key=lambda note: note["created"], reverse=True)
    return render_template("index.html", notes=notes)


@app.get("/health")
def health():
    return jsonify(status="ok", notes_file=str(NOTES_FILE))


@app.get("/api/notes")
def list_notes():
    return jsonify(load_notes())


@app.post("/notes")
def add_note():
    title = request.form.get("title", "").strip()
    body = request.form.get("body", "").strip()
    if not title:
        abort(400, "A note needs a title.")
    notes = load_notes()
    notes.append({
        "id": str(uuid4()),
        "title": title,
        "body": body,
        "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    })
    save_notes(notes)
    return redirect(url_for("index"))


@app.post("/notes/<note_id>/delete")
def delete_note(note_id):
    save_notes([note for note in load_notes() if note["id"] != note_id])
    return redirect(url_for("index"))
