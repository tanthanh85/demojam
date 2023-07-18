import requests
from pprint import pprint
# from get_agentID import *

headers = {
    'Authorization': 'Bearer 1a7b95ff-5aa6-421a-9ec8-d0b7bf63e67a'
}
#test ID for ISE
test_ids = ['206945','207112']


base_url = 'https://api.thousandeyes.com/'

vpn_1 = 'https://198.18.4.100'
vpn_2 = 'https://198.18.4.200'
# agent_Id = get_agentId()

def get_best_VPN(agent_Id=None):
    response_time_list = {}
    for test_id in test_ids:
        uri = f'/v6/endpoint-data/tests/web/http-server/{test_id}.json'
        response = requests.get(url=base_url+uri,headers=headers)
        for metric in response.json()['endpointWeb']['httpServer']:
            if metric['agentId'] == agent_Id:
                # print(f"Average response time from VPN Server " + metric['serverIp'] + f" to agent {agent_Id}" + " is " + str(metric['responseTime']) + " ms")
                response_time_list[test_id] = metric['responseTime']
    return response_time_list


if __name__=='__main__':
    response_time_list=get_best_VPN(agent_Id='b72a845f-8a86-4e7e-8664-27fbb58c702d')

    print(response_time_list)
   