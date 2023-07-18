import requests


headers = {
    'Authorization': 'Basic dGhhbmRvYW5AY2lzY28uY29tOm5lOTVma3dpYXJrMGsweGhjYnFrY21ia25vcmtpeGw2'
}



base_url = 'https://api.thousandeyes.com/'


uri = 'v6/endpoint-agents.json'
def get_agentId(host=None):
    response = requests.get(url=base_url+uri,headers=headers)
    # hostname = socket.gethostname()
    for agent in response.json()['endpointAgents']:
        if agent['computerName'] == host:
            agent_id = agent['agentId']
            break
    # with open('agentid.yaml', 'w') as f:
    #     f.write(agent_id)
    return agent_id





