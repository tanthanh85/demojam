from flask import Flask,redirect
from get_response_time import vpn_1, vpn_2, get_best_VPN
from get_agentID import *
app = Flask(__name__)
import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


# @app.route('/<hostname>',methods = ['GET', 'POST'])
@app.route('/',methods = ['GET', 'POST'])
def home():
    try:
        agent_Id = get_agentId(host=hostname)
        logging.info(f'Agent id is {agent_Id}')
        response_time_list = get_best_VPN(agent_Id=agent_Id)
        logger.info(f'response time list is {response_time_list}')  
        min_response_time = min(response_time_list.values())
        logger.info(f'Min response time is {min_response_time}')
        for server,response_time in response_time_list.items():
            if response_time==min_response_time:              
                best_VPN = server
                logger.info(f'Best VPN server is {best_VPN}')

        if best_VPN == '206945':
            vpn='https://vpn1.demojam.com'
            logger.info(f'Best VPN server address is {vpn}')
            return redirect(vpn, code=302)
        if best_VPN == '207112':
            vpn='https://vpn1.demojam.com'
            logger.info(f'Best VPN server address is {vpn}')
            return redirect(vpn, code=302)
    except:
        return redirect('https://198.18.4.200', code=302)
if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
    # app.run(debug=True)