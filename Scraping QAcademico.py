import requests 
from bs4 import BeautifulSoup

url = "https://academico.ifmt.edu.br/qacademico/lib/validalogin.asp" #Url where i need post the login 
login = ("<Registration Nº>", "<password>")
session = requests.session() #Creation of the session 
r = session.post(url, auth=login, verify=False) #Using the POST method, i give the user and password
print (r.status_code) #Checking if everything is okay

url = "http://academico.ifmt.edu.br/qacademico/index.asp?t=2000" #Url of the homepage after login page 
r = session.get(url, verify=False) #Using the GET method for take the HTML file, but he is about a error page
soup = BeautifulSoup(r.text, "lxml")
print(soup)
