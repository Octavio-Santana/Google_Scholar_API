from flask import Flask, jsonify
from google_scholar import GoogleScholar
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome to the Google Scholar API."

@app.route('/<busc>', methods=['GET'])
def first_five_pages(busc):
    infos = GoogleScholar(busc).run(None, None)
    return jsonify({busc: infos})

@app.route('/<busc>/inicio=<int:pg_i>&fim=<int:pg_f>', methods=['GET'])
def pages(busc, pg_i, pg_f):
    infos = GoogleScholar(busc).run(pg_i, pg_f)
    return jsonify({busc: infos})

@app.route('/<busc>/pg=<int:pg>', methods=['GET'])
def page_busc(busc, pg):
    infos = GoogleScholar(busc, pg).run(pg, None)
    return jsonify({busc: infos})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)