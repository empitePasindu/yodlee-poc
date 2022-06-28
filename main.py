from yodlee_client.swagger_client  import AuthApi ,ApiClient,Configuration
# from  swagger_client import AuthApi ,ApiClient,Configuration

config = Configuration()
config.host = 'https://development.api.yodlee.com.au/ysl'
print(config.auth_settings())

auth_api_client = ApiClient(configuration=config,header_name='', header_value='1.1')
auth_api_client.default_headers['Api-Version']='1.1'



# auth_api = AuthApi(api_client=api_client)
# auth_api.generate_access_token()


