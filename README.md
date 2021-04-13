# GHA: Publish Schema to Postman 

This action updates a given Postman API with a new OpenAPI3 schema. 

Makes the assmption that the schema already exists. 

## Inputs

- `schema_name` - The name of the GitHub repository 
- `postman_api_id` - The GitHub token to access private repositories
- `postman_api_version_id` - The version of the API to publish the schema to.
- `postman_workspace_id` - The id of the workspace to generate collections to
- `postman-schema-id` - The id of the schema to be updated. 
- `postman-api-key` - The API key needed to contact the postman api
## Outputs

None

## Example usage

Generate a schema from your django service:

```
./manage.py spectacular --file YOUR_SCHEMA_NAME_HERE.yml
```

```
uses: actions/gha-publish-schema-to-postman@v1
with:
    schema_name: 'YOUR_SCHEMA_NAME_HERE.yml'
    postman_api_id: 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman_api_version_id: 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman_workspace_id: 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman-schema-id = 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman-api-key =  'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
```