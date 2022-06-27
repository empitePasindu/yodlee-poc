import logging
import logging.handlers
import threading
from pytz import timezone as get_timezone
from datetime import datetime
import os
import re
class MDCLocal(threading.local):
 
    def __init__(self):
        self.mdc_dict = {"trace_id": ""}
 
    def set_attribute(self, key, value):
        self.mdc_dict[key] = value
 
    def remove_attribute(self, key):
        del self.mdc_dic[key]
 
    def get_attribute(self, key):
        return self.mdc_dict[key]
 
    def get_mdc_map(self):
        return self.mdc_dict
 
    def clear(self):
        [self.mdc_dict.update({k: ""}) for k in self.mdc_dict]
 
 
MDC_BASIC_FORMAT = '%(asctime)s - %(name)s %(levelname)s - [%(trace_id)s] : %(message)s'
MDC_MAP = MDCLocal()
 
 
class MDCLogger(logging.Logger):
 
    def __init__(self, deco_logger):
        self.deco_logger = deco_logger
 
    def setLevel(self, level):
        self.deco_logger.setLevel(level)
 
    def debug(self, msg, *args, **kwargs):
        self.deco_logger.debug(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def info(self, msg, *args, **kwargs):
        self.deco_logger.info(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def warning(self, msg, *args, **kwargs):
        self.deco_logger.warning(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def warn(self, msg, *args, **kwargs):
        self.deco_logger.warning(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def error(self, msg, *args, **kwargs):
        self.deco_logger.error(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def exception(self, msg, *args, **kwargs):
        self.deco_logger.exception(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def critical(self, msg, *args, **kwargs):
        self.deco_logger.critical(msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
 
    def log(self, level, msg, *args, **kwargs):
        self.deco_logger.critical(level, msg, extra=MDC_MAP.get_mdc_map(), *args, **kwargs)
    
    def addHandler(self, hdlr):
        self.deco_logger.addHandler(hdlr)
 
def put_mdc(key, value):
    MDC_MAP.set_attribute(key, value)

def set_mdc_trace_id(value=None):
    if value == None :
        value = datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
    MDC_MAP.set_attribute('trace_id', value)
 
 
def clear_mdc():
    MDC_MAP.clear()
 
 
def basic_config(**kwargs):
    if 'format' in kwargs.keys():
        pass
    else:
        kwargs['format'] = MDC_BASIC_FORMAT
    logging.basicConfig(**kwargs)
 
 
def get_mdc_logger(name=None):
    if name:
        return MDCLogger(logging.getLogger(name))
    else:
        return MDCLogger(logging.getLogger())
    
    
#------------log format setup and initialization-----------------------
class RequestFormatter(logging.Formatter):

    def format(self, record):
        '''To remove unpopulated traceId in root logger'''
        arg_pattern = re.compile(r'%\((\w+)\)')
        arg_names = [x.group(1) for x in arg_pattern.finditer(self._fmt)]
        for field in arg_names:
            if field not in record.__dict__:
                record.__dict__[field] = None

        return super().format(record)


def log_namer(default_name):
            # This will be called when doing the log rotation
            # default_name is the default filename that would be assigned, e.g. Rotate_Test.txt.YYYY-MM-DD
            # Do any manipulations to that name here, for example this changes the name to Rotate_Test.YYYY-MM-DD.txt
            base_filename, ext, date = default_name.split(".")
            return f"{base_filename}.{date}.{ext}" 
 
def init_logging(timezone,log_level,log_rotate,file_name):
        folder_path = os.path.dirname(file_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_log_handler = logging.handlers.TimedRotatingFileHandler(file_name, when=log_rotate)
        formatter=RequestFormatter('%(asctime)s - %(name)s %(levelname)s - [%(trace_id)s] : %(message)s')

        if timezone and isinstance(timezone, str):
                timezone = get_timezone(timezone)
                # formatter.converter = timezone
        console_log_handler = logging.StreamHandler()
        console_log_handler.setFormatter(formatter)
        file_log_handler.setFormatter(formatter)
        file_log_handler.namer = log_namer
        logger = get_mdc_logger()
        logger.addHandler(file_log_handler)
        logger.addHandler(console_log_handler)
        logger.setLevel( logging.DEBUG if log_level == 'DEBUG' else logging.INFO)
        logging.getLogger('apscheduler.executors.default').setLevel(logging.WARNING)
        set_mdc_trace_id()