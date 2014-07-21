from flask import Flask, render_template
from requests import get
from werkzeug.contrib.cache import SimpleCache

INDEX_URL = "https://raw.githubusercontent.com/bundlewrap/plugins/master/index.json"
CACHE_TIMEOUT = 3 * 60  # seconds

app = Flask(__name__)
cache = SimpleCache()


@app.route('/')
def index():
    index_data = cache.get('index')
    if index_data is None:
        print("GET")
        index_data = get(INDEX_URL).json()
        cache.set('index', index_data, timeout=CACHE_TIMEOUT)
    return render_template(
        "index.html",
        index=sorted(index_data.items()),
    )

if __name__ == '__main__':
    app.run(debug=True)
