from .utils import load_json_generalData
import pandas as pd
import json
import re

def converter_method():
    Docs.generate_csv()

class Docs():

    def generate_csv():

        data = load_json_generalData()
        dict_data = []
        for file in data:
            dict_data.append(file)
        
        df = pd.DataFrame(dict_data)
        df.to_csv("docs/general_data.csv", index=False, encoding="utf-8")

        df = df.where(pd.notnull(df), None)
        
        df.columns = [col.replace(" ", "_").replace("[", "").replace("]", "").replace("%", "") for col in df.columns]
        df.columns = [re.sub(r'\W|^(?=\d)', '_', col) for col in df.columns]

        df.to_xml("docs/general_data.xml", index=False, encoding="utf-8")



    