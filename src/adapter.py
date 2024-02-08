import csv
import src.record as rec

class Adapter:

    def open_decoded_csv(self,decoded_csv):
        reader = csv.reader(decoded_csv.splitlines(), delimiter=',')
        output_list = list(reader)
        keys = output_list[0]
        return self.build_records(output_list[1:],keys)
    
    def build_record(self,attrs,keys):
        return rec.Record(attrs,keys)
    
    def build_records(self,attrs_list,keys):
            return [self.build_record(attrs,keys) for attrs in attrs_list]