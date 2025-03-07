import re
import os
import json
import matplotlib.pyplot as plt
import pycountry
from .utils import generate_colors, abreviature_country, load_json_generalData

plt.figure(figsize=(15, 6))

graph_location = "src/data/analized_data/graphs"

def analizer_method():
    graph_numberReactorsStatus()
    graph_numberReactorsType()
    graph_numberReactorsCountry()

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

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(keys, values, color=colors)

    plt.bar(keys, values, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Status")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.savefig(f"{graph_location}/nuclear_plants_status.png", dpi=300, bbox_inches='tight')

    plt.show()

def graph_numberReactorsType():

    list_types = {}

    json_data_list = load_json_generalData()

    for data in json_data_list:

        reactor_status = data["Reactor Type"]

        if reactor_status not in list_types:
            list_types[reactor_status] = 1
        else:
            list_types[reactor_status] += 1

    values = list_types.values()
    keys = list_types.keys()

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(keys, values, color=colors)

    plt.bar(keys, values, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Status")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

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

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(keys, values, color=colors)

    plt.bar(keys, values, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Country")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.savefig(f"{graph_location}/nuclear_plants_country.png", dpi=300, bbox_inches='tight')

    plt.show()
                        
