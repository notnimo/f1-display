
import requests
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
api_token: str = str(os.getenv("API_TOKEN"))
url = "https://v1.formula-1.api-sports.io/competitions"

payload={}
headers = {
  'x-apisports-key': api_token,
}

response = requests.request("GET", url, headers=headers, data=payload)

with open('test.json', 'w') as f:
  f.write(response.text)