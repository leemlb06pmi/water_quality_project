class Record:
    selected_keys = ['OrganizationFormalName','ActivityMediaSubdivisionName','ActivityStartDate','ActivityConductingOrganizationText',
                     'MonitoringLocationIdentifier','CharacteristicName','ResultSampleFractionText','ResultMeasureValue',
                     'ResultMeasure/MeasureUnitCode']
    def __init__(self,attrs,keys):
        self.__dict__={k:v for k,v in self.build_dict(keys,attrs).items() if k in self.selected_keys}
    
    def build_dict(self,keys,attrs):
        return dict(zip(keys,attrs))