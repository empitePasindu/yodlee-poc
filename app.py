
from flask import Flask,request,make_response,jsonify
from helpers.mdc_logging import get_mdc_logger,set_mdc_trace_id
from config.config import Config

config = Config('config.yaml')


app = Flask(__name__)
log = get_mdc_logger(__name__)

@app.route('/fastlink/get-token', methods=['GET'])
def get_token():    
    set_mdc_trace_id()
    
    return make_response('', 200)


#-------------------------MAIN----------------------------
if __name__ == '__main__':
    if config.PROD_MODE:
        # serve(app, host='127.0.0.1', port=config.SERVER_PORT)
        pass
    else:         
        #hot reloading makes schedulers run twice
        app.run(debug=True,port=config.SERVER_PORT ,use_reloader=False)