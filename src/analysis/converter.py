from .utils import load_json_generalData
import pandas as pd
import json

def converter_method():
    Docs.generate_csv()

class Docs():

    def generate_csv():

        data = load_json_generalData()
        dict_data = []
        for file in data:
            dict_data.append(file)

        df = pd.DataFrame(dict_data)
        df.to_csv("CSVs/general_data.csv", index=False)



    