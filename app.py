
from flask import Flask,request,make_response,jsonify
from helpers.mdc_logging import get_mdc_logger,set_mdc_trace_id
from config.config import Config
from main import get_fast_url_data_by_cubis_profile_id
config = Config('config.yaml')


app = Flask(__name__)
log = get_mdc_logger(__name__)

@app.route('/fastlink/<cubis_user_id>', methods=['GET'])
def get_fastlink(cubis_user_id):   
    set_mdc_trace_id()
    # cubis_user_id = request.view_args['cubis_user_id']
    log.info("get_fastlink[REST] BEGIN cubis_user_id={}",cubis_user_id)
    
    token ,fastlink,config_name = get_fast_url_data_by_cubis_profile_id(cubis_user_id)
    
    response = make_response( jsonify(access_token=token,fastlink_url=fastlink,config_name=config_name) , 200)
    
    log.info("get_fastlink[REST] END response={}",response)
    return response  


#-----------------------WEB HOOKS-------------------------
@app.route('/webhook/account-update', methods=['POST'])
def get_account_updates():    
    set_mdc_trace_id()
    data = request.get_json()
    print(data)
    return make_response('tada', 200)

@app.route('/webhook/balance-update', methods=['POST'])
def get_balance_updates():    
    set_mdc_trace_id()
    data = request.get_json()
    print(data)
    return make_response('tada', 200)
#-------------------------MAIN----------------------------
if __name__ == '__main__':
    if config.PROD_MODE:
        # serve(app, host='127.0.0.1', port=config.SERVER_PORT)
        pass
    else:         
        #hot reloading makes schedulers run twice
        app.run(debug=True,port=config.SERVER_PORT ,use_reloader=False)