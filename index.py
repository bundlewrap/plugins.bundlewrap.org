from flask import Flask
from requests import get

INDEX_URL = "https://raw.githubusercontent.com/blockwart/plugins/master/index.json"

app = Flask(__name__)


@app.route('/')
def index():
    index_data = get(INDEX_URL)
    return index_data.text
