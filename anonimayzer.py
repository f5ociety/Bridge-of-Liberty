#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import render_template

import requests
app = Flask(__name__)

from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@app.route('/anon/', methods=['GET'])
def search():
    error = None
    query = request.args.get('query')
    if query and query != '':
        
        br = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        br.get(query)

        with open("templates/index.html", "w", encoding="utf-8") as f:
            f.write(br.page_source)
        br.close()
        
        
        return render_template("index.html")

    else:
        error = 'Не введен запрос!'
        return f"Не введен запрос!"

if __name__ == '__main__':
    app.run(debug=True)