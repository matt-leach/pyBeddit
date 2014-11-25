import requests
import json

class BedditRequestor(object):
    api_endpoint = None
    token = None
    user_id = None
    
    def __init__(self, token=None, api_endpoint=None, user_id=None):
        self.token = token
        self.api_endpoint = api_endpoint
        self.user_id = user_id
        
    def get_token(self, username, password):   
        
        data = {"grant_type": "password", "username": username, "password": password}
        
        r = requests.post("%s/api/v1/auth/authorize" % self.api_endpoint, data = data)
        
        if r.status_code == 200:
            content = r.json()
            self.token = content["access_token"]
            self.user_id = content["user"]
        
        else:
            raise Exception
        
        return r
    
    def get_user(self):
        auth_header = "UserToken %s" % self.token
        headers = {"authorization": auth_header}
        
        r = requests.get("%s/api/v1/user/%s" % (self.api_endpoint, self.user_id), headers=headers)
        
        return r
    
    def put_user(self, update_dict):
        auth_header = "UserToken %s" % self.token
        headers = {"authorization": auth_header}
        
        r = requests.put("%s/api/v1/user/%s" % (self.api_endpoint, self.user_id), data=json.dumps(update_dict), headers=headers)
        
        return r
    
    
    def get_all_sleeps(self, start_date, end_date):
        auth_header = "UserToken %s" % self.token
        headers = {"authorization": auth_header}
        data = {"start_date": start_date, "end_date": end_date}
        r = requests.get("%s/api/v1/user/%s/sleep" % (self.api_endpoint, self.user_id), data=data, headers=headers)
        
        return r

