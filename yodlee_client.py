import requests
from rest_client import session



base_url = 'https://development.api.yodlee.com.au/ysl'
client_id = 'mvARj21uCPC3aob1LhTNsFVEOPVXC9yz'
client_secret =  'JwJaVYZiiVkgelln'

def set_configs(url,clientId,clientSecret):
    global base_url 
    global client_id
    global client_secret
    
    base_url = url
    client_id=clientId
    client_secret=clientSecret
    

def get_access_token(userId):
    response = session.post(
        url = base_url + '/auth/token' ,
        headers={'Content-Type': 'application/x-www-form-urlencoded',
                 'loginName':userId,
                 'Api-Version':'1.1'
                 },
        data={
            'clientId': client_id,
            'secret': client_secret
        }
    
    )
    json = response.json()
    
    
    return json['token']['accessToken']



get_access_token('test-cx-1')