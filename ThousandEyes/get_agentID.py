import requests


headers = {
    'Authorization': 'Bearer 1a7b95ff-5aa6-421a-9ec8-d0b7bf63e67a'
}



base_url = 'https://api.thousandeyes.com/'



def get_agentId(host=None):
    uri = 'v6/endpoint-agents.json'
    response = requests.get(url=base_url+uri,headers=headers)
    # hostname = socket.gethostname()
    for agent in response.json()['endpointAgents']:
        if agent['computerName'] == host:
            agent_id = agent['agentId']
            break
    # with open('agentid.yaml', 'w') as f:
    #     f.write(agent_id)
    return agent_id
    # return response

def get_testId():
    uri='/v6/tests.json'
    response = requests.get(url=base_url+uri,headers=headers)
    return response.text



if __name__=='__main__':
    agent_id=get_agentId(host='PC01')

    print(agent_id)
    # test_id=get_testId()
    # print(test_id)



