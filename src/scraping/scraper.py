import re, os, time
from tqdm import tqdm
from bs4 import BeautifulSoup
from .utils import create_ssl_session, save_json, load_json

session = create_ssl_session()

def get_countries():

    url = 'https://pris.iaea.org/PRIS/CountryStatistics/CountryStatisticsLandingPage.aspx'

    response = session.get(url)

    countries_list = []
    countries_url_list = []
    
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', {'id': re.compile('^MainContent_rptSideNavigation_hypNavigation_')})

        for link in tqdm(links, desc="Getting Data", unit="Country URL"):
            
            time.sleep(0.01)

            link_text = link.get_text(strip=True)
            link_href = link.get('href')

            countries_list.append(link_text)
            countries_url_list.append(link_href)


    data_dicts = dict(zip(countries_list, countries_url_list))

    save_json('countries.json', data_dicts)

def get_nuclearPlant():

    url = 'https://pris.iaea.org/'

    countries = load_json('countries.json')
    
    index = 0

    for country, path in countries.items():     

        url_country = url + path

        response = session.get(url_country)

        os.makedirs(f"src/data/{country}", exist_ok=True)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            links = soup.find_all('a', {"id": re.compile("^MainContent_MainContent_rptCountryReactors_hypReactorName_")})

            for nuclearPlantName in links:
                
                os.makedirs(f'src/data/{country}/{nuclearPlantName.get_text(strip=True)}', exist_ok=True)

            for link in links:
                href = link["href"]
                if "javascript:__doPostBack" in href:
                    
                    event_target = href.split("'")[1]

                    viewstate = soup.select_one("input[name='__VIEWSTATE']")["value"]
                    event_validation = soup.select_one("input[name='__EVENTVALIDATION']")["value"]

                    post_data = {
                        "__EVENTTARGET": event_target,
                        "__EVENTARGUMENT": "",
                        "__VIEWSTATE": viewstate,
                        "__EVENTVALIDATION": event_validation,
                    }

                post_response = session.post(url_country, data=post_data)
                
                get_nuclearPlantAnnualData(post_response.url, country)
                get_nuclearPlantInfo(post_response.url, country)

                index = index + 1

                print(" " * 60, end="\r")
                print(f'{country} Data Uploaded ... ({index}/712)', end='\r')

        else:
            
            print(f"Error al acceder a la página: {response.status_code}")
        
def get_nuclearPlantInfo(url, country):

    response = session.get(url)
        
    if response.status_code == 200:
            
        soup = BeautifulSoup(response.text, 'html.parser')

        ReactorStatus = soup.find('span',{"id": "MainContent_MainContent_lblReactorStatus"}).text
        ReactorName = str(soup.find('span', {'id': 'MainContent_MainContent_lblReactorName'}).text).rstrip()
        table = soup.find('table', {'class': 'layout'})

        rows = table.find_all('tr')

        final_headers=['Reactor Name', 'Reactor Status', 'Country',
                        'Reactor Type', 'Model', 'Owner', 'Operator', 
                       'Reference Unit Power (Net Capacity) [MWe]', 'Design Net Capacity [MWe]', 'Gross Capacity [MWe]', 'Thernmal Capacity [MWt]', 
                       'Construcion Start Date', 'First Criticality Date', 'Construction Suspended Date', 'Construction Restart Date',
                       'First Grid Connection', 'Commercial Operation Date', 'Suspended Operation Date', 'End of Suspended Operation Date',
                       'Permanent Shutdown Date']
        data = []

        data.append(ReactorName)
        data.append(ReactorStatus)
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

        save_json(f'src/data/{country}/{ReactorName}/{ReactorName}_data.json', cleaned_data)
            
def get_nuclearPlantAnnualData(url,country):

    response = session.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        ReactorStatus = soup.find('span',{"id": "MainContent_MainContent_lblReactorStatus"}).text
        ReactorName = str(soup.find('span', {'id': 'MainContent_MainContent_lblReactorName'}).text).rstrip()

        if ReactorStatus == "Under Construction":

            save_json(f'src/data/{country}/{str(ReactorName).lstrip()}/{str(ReactorName).lstrip()}_AnualData.json', {})
            

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

                save_json(f'src/data/{country}/{str(ReactorName).lstrip()}/{str(ReactorName).lstrip()}_AnualData.json', data_dicts)




    else:
        print(f"Error al acceder a la página: {response.status_code}")
