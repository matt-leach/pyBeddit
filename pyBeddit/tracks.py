class State(object):
    
    def __init__(self, time=None, value=None, meaning=""):
        self.time = time
        self.value = value
        self.meaning = meaning
        
    def __repr__(self):
        return "< %s: %s >" % (self.time, self.meaning)

class TimeValueTrack(object):
    items = []
    value_data_type = ""
    
    def __init__(self, items=[], value_data_type="", codes={}):
        self.items = []
        self.value_data_type = value_data_type
        
        for time, value in items:
            self.items.append(State(time=time, value=value, meaning=codes[value]))
            
            
        