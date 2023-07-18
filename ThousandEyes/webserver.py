from flask import Flask,redirect
from get_response_time import vpn_1, vpn_2, get_best_VPN
from get_agentID import *
app = Flask(__name__)


@app.route('/<hostname>',methods = ['GET', 'POST'])
@app.route('/',methods = ['GET', 'POST'])
def home(hostname=None):
    if hostname:
        agent_Id = get_agentId(host=hostname)
        response_time_list = get_best_VPN(agent_Id=agent_Id)
        min_response_time = min(response_time_list.values())
        for server,response_time in response_time_list.items():
            if response_time==min_response_time:              
                best_VPN = server
        if best_VPN == '190995':
            return redirect('https://198.18.4.100', code=302)
        if best_VPN == '190994':
            return redirect('https://198.18.4.200', code=302)
    else:
        return redirect('https://198.18.4.200', code=302)
if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
    # app.run(debug=True)