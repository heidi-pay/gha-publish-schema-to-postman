import requests
import json
import sys

schema_name=sys.argv[1]
postman_api_id=sys.argv[2]
postman_api_version_id=sys.argv[3]
postman_workspace_id=sys.argv[4]
postman_schema_id=sys.argv[5]
api_key=sys.argv[6]

with open(schema_name, 'r') as file:
    schema = file.read()

# Update the Schema
def update_schema():
        url = "https://api.getpostman.com/apis/{}/versions/{}/schemas/{}".format(postman_api_id, postman_api_version_id, postman_schema_id)

        payload = json.dumps({
          "schema": {
            "language": "json",
            "schema": schema,
            "type": "openapi3"
          }
        })
        headers = {
          'Content-Type': 'application/json',
          'X-API-Key': api_key
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        if response.status_code == 200:
            print("Successfully posted Schema")
            return True
        else:
            print(response.text)
            return False

def create_collection_from_schema():
        url = "https://api.getpostman.com/apis/{}/versions/{}/schemas/{}/collections?workspace={}".format(
            postman_api_id,
            postman_api_version_id,
            postman_schema_id,
            postman_workspace_id)

        payload = json.dumps({
                "name": "My generated collection",
                "relations": [
                        {
                                "type": "contracttest"
                        }
                ]
        })
        headers = {
                'Content-Type': 'application/json',
                'X-API-Key': api_key
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            print("Successfully generated collections")
            return True
        else:
            print(response.text)
            return False



if __name__ == "__main__":
    if update_schema():
        create_collection_from_schema()