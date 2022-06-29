# from yodlee_client.swagger_client  import AuthApi ,ApiClient,Configuration
# from  swagger_client import AuthApi ,ApiClient,Configuration
from config.config import Config


config = Config('config.yaml')

# api_config = Configuration()
# api_config.host = 'https://development.api.yodlee.com.au/ysl'
# api_client = ApiClient(configuration=api_config)
# api_client.set_default_header('Api-Version','1.1')
# api_client.set_default_header('loginName','testUser1')
# auth_api = AuthApi(api_client=api_client)

# def get_token(loginName,api_client=api_client):
#     api_client.set_default_header('loginName',loginName)
#     result = auth_api.generate_access_token(client_id=config.yodlee.CLIENT_ID,secret=config.yodlee.CLIENT_SECRET)
#     return result





# print(get_token('tteest'))

import yodlee_client as client

client.set_configs(config.yodlee.URL,config.yodlee.CLIENT_ID,config.yodlee.CLIENT_SECRET)


client.get_access_token('test-cx-1')

