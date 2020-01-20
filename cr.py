import requests as rq
import json


class CustomRequest:
    def __init__(self,url):
    
        self.url = url
        self.headers = {'content-type': "application/json",'cache-control': "no-cache"}
        
    def request(self,payload):
    
        payload = json.dumps(payload)
        
        res = rq.request("POST", self.url,data=payload, headers=self.headers)
        
        return json.loads(res.text)
        
    def getXP(self,level):
    
        payload = {"type": "level","level": level}
        
        data = self.request(payload)
        
        return data["xp"]
        
    def getLevel(self,xp):
        payload =  {"type": "xp","xp": xp}
        
        data = self.request(payload)
        
        return data["level"]