import requests 
from bs4 import BeautifulSoup

url = "https://academico.ifmt.edu.br/qacademico/lib/validalogin.asp"
login = ("<Registration Nº>", "<password>")
session = requests.session()
r = session.post(url, auth=login, verify=False)
print (r.status_code)

url = "http://academico.ifmt.edu.br/qacademico/index.asp?t=2000"
r = session.get(url, verify=False)
soup = BeautifulSoup(r.text, "lxml")
print(soup)
