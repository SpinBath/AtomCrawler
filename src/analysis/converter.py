from .utils import load_json_generalData
import pandas as pd
import json
import re
import os
import datetime

def converter_method():
    Docs.generate()

class Docs():

    def generate():

        data = load_json_generalData()
        dict_data = []

        date_str = datetime.date.today().strftime("%Y-%m-%d")

        dir_name = f"docs/{date_str}"

        os.makedirs(dir_name, exist_ok=True)

        for file in data:
            dict_data.append(file)
        
        df = pd.DataFrame(dict_data)
        df.to_csv(f"{dir_name}/general_data.csv", index=False, encoding="utf-8")

        df = df.where(pd.notnull(df), None)
        
        df.columns = [col.replace(" ", "_").replace("[", "").replace("]", "").replace("%", "") for col in df.columns]
        df.columns = [re.sub(r'\W|^(?=\d)', '_', col) for col in df.columns]

        df.to_xml(f"{dir_name}/general_data.xml", index=False, encoding="utf-8")



    