from pyBeddit.requestors import BedditRequestor
from pyBeddit.resources import SleepDataResource

class BedditClient(object):
    
    def __init__(self, token=None, api_endpoint="", user_id=None):
        self.requestor = BedditRequestor(token=token, api_endpoint=api_endpoint)
      
      
    def get_token(self, username, password):
        try:
            self.requestor.get_token(username, password)
        except:
            raise Exception("could not authenticate")
        
        
    def get_latest_sleep(self):
        # TODO: no longer hard coded
        r = self.requestor.get_all_sleeps("2014-01-01", "2015-01-01")
        data_dict = r.json()[-1]
        sleep_data = SleepDataResource(data_dict)
        return sleep_data
    