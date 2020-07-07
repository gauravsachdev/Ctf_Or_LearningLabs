from bs4 import BeautifulSoup
import requests
import hashlib
url = "http://docker.hackthebox.eu:32468/"
s = requests.Session()
req = s.get(url)
soup = BeautifulSoup(req.text, "html.parser")
convert=soup.find("h3").text
tosend=hashlib.md5(convert.encode()).hexdigest()
values = {'hash':tosend}
r = s.post(url, data=values)
print(r.text)
