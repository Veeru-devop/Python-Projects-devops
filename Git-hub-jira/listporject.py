import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veerpratap7773.atlassian.net/rest/api/3/project"


auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

Project= json.loads(response.text)

print(Project)