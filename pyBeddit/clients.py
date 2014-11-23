from pyBeddit.requestors import BedditRequestor
from pyBeddit.resources import SleepDataResource
from collections import OrderedDict

API_ENDPOINT = "https://cloudapi.beddit.com"

class BedditClient(object):
    
    def __init__(self, token=None, api_endpoint=API_ENDPOINT, user_id=None):
        self.requestor = BedditRequestor(token=token, api_endpoint=api_endpoint, user_id=user_id)
      
      
    def get_token(self, username, password):
        try:
            self.requestor.get_token(username, password)
        except:
            raise Exception("could not authenticate")
        
        return self.requestor.token, self.requestor.user_id
        
    def get_latest_sleep(self):
        # TODO: no longer hard coded
        r = self.requestor.get_all_sleeps("2014-01-01", "2015-01-01")
        data_dict = r.json()[-1]
        sleep_data = SleepDataResource(data_dict)
        return sleep_data
    
    def get_sleep_scores(self):
        r = self.requestor.get_all_sleeps("2014-01-01", "2015-01-01")
        
        sleep_data = OrderedDict()
        
        print r.content
        
        for sleep_obj in r.json():
            sleep_resource = SleepDataResource(sleep_obj)
            print sleep_resource.date, sleep_resource.properties.total_sleep_score
            sleep_data[sleep_resource.date] = sleep_resource.properties.total_sleep_score
            
        return sleep_data