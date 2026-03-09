import http.client
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(Path("../.env"))
api_token: str = str(os.getenv("API_TOKEN"))
baseURL: str = "v1.formula-1.api-sports.io"

conn: http.client.HTTPSConnection = http.client.HTTPSConnection(baseURL)

headers = { 'x-apisports-key': api_token }

conn.request("GET", "/races?competition=1&season=2022", headers=headers)

res = conn.getresponse()
data = res.read()

with open('test.json', 'w') as f:
   f.write(data.decode("utf-8"))