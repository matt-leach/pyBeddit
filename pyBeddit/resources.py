from pyBeddit import fields

    
class BedditResourceType(type):
    """
    Beddit Resource Metaclass
    """
    def __init__(self, name, bases, attrs):
        super(BedditResourceType, self).__init__(name, bases, attrs)

        if "fields" in attrs:
            # be careful with lists and copying
            self.fields = list(attrs["fields"])
        else:
            self.fields = []
        
        for field_name, field_type in attrs.items():
            # Now add each Field defined to the fields attribute
            if fields.Field in type(field_type).__bases__:
                self.fields.append(field_name)


class BedditResource(object):   
    __metaclass__ = BedditResourceType
    
    def __init__(self, data_dict):
        
        for field_name, value in data_dict.items():
            try:
                setattr(self, field_name, value)
            except ValueError:
                raise Exception("no field %s" % field_name)


class SleepPropertiesResource(BedditResource):
    
    score_snoring = fields.floatField()
    sleep_time_target = fields.floatField()
    away_episode_count = fields.floatField()
    sleep_latency = fields.floatField()
    total_sleep_score = fields.floatField()
    stage_duration_A = fields.floatField()
    total_snoring_episode_duration = fields.floatField()
    average_respiration_rate = fields.floatField()
    short_term_average_respiration_rate = fields.floatField()
    stage_duration_G = fields.floatField()
    short_term_resting_heart_rate = fields.floatField()
    resting_heart_rate = fields.floatField()
    score_sleep_latency = fields.floatField()
    score_awakenings = fields.floatField()
    score_bed_exits = fields.floatField()
    score_sleep_efficiency = fields.floatField()
    stage_duration_S = fields.floatField()
    score_amount_of_sleep = fields.floatField()
    stage_duration_W = fields.floatField()

    def __repr__(self):
        return "< Sleep Properties: Score %s >" % self.total_sleep_score



class SleepDataResource(BedditResource):
    
    date = fields.dateField()
    timezone = fields.stringField()
    start_timestamp = fields.integerField()
    end_timestamp = fields.integerField()
    session_range_start = fields.integerField()
    session_range_end = fields.integerField()
    properties = fields.relatedField(SleepPropertiesResource)
    
    def __repr__(self):
        return "< Sleep %s >" % (self.date)


  