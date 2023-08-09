import requests
from pprint import pprint


headers = {
    'Authorization': 'Bearer 009a4eb6-30a5-46b5-a8df-c2bd0d93226a'
}



base_url = 'https://api.thousandeyes.com/'



def get_agentId(host=None):
    uri = 'v6/endpoint-agents.json'
    response = requests.get(url=base_url+uri,headers=headers)
    # hostname = socket.gethostname()
    # for agent in response.json()['endpointAgents']:
    #     if agent['computerName'] == host:
    #         agent_id = agent['agentId']
            # break
    # with open('agentid.yaml', 'w') as f:
    #     f.write(agent_id)
    # return agent_id
    return response.json()

def get_agentId_byIP(IP=None):
    uri = 'v6/endpoint-agents.json'
    response = requests.get(url=base_url+uri,headers=headers)
    # pprint(response.text,indent=2)
    with open('agent.json', 'w') as f:
        f.write(response.text)
    for agent in response.json()['endpointAgents']:
        # if agent['networkInterfaceProfiles'][0]['addressProfiles'][0]['ipAddress'] == IP:
        #     agent_id = agent['agentId']
        #     break
        for address in agent['networkInterfaceProfiles']:
            if address['addressProfiles'][0]['ipAddress'] == IP:
                agent_id = agent['agentId']
                break

    # with open('agentid.yaml', 'w') as f:
    #     f.write(agent_id)
    return agent_id
    # return response.json()

def get_testId():
    uri='/v6/tests.json'
    response = requests.get(url=base_url+uri,headers=headers)
    return response.text



if __name__=='__main__':
    agent_id=get_agentId_byIP(IP='198.18.4.10')

    pprint(agent_id)



