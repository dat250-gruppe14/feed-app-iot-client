import requests
import urllib3
import json
urllib3.disable_warnings()


class FeedAppClient:
    url = ""
    id = ""
    token = ""

    def __init__(self, config):
        self.url = config['url']
        self.id = config['id']
        self.token = 'Bearer ' + config['token']


    def _getHeaders(self):
        return {
                "Authorization": self.token, 
                "Id": self.id,
                "Content-Type": "application/json"
                }
    def getDevice(self):
        response = requests.get(self.url+'/api/device', 
                                headers=self._getHeaders(), 
                                verify=False)
        return response.json()
    def sendVotes(self, votes1, votes2):
        body = {
                "option1": votes1,
                "option2": votes2,
                }
        try:
            response = requests.post(self.url+'/api/device', data=json.dumps(body), headers=self._getHeaders(), verify=False)
            return response.json()
        except requests.exceptions.ConnectionError:
            print("Server is down")
            return "Server is down"
