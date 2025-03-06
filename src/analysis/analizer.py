import re
import os
import json
import matplotlib.pyplot as plt
from .utils import generate_colors

plt.figure(figsize=(15, 6))


graph_location = "src/data/analized_data/graphs"

def analizer_method():
    graph_numberReactorsType()

def graph_numberReactorsStatus():

    location = "src/data/scraped_data"

    list_types = {}

    for files in os.walk(location):
        for dir in files:
            for data in dir:
                if data.endswith("_data.json"):
                    url = (f'{files[0]}/{data}')
                    with open(url, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        reactor_status = data["Reactor Status"]

                        if reactor_status not in list_types:
                            list_types[reactor_status] = 1
                        else:
                            list_types[reactor_status] += 1

    list_types = dict(sorted(list_types.items(), key=lambda item: item[1], reverse=True))
    
    valores = list_types.values()
    etiquetas = list_types.keys()

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(etiquetas, valores, color=colors)

    plt.bar(etiquetas, valores, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Status")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.savefig(f"{graph_location}/nuclear_plants_status.png", dpi=300, bbox_inches='tight')

    plt.show()

def graph_numberReactorsType():

    location = "src/data/scraped_data"

    list_types = {}

    for files in os.walk(location):
        for dir in files:
            for data in dir:
                if data.endswith("_data.json"):
                    url = (f'{files[0]}/{data}')
                    with open(url, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        reactor_status = data["Reactor Type"]

                        if reactor_status not in list_types:
                            list_types[reactor_status] = 1
                        else:
                            list_types[reactor_status] += 1

    valores = list_types.values()
    etiquetas = list_types.keys()

    colors = generate_colors('#80baff', len(list_types))

    bars = plt.bar(etiquetas, valores, color=colors)

    plt.bar(etiquetas, valores, color=colors)

    plt.ylabel("Nº Nuclear Plants")
    plt.title("Nuclear Plants Status")

    legend_labels = [f"{key}: {value}" for key, value in list_types.items()]
    plt.legend(bars, legend_labels, loc="upper right")

    plt.savefig(f"{graph_location}/nuclear_plants_types.png", dpi=300, bbox_inches='tight')

    plt.show()
                        
