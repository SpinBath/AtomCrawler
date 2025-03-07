import re
import os
import json
import matplotlib.pyplot as plt
import pycountry
from .utils import generate_colors, abreviature_country, load_json_generalData


graph_location = "data/analized_data/graphs"

def analizer_method():
    graph_numberReactorsStatus()
    graph_numberReactorsType()
    graph_numberReactorsCountry()
    graph_efficiencyReactor()
    graph_grossCapacityReactor()

def graph_numberReactorsStatus():

    list_types = {}

    json_data_list = load_json_generalData()

    for data in json_data_list:

        reactor_status = data["Reactor Status"]

        if reactor_status not in list_types:
            list_types[reactor_status] = 1
        else:
            list_types[reactor_status] += 1

    list_types = dict(sorted(list_types.items(), key=lambda item: item[1], reverse=True))
    
    values = list_types.values()
    keys = list_types.keys()

    plt.figure(figsize=(15, 6))

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(keys, values, color=colors)

    plt.bar(keys, values, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Status")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.tight_layout()
    plt.savefig(f"{graph_location}/nuclear_plants_status.png", dpi=300, bbox_inches='tight')
    plt.show()

def graph_numberReactorsType():

    list_types = {}

    json_data_list = load_json_generalData()

    for data in json_data_list:

        reactor_type = data["Reactor Type"]

        if reactor_type not in list_types:
            list_types[reactor_type] = 1
        else:
            list_types[reactor_type] += 1

    list_types = dict(sorted(list_types.items(), key=lambda item: item[1], reverse=True))
    list_types = dict(list(list_types.items())[:12])

    values = list_types.values()
    keys = list_types.keys()

    plt.figure(figsize=(13, 6))

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(keys, values, color=colors)

    plt.bar(keys, values, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Type")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.tight_layout()
    plt.savefig(f"{graph_location}/nuclear_plants_types.png", dpi=300, bbox_inches='tight')
    plt.show()

def graph_numberReactorsCountry():

    list_types = {}

    json_data_list = load_json_generalData()

    for data in json_data_list:

        reactor_status = data["Country"]
                                
        if data["Reactor Status"] == "Operational":
            if reactor_status not in list_types:
                list_types[reactor_status] = 1
            else:
                list_types[reactor_status] += 1

    list_types = dict(sorted(list_types.items(), key=lambda item: item[1], reverse=True))
    list_types = dict(list(list_types.items())[:12])

    values = list_types.values()
    keys = [f"{abreviature_country(key)}" for key, value in list_types.items()]

    plt.figure(figsize=(7, 6))

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(keys, values, color=colors)

    plt.bar(keys, values, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Top Countries (Top 12)")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.tight_layout()
    plt.savefig(f"{graph_location}/nuclear_plants_country.png", dpi=300, bbox_inches='tight')
    plt.show()
                        
def graph_efficiencyReactor():

    list_reactors = {}

    json_data_list = load_json_generalData()

    for data in json_data_list:
           
        if data["Reactor Status"] == "Operational":
            
            reactor_name = data["Reactor Name"]
            term = data["Thernmal Capacity [MWt]"]
            net_power = data["Reference Unit Power (Net Capacity) [MWe]"]

            efficiency = round(int(net_power) / int(term) * 100, 2)
            list_reactors[reactor_name] = efficiency
           
    list_reactors = dict(sorted(list_reactors.items(), key=lambda item: item[1], reverse=True))
    list_reactors = dict(list(list_reactors.items())[:15])

    values = list_reactors.values()
    keys = list_reactors.keys()

    plt.figure(figsize=(10, 5))

    colors = generate_colors('#80baff', len(list_reactors))

    bars = plt.barh(keys, values, color=colors)

    plt.barh(keys, values, color=colors)

    plt.xlabel("Efficiency (%)")
    plt.xlim(0, 100)

    plt.ylabel("Reactor Name")
    plt.gca().invert_yaxis()

    plt.title("Most Efficient Reactors (Top 15)")


    for bar in bars:
        plt.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():,.2f}%', va='center')

    plt.tight_layout()
    plt.savefig(f"{graph_location}/nuclear_plants_efficiency.png", dpi=300, bbox_inches='tight')
    plt.show()

def graph_grossCapacityReactor():

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

    # Ajuste de etiquetas y título
    plt.xlabel("Gross Capacity (MWe)", fontsize=12)
    plt.xlim(0, 2500)

    plt.ylabel("Nuclear Plants", fontsize=12)
    plt.gca().invert_yaxis()

    plt.title("Top 12 Nuclear Plants by Gross Capacity", fontsize=14)


    for bar in bars:
        plt.text(bar.get_width() + 25, bar.get_y() + bar.get_height()/2, f'{bar.get_width():,.0f} MWe', va='center')

    plt.tight_layout()
    plt.savefig(f"{graph_location}/nuclear_plants_gross.png", dpi=300, bbox_inches='tight')
    plt.show()

