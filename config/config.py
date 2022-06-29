import yaml
from helpers.mdc_logging import init_logging
from pytz import timezone as get_timezone
import os
class YodleeConfig:
    def __init__(self,config_dict,callback_url) -> None:
        self.CLIENT_ID =  config_dict['CLIENT_ID']
        self.CLIENT_SECRET =  config_dict['CLIENT_SECRET']
        self.URL = config_dict['URL']
        self.CALLBACK_URL = callback_url

class DbConfig:
    def __init__(self,config_dict) -> None:
        self.HOST =  "{}:{}".format(config_dict['HOST'],config_dict['PORT'])
        self.USERNAME =  config_dict['USERNAME']
        self.PASSWORD =  config_dict['PASSWORD']
        self.DB_NAME = config_dict['DB_NAME']
        self.RECREATE_TABLES = config_dict['RECREATE_TABLES']

class Config:
    """
    Load configs and Setup logging
    """
    def __init__(self,config_path) -> None:
        with open(config_path) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        

        self.SERVER_PORT = config['SERVER_PORT']
        self.timezone = config['TIME_ZONE']
        self.MAX_THREADS = config['MAX_THREADS']
        self.PUBLIC_URL = os.environ.get('PUBLIC_URL', config['PUBLIC_URL'])
        mode = str(os.environ.get('ENV_MODE', config['ENV_MODE'])).upper()
        if mode != 'DEV' and mode != 'PROD':
            raise TypeError("Invalid ENV_MODE ,has to be one of DEV or PROD")
        self.PROD_MODE = True if mode == 'PROD' else False
        
        if(self.PROD_MODE):
            config['db']['HOST']= os.environ['DB_HOST']
            config['db']['PORT']= os.environ['DB_PORT']
            config['db']['USERNAME']= os.environ['DB_USERNAME']
            config['db']['PASSWORD']= os.environ['DB_PASSWORD']
        
        self.yodlee =  YodleeConfig(config['yodlee'],self.PUBLIC_URL)
        self.db = DbConfig(config['db'])
            
        init_logging(timezone=self.timezone,log_level=config['log']['LOG_LEVEL'],log_rotate=config['log']['LOG_ROTATE'],file_name=config['log']['LOG_FILE_PATH'])


