from flask import Flask, send_from_directory
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent.parent
SHARKIE_DIR = BASE_DIR / 'frontend/sharkie'
SHARKIE_DOC_DIR = SHARKIE_DIR / 'docs/html'
JOIN_DIR = BASE_DIR / 'frontend/join/dist/join/browser'

@app.route('/projects/sharkie/')
def sharkie_index():
    return send_from_directory(SHARKIE_DIR, 'index.html')

@app.route('/projects/sharkie/<path:path>')
def sharkie_files(path):
    return send_from_directory(SHARKIE_DIR, path)

@app.route('/projects/sharkie/docs/')
def sharkie_docs_index():
    return send_from_directory(SHARKIE_DOC_DIR, 'index.html')

@app.route('/projects/sharkie/docs/<path:path>')
def sharkie_docs_files(path):
    return send_from_directory(SHARKIE_DOC_DIR, path)

@app.route('/projects/join/')
def join_index():
    return send_from_directory(JOIN_DIR, 'index.html')

@app.route('/projects/join/<path:path>')
def join_data(path):
    return send_from_directory(JOIN_DIR, path)