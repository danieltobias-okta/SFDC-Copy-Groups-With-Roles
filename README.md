# SFDC-Copy-Groups-With-Roles
The `main.py` file requires four values to get started; app_id, api_token, base_url, target_app_id. 
* `app_id` this is the source (starting) app id.
* `target_app_id` is the target (ending) app id.
* base_url should be in the form xyz.okta.com (or xyz.oktapreview.com)

Please note there is a **limit of 200** groups for this migration. You can probably adjust it to handle more, but I have not done it.
