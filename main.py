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

import db.db_manager as db
import yodlee_client as client
from helpers.mdc_logging import get_mdc_logger

log = get_mdc_logger(__name__)

db.init(host=config.db.HOST, username=config.db.USERNAME, password=config.db.PASSWORD,
            db_name=config.db.DB_NAME, recreate_tables=config.db.RECREATE_TABLES)

client.set_configs(config.yodlee.URL,config.yodlee.CLIENT_ID,config.yodlee.CLIENT_SECRET)


def get_fast_url_data_by_cubis_profile_id(cubis_profile_id):
    '''
    For a given cubis user returns the config parameters needed to generate fastlink window
    if the respective yodlee user doesn't exist in the db ,a new user is created and stored.  
    [the same cubis profile id is used as the yodlee id]
    :returns access_token,fastlink_url,fastlink_config_name
    '''
    log.info('get_fast_url_data_by_cubis_profile_id BEGIN cubis_profile_id={}',cubis_profile_id)
    
    token = client.get_access_token(cubis_profile_id)
    user = db.get_user(cubis_profile_id)
    if user == None :
        log.info('get_fast_url_data_by_cubis_profile_id adding new user {}',cubis_profile_id)
        db.add_user(cubis_profile_id)              
    
    log.info('get_fast_url_data_by_cubis_profile_id END access_token={}',token)
    return token , config.yodlee.FASTLINK_URL , config.yodlee.CONFIG_NAME
    
    
    

# client.get_access_token('test-cx-1')

