class Record:
    selected_keys = ['OrganizationFormalName','ActivityMediaSubdivisionName','ActivityStartDate','ActivityConductingOrganizationText',
                     'MonitoringLocationIdentifier','CharacteristicName','ResultSampleFractionText','ResultMeasureValue',
                     'ResultMeasure/MeasureUnitCode',]
    def __init__(self,attrs,keys):
        for keys in self.selected_keys:
            self.__dict__=dict(zip(keys,attrs))