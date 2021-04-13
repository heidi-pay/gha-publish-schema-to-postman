# GHA: Publish Schema to Postman 

This action updates a given Postman API with a new OpenAPI3 schema. 

Makes the assmption that the schema already exists. 

## Inputs

- `schema_name` - The name of the GitHub repository 
- `postman_api_id` - The GitHub token to access private repositories
- `postman_api_version_id` - The release version in the form refs/tags/v4
- `postman_workspace_id` - The release version in the form refs/tags/v4
- `postman_schema_id` - The release version in the form refs/tags/v4
- `postman-schema-id` - The id of the schema to be updated. 
- `postman-api-key` - The API key needed to contact the postman api
## Outputs

None

## Example usage
```
uses: actions/gha-publish-schema-to-postman@v1
with:
    schema_name: 'input.yml'
    postman_api_id: 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman_api_version_id: 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman_workspace_id: 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman_schema_id = 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman-schema-id = 'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
    postman-api-key =  'XXXXXXXX-XXXXX-XXXX-XXXXX-XXXXXXXX'
```