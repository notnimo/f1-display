import http.client
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

if __name__ == "__main__":
  load_dotenv(Path("../.env"))
  api_token: str = str(os.getenv("API_TOKEN"))
  baseURL: str = "v1.formula-1.api-sports.io"

  conn: http.client.HTTPSConnection = http.client.HTTPSConnection(baseURL)

  headers = { 'x-apisports-key': api_token }

# handle requests of h2h and overviews