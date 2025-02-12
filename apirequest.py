# import requests
# response = requests.get('  https://api.github.com/issues')
# print(response.json())

import requests  # Correct module name

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")  # Correct URL format
Json_response=response.json()
# print(len(Json_response))
total_id=[]
for i in range(len(Json_response)):
    total_id.append((Json_response[i]["user"]["id"]))
    i=i+1
    
print(total_id)