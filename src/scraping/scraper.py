import re, os, time
from tqdm import tqdm
from bs4 import BeautifulSoup
from .utils import create_ssl_session, save_json, load_json

session = create_ssl_session()

def get_countriesUrl():

    url = 'https://pris.iaea.org/PRIS/CountryStatistics/CountryStatisticsLandingPage.aspx'

    response = session.get(url)

    countries_list = []
    countries_url_list = []
    
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', {'id': re.compile('^MainContent_rptSideNavigation_hypNavigation_')})

        for link in tqdm(links, desc="Getting Countries URLs"):
            
            time.sleep(0.01)

            link_text = link.get_text(strip=True)
            link_href = link.get('href')

            countries_list.append(link_text)
            countries_url_list.append({"URL": link_href})

    

    data_dicts = dict(zip(countries_list, countries_url_list))
    save_json("data/countries_urls.json", data_dicts)

    return data_dicts

def get_nuclearPlantsUrl():

    url = 'https://pris.iaea.org/'

    nuclearPlants_list = []

    countries = load_json("data/countries_urls.json")
    
    for country, path in tqdm(countries.items(), desc="Getting Nuclear Plant URLs"):     

        nuclearPlants_list_country = []

        url_country = url + path["URL"]

        response = session.get(url_country)

        os.makedirs(f"data/scraped_data/{country}", exist_ok=True)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            viewstate = soup.select_one("input[name='__VIEWSTATE']")["value"]
            event_validation = soup.select_one("input[name='__EVENTVALIDATION']")["value"]

            links = soup.find_all('a', {"id": re.compile("^MainContent_MainContent_rptCountryReactors_hypReactorName_")})

            for link in links:
                
                os.makedirs(f'data/scraped_data/{country}/{link.get_text(strip=True)}', exist_ok=True)

                href = link["href"]
                if "javascript:__doPostBack" in href:
                    
                    event_target = href.split("'")[1]
                    post_data = {
                        "__EVENTTARGET": event_target,
                        "__EVENTARGUMENT": "",
                        "__VIEWSTATE": viewstate,
                        "__EVENTVALIDATION": event_validation,
                    }

                post_response = session.post(url_country, data=post_data)

                nuclearPlants_list_country.append({link.get_text(strip=True): post_response.url})

            nuclearPlants_list.append(nuclearPlants_list_country)
        
        else:
            
            print(f"Error al acceder a la página: {response.status_code}")

    return(nuclearPlants_list)
    
def get_Urls():
    datalist1 = get_countriesUrl()
    datalist2 = get_nuclearPlantsUrl()
    
    index = 0

    for data in datalist1:
        datalist1[data]["info"] = datalist2[index]
        index = index + 1
    
    save_json("data/countries_urls.json", datalist1)

def get_nuclearPlantInfo():

    if os.path.exists("data/countries_urls.json"):
        
        data = load_json("data/countries_urls.json")

        for country, info in tqdm(data.items(), desc="Getting Data"):
            for reactors in info.get("info", []):
                for reactor_name, reactor_url in reactors.items():
                    response = session.get(reactor_url)
                        
                    if response.status_code == 200:
                            
                        soup = BeautifulSoup(response.text, 'html.parser')

                        reactorStatus = soup.find('span',{"id": "MainContent_MainContent_lblReactorStatus"}).text
                        table = soup.find('table', {'class': 'layout'})

                        rows = table.find_all('tr')

                        final_headers=['Reactor Name', 'Reactor Status', 'Country',
                                        'Reactor Type', 'Model', 'Owner', 'Operator', 
                                    'Reference Unit Power (Net Capacity) [MWe]', 'Design Net Capacity [MWe]', 'Gross Capacity [MWe]', 'Thernmal Capacity [MWt]', 
                                    'Construcion Start Date', 'First Criticality Date', 'Construction Suspended Date', 'Construction Restart Date',
                                    'First Grid Connection', 'Commercial Operation Date', 'Suspended Operation Date', 'End of Suspended Operation Date',
                                    'Permanent Shutdown Date']
                        data = []

                        data.append(reactor_name)
                        data.append(reactorStatus)
                        data.append(country)

                        keys = final_headers

                        index = 1
                        
                        
                        while index < len(rows):
                            headers = rows[index].find_all('td')  


                            for header in headers:

                                data.append(header.get_text(strip=True))
                    
                            index += 2
                        
                        data_dicts = dict(zip(keys, data))

                        cleaned_data = {}

                        for key, value in data_dicts.items():

                            if isinstance(value, str) and (value.endswith("MWe") or value.endswith("MWt")): 
                                match = re.match(r"(\d+)", value) 
                                cleaned_data[key] = match.group(1)
                            else:
                                cleaned_data[key] = value

                        save_json(f'data/scraped_data/{country}/{reactor_name}/{reactor_name}_data.json', cleaned_data)

                    else:
                        print({response.status_code})
    else:
        print("---  countries_urls.json | not found  ---")
        print("---  Getting URLs  ---")
        get_Urls()
        get_nuclearPlantInfo()
            
def get_nuclearPlantAnnualData():

    if os.path.exists("data/countries_urls.json"):
        
        data = load_json("data/countries_urls.json")

        for country, info in tqdm(data.items(), desc="Getting Data"):
            for reactors in info.get("info", []):
                for reactor_name, reactor_url in reactors.items():

                    response = session.get(reactor_url)

                    if response.status_code == 200:

                        soup = BeautifulSoup(response.text, 'html.parser')
                        ReactorStatus = soup.find('span',{"id": "MainContent_MainContent_lblReactorStatus"}).text

                        if ReactorStatus == "Under Construction":

                            save_json(f'data/scraped_data/{country}/{str(reactor_name).lstrip()}/{str(reactor_name).lstrip()}_AnualData.json', {})
                            
                        else:

                            table = soup.find('table', {'class': 'active'})

                            rows = table.find_all('tr')

                            final_headers = []
                            headers = rows[0].find_all('th')
                            sub_headers = rows[1].find_all('th')
                            n_cols = 0

                            data = []

                            for header in headers:

                                if header.get('colspan'):

                                    for i in range(n_cols, n_cols + int(header.get('colspan'))):
                                        if i < len(sub_headers):
                                            final_headers.append(f'{header.get_text(strip=True)}_{sub_headers[i].get_text(strip=True)}')
                                    
                                    n_cols = n_cols + int(header.get('colspan'))
                                else:
                                    final_headers.append(header.get_text(strip=True))

                            keys = final_headers

                            for row in rows[2:]:

                                cells = row.find_all('td')

                                row_data = []

                                for cell in cells:

                                    if cell.get('colspan'):

                                        for i in range(int(cell.get('colspan'))):
                                            row_data.append(cell.get_text(strip=True))

                                    else:

                                        row_data.append(cell.get_text(strip=True))

                                data.append(row_data)

                            for row in data:
                                data_dicts = [dict(zip(keys, row)) for row in data]

                                save_json(f'data/scraped_data/{country}/{str(reactor_name).lstrip()}/{str(reactor_name).lstrip()}_AnualData.json', data_dicts)
                    else:
                        print({response.status_code})
    else:
        print("---  countries_urls.json | not found  ---")
        print("---  Getting URLs  ---")
        get_Urls()
        get_nuclearPlantInfo()


    