from weakref import WeakKeyDictionary


class Field(object):
    value = None
    units = None
    
    def __init__(self, units=None, choices=[]):
        self.data = WeakKeyDictionary()
        self.units = units
        
    def __get__(self, instance, owner):
        if instance is None:
            return self        
        return self.data.get(instance)
        
    
    def __set__(self, instance, value):
        self.data[instance] = value
        


class stringField(Field):
    pass
    
    

class dateField(Field):
    pass

    
class integerField(Field):
    
    def __set__(self, instance, value):
        try:
            self.data[instance] = int(value)
        except:
            # TODO: null=True?
            if value is None:
                self.data[instance] = None
            else:
                raise ValueError("Integer value required.")


class floatField(Field):
    
    def __set__(self, instance, value):
        try:
            self.data[instance] = float(value)
        except (ValueError, TypeError):
            # TODO: null=True?
            if value is None:
                self.data[instance] = None
            else:
                raise ValueError("Float required.")



class relatedField(Field):
    resource = None
    
    def __init__(self, resource):
        super(relatedField, self).__init__()
        self.resource = resource
        
        
    def __set__(self, instance, value):
        resource_filled = self.resource(value)
        self.data[instance] = resource_filled
    
        
        
        
        
        
        
class listField(Field):
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Integer value required.")
        
        
        
        
        
        