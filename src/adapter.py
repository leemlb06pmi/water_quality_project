import csv
import pandas as pd
import src.models as models

class Adapter:

    def open_decoded_csv(self,decoded_csv):
        reader = csv.reader(decoded_csv.splitlines(), delimiter=',')
        output_list = list(reader)
        keys = output_list[0]
        return self.build_records(output_list[1:],keys)
    
    def build_record(self,attrs,keys):
        return models.Record(attrs,keys)
    
    def build_records(self,attrs_list,keys):
            return [self.build_record(attrs,keys) for attrs in attrs_list]
    
    def build_df(self, list_of_objs):
        list_of_dicts = [obj.__dict__ for obj in list_of_objs]
        return pd.DataFrame(list_of_dicts)