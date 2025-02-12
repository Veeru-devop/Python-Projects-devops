with open(r'C:\Users\acer\OneDrive\Desktop\projects\notes\labmdacodefor-s3automate.txt', 'r') as file:
    content=file.read()
    print(content)

# with open(r'C:\Users\acer\OneDrive\Desktop\projects\notes\labmdacodefor-s3automate.txt', 'w') as file:
#     content=file.write("""import json
#                         import boto3
#                         import urllib

#                         def lambda_handler(event, context):
#                             s3client = boto3.client("s3")
#                             print(event)
#                             bucket_name = event['Records'][0]['s3']['bucket']['name']
#                             print(bucket_name)
#                             key = event['Records'][0]['s3']['object']['key']
#                             key = urllib.parse.unquote_plus(key, encoding ='utf-8')

#                             print(response)
#                             contents = response['Body'].read().decode()

#                             print(contents)""")
#     print(content)