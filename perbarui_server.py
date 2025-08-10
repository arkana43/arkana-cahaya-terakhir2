from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
RELEASE_DIR = '/var/www/arkana/releases'

@app.route('/arkana/latest_manifest')
def latest():
    return send_from_directory(RELEASE_DIR, 'manifest.json')

@app.route('/arkana/download/<path:filename>')
def dl(filename):
    return send_from_directory(RELEASE_DIR, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
