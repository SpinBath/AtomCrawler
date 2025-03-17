import matplotlib.colors as mcolors
import numpy as np
import os
import json

def generate_colors(start_color, num_colors):
    start_rgb = np.array(mcolors.to_rgb(start_color)) 
    factor = np.linspace(0.2, 1, num_colors)  
    
    colors = [mcolors.to_hex(start_rgb * f) for f in factor]
    return colors

def abreviature_country(country):
    
    abr_list = {
    'Argentina': 'AR',
    'Armenia': 'AM',
    'Belarus': 'BY',
    'Belgium': 'BE',
    'Brazil': 'BR',
    'Bulgaria': 'BG',
    'Canada': 'CA',
    'China': 'CN',
    'Czech Republic': 'CZ',
    'Finland': 'FI',
    'France': 'FR',
    'Hungary': 'HU',
    'India': 'IN',
    'Iran, Islamic Republic of': 'IR',
    'Japan': 'JP',
    'Korea, Republic of': 'KR',
    'Mexico': 'MX',
    'Netherlands, Kingdom of The': 'NL',
    'Pakistan': 'PK',
    'Romania': 'RO',
    'Russia': 'RU',
    'Slovakia': 'SK',
    'Slovenia': 'SI',
    'South Africa': 'ZA',
    'Spain': 'ES',
    'Sweden': 'SE',
    'Switzerland': 'CH',
    'Ukraine': 'UA',
    'United Arab Emirates': 'AE',
    'United Kingdom': 'GB',
    'United States of America': 'US'
}
    
    for coun, abr in abr_list.items():
        if country == coun:
            return abr

def update_json(filename, data):

    if os.path.exists(filename):

        with open(filename, "r", encoding="utf-8") as f:
            current_data = json.load(f)

        if isinstance(current_data, list):
            if isinstance(data, list):
                current_data.extend(data)

        elif isinstance(current_data, dict):
            if isinstance(data, dict):
                current_data.update(data)
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)

def load_json_generalData():

    location = "data/sanitize_data"
    
    json_data_list = []
    
    for root, _, files in os.walk(location):
        for file in files:
            if file.endswith("_data.json"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    json_data_list.append(data)
    
    return json_data_list
       
def load_json_annualData(reactor_name):

    location = "data/sanitize_data"
    
    json_data_list = []
    
    for root, _, files in os.walk(location):
        for file in files:
            if file == (f'{reactor_name}_AnualData.json'):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    json_data_list.append(data)
    
    return json_data_list
