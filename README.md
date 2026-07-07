# snowflake_data_engineering

## Snowflake Streamlit deployment

This repository includes a GitHub Actions workflow that deploys the Streamlit app in the app folder to Snowflake using the Snowflake CLI and GitHub OIDC authentication.

Workflow file: .github/workflows/deploy.yml
App folder: apps/streamlit_to_sharepoint_app

Set the following GitHub repository secrets before using the workflow:
- SNOWFLAKE_ACCOUNT
- SNOWFLAKE_ROLE
- SNOWFLAKE_WAREHOUSE
- SNOWFLAKE_DATABASE
- SNOWFLAKE_SCHEMA

The workflow uses the Snowflake service user github_cicd_user by default. If you want to override it, set the GitHub Actions variable SNOWFLAKE_SERVICE_USER.

Optionally, set these GitHub Actions variables:
- SNOWFLAKE_STREAMLIT_APP_NAME to control the app name in Snowflake
- SNOWFLAKE_OIDC_AUDIENCE if your Snowflake security integration uses a custom audience value
