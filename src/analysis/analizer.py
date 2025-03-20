import re
import os
import json
import matplotlib.pyplot as plt
import pycountry
import pandas as pd
from .utils import generate_colors, abreviature_country, load_json_generalData, load_json_annualData, update_json
from datetime import datetime
import locale


graph_location = "data/analized_data/graphs"

def analizer_method():
    Data.reactor_hours_on_line()

class Graph():

    def numberReactorsStatus():

        df = pd.DataFrame(load_json_generalData())

        reactor_status_counts = df["Reactor Status"].value_counts()
        
        values = reactor_status_counts.values
        keys = reactor_status_counts.index

        plt.figure(figsize=(15, 6))

        colors = generate_colors('#80baff', len(reactor_status_counts))

        bars = plt.bar(keys, values, color=colors)

        plt.bar(keys, values, color=colors)

        plt.ylabel("Nº Nuclear Plants")
        plt.title("Nuclear Plants Status")

        legend_labels = [f"{key}: {value}" for key, value in reactor_status_counts.items()]
        plt.legend(bars, legend_labels, loc="upper right")

        plt.tight_layout()
        plt.savefig(f"{graph_location}/nuclear_plants_status.png", dpi=300, bbox_inches='tight')
        plt.show() 

    def numberReactorsType():

        df = pd.DataFrame(load_json_generalData())

        reactor_type_counts = df["Reactor Type"].value_counts()
        
        values = reactor_type_counts.values
        keys = reactor_type_counts.index

        plt.figure(figsize=(13, 6))

        colors = generate_colors('#80baff', len(reactor_type_counts))

        bars = plt.bar(keys, values, color=colors)

        plt.bar(keys, values, color=colors)

        plt.ylabel("Nº Nuclear Plants")
        plt.title("Nuclear Plants Type")

        legend_labels = [f"{key}: {value}" for key, value in reactor_type_counts.items()]
        plt.legend(bars, legend_labels, loc="upper right")

        plt.tight_layout()
        plt.savefig(f"{graph_location}/nuclear_plants_types.png", dpi=300, bbox_inches='tight')
        plt.show()

    def numberReactorsCountry():

        df = pd.DataFrame(load_json_generalData())
        
        df_OperationalReactor = df[df["Reactor Status"] == "Operational"]

        df_ReactorCountrys = df_OperationalReactor["Country"].value_counts()

        top_countries = df_ReactorCountrys.nlargest(12)

        keys = [abreviature_country(country) for country in top_countries.index]
        values = top_countries.values

        plt.figure(figsize=(7, 6))

        colors = generate_colors('#80baff', len(top_countries))

        bars = plt.bar(keys, values, color=colors)

        plt.bar(keys, values, color=colors)

        plt.ylabel("Nº Nuclear Plants")
        plt.title("Top 12 Countries by Reactor Count")

        legend_labels = [f"{key}: {value}" for key, value in top_countries.items()]
        plt.legend(bars, legend_labels, loc="upper right")

        plt.tight_layout()
        plt.savefig(f"{graph_location}/nuclear_plants_country.png", dpi=300, bbox_inches='tight')
        plt.show()
                        
    def efficiencyReactor():

        df = pd.DataFrame(load_json_generalData())
        
        df_OperationalReactor = df[df["Reactor Status"] == "Operational"]

        top_reactors = df_OperationalReactor.nlargest(15, "Thermal Efficiency [%]")

        keys = top_reactors["Reactor Name"].values
        values = top_reactors["Thermal Efficiency [%]"].values

        plt.figure(figsize=(10, 5))

        colors = generate_colors('#80baff', len(top_reactors))

        bars = plt.barh(keys, values, color=colors)

        plt.barh(keys, values, color=colors)

        plt.xlabel("Thermal Efficiency (%)")
        plt.xlim(0, 100)

        plt.ylabel("Reactor Name")
        plt.gca().invert_yaxis()

        plt.title("Top 15 Nuclear Plants by Thermal Efficiency")


        for bar in bars:
            plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():,.2f}%', va='center')

        plt.tight_layout()
        plt.savefig(f"{graph_location}/nuclear_plants_efficiency.png", dpi=300, bbox_inches='tight')
        plt.show()

    def grossCapacityReactor():

        list_reactors = {}

        json_data_list = load_json_generalData()

        for data in json_data_list:

            if data["Reactor Status"] == "Operational":
                
                reactor_name = data["Reactor Name"]
                gross_capacity = data["Gross Capacity [MWe]"]

                list_reactors[reactor_name] = int(gross_capacity)
            

        list_reactors = dict(sorted(list_reactors.items(), key=lambda item: item[1], reverse=True))
        list_reactors = dict(list(list_reactors.items())[:12])

        values = list_reactors.values()
        keys = list_reactors.keys()

        plt.figure(figsize=(13, 6))

        colors = generate_colors('#80baff', len(list_reactors))

        bars = plt.barh(keys, values, color=colors)

        plt.xlabel("Gross Capacity (MWe)")
        plt.xlim(0, 2500)

        plt.ylabel("Nuclear Plants")
        plt.gca().invert_yaxis()

        plt.title("Top 12 Nuclear Plants by Gross Capacity")


        for bar in bars:
            plt.text(bar.get_width() + 25, bar.get_y() + bar.get_height()/2, f'{bar.get_width():,.0f} MWe', va='center')

        plt.tight_layout()
        plt.savefig(f"{graph_location}/nuclear_plants_gross.png", dpi=300, bbox_inches='tight')
        plt.show()

    def reactorYearConstruction():

        df = pd.DataFrame(load_json_generalData)

        df_reactorYears = df["Years Connected"]

        plt.figure(figsize=(25, 6))

        colors = generate_colors('#80baff', len(df_reactorYears))

        bars = plt.bar(keys, values, color=colors)

        plt.bar(keys, values, color=colors)
        plt.xticks(rotation=75)
        plt.title("Historical Nuclear Plant Construction (Construcion Start Date)")
        plt.ylabel("Nº Nuclear Plants")

        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                    str(bar.get_height()),  
                    ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        plt.savefig(f"{graph_location}/nuclear_plants_year.png", dpi=300, bbox_inches='tight')
        plt.show()

class Data():

    def thermal_efficiency():

        location = "data/sanitize_data"
            
        for root, _, files in os.walk(location):
            for file in files:
                if file.endswith("_data.json"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                                    
                        term = data["Thermal Capacity [MWt]"]
                        net_power = data["Reference Unit Power (Net Capacity) [MWe]"]

                        efficiency = round(net_power / term * 100, 2)
                        data["Thermal Efficiency [%]"] = efficiency
                    
                        with open(file_path, "w", encoding="utf-8") as f:
                                json.dump(data, f, ensure_ascii=False, indent=4)


    def reactor_age():

        location = "data/sanitize_data"
            
        for root, _, files in os.walk(location):
            for file in files:
                if file.endswith("_data.json"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        list_data = load_json_annualData(data["Reactor Name"])

                        df = pd.DataFrame(list_data)

                        num_rows, num_columns = df.shape
                            
                        data["Years Connected"] = num_columns

                        with open(file_path, "w", encoding="utf-8") as f:
                                json.dump(data, f, ensure_ascii=False, indent=4)

    def reactor_hours_on_line():
        
        location = "data/sanitize_data"
            
        for root, _, files in os.walk(location):
            for file in files:
                if file.endswith("_data.json"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        list_data = load_json_annualData(data["Reactor Name"])

                        for annual_data in list_data: 
                            try:
                                df = pd.DataFrame(annual_data)
                                df["Annual Time On Line[h]"] = pd.to_numeric(df["Annual Time On Line[h]"], errors='coerce')

                                df_clean = df.dropna()
                                total_hours = int(df_clean["Annual Time On Line[h]"].values.sum())

                                data["Hours On Line"] = total_hours   
       
                            except:
                                data["Hours On Line"] = 0

                        with open(file_path, "w", encoding="utf-8") as f:
                                json.dump(data, f, ensure_ascii=False, indent=4) 
