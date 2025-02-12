import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://veerpratap7773.atlassian.net/rest/api/3/issue"


auth = HTTPBasicAuth("", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
    "fields": {
        "summary": "First JIRA Ticket",
        "project": { "key": "PGA" },
        "issuetype": { "name": "Story" },  
        "reporter": { "id": "" },  # FIXED: Added required reporter field
        "description": {
            "content": [
                {
                    "content": [
                        { "text": "My first Jira ticket", "type": "text" }
                    ],
                    "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
        }
    }
})

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
