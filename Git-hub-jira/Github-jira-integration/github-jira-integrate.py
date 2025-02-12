from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def Jira_integration():

    url = "https://veerpratap7773.atlassian.net/rest/api/3/issue"

    API_TOKEN = "ATATT3xFfGF0essCQ4CcFxvevdmPv5K-bgpHEyjL4VlYr_KQciPBRIszwNJ7lWU5etHVObUnj452NmHLeSis7yGC1R5JlDkf5mLJcjsqaJGVHKst-ojqaD-1-d9g8JRcnMmRIq1KOpXY_IAgQfm5pZf8h4gL45C7N_mAAJKhAByOMnUZLn1JCSg=9BFDC33F" 

    auth = HTTPBasicAuth("veerpratap7773@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "summary": "First JIRA Ticket",
            "project": { "key": "PGA" },
            "issuetype": { "name": "Story" },  
            "reporter": { "id": "712020:441ca20c-81d2-4edc-8484-55505a4689a1" },  # FIXED: Added required reporter field
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))



if __name__ == '__main__':
    app.run("0.0.0.0", port=80)