import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veerpratap7773.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0essCQ4CcFxvevdmPv5K-bgpHEyjL4VlYr_KQciPBRIszwNJ7lWU5etHVObUnj452NmHLeSis7yGC1R5JlDkf5mLJcjsqaJGVHKst-ojqaD-1-d9g8JRcnMmRIq1KOpXY_IAgQfm5pZf8h4gL45C7N_mAAJKhAByOMnUZLn1JCSg=9BFDC33F" 

auth = HTTPBasicAuth("veerpratap7773@gmail.com", API_TOKEN)

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