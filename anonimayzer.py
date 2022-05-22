#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask import render_template

import requests, time
app = Flask(__name__)

from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.firefox import GeckoDriverManager



@app.route('/anon/', methods=['GET'])
def search():
    error = None
    query = request.args.get('query')
    if query and query != '':
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--ignore-certificate-errors-spki-list')
        
        
        myProxy = "https://antizapret.prostovpn.org/proxy.pac"

        
        profile = webdriver.FirefoxProfile() 
        profile.set_preference("network.proxy.type", 2)
        profile.set_preference("network.proxy.autoconfig_url", myProxy)
        profile.update_preferences() 

        br = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options, firefox_profile=profile)
        
        #br.install_addon("censor_tracker-5.3.1.0.xpi", temporary=True)
        
        br.get(query)
        
        time.sleep(3)

        with open("templates/index.html", "w", encoding="utf-8") as f:
            f.write(br.page_source)
        br.close()
        
        
        return render_template("index.html")

    else:
        error = 'Не введен запрос!'
        return f"Не введен запрос!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')