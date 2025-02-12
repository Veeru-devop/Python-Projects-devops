import requests
import json

# Zendesk API credentials
ZENDESK_DOMAIN = ""
ZENDESK_API_TOKEN = ""
ZENDESK_EMAIL = ""

# Load configuration from JSON file
with open("zendesk_fields.json") as file:
    field_config = json.load(file)

# Zendesk API endpoint for ticket fields
url = f"https://{ZENDESK_DOMAIN}/api/v2/ticket_fields.json"

# Basic Authentication with email/token
auth = (f"{ZENDESK_EMAIL}/token", ZENDESK_API_TOKEN)

# Deploy the field
response = requests.post(url, json=field_config, auth=auth)

if response.status_code == 201:
    print("Field successfully deployed to Zendesk!")
else:
    print(f"Failed to deploy field: {response.status_code} - {response.text}")
