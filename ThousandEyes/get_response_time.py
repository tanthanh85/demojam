import requests
# from get_agentID import *

headers = {
    'Authorization': 'Basic dGhhbmRvYW5AY2lzY28uY29tOm5lOTVma3dpYXJrMGsweGhjYnFrY21ia25vcmtpeGw2'
}
#test ID for ISE
test_ids = ['190994','190995']


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