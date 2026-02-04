import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/api/patients"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Patients Data:", soup.text)
