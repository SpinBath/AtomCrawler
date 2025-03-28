# AtomCrawler

![ATOMCRAWLER-LOGO](https://github.com/XRayBinary/assets/blob/main/AtomCrawler.png)

## About the project

> [!IMPORTANT]  
> Under Development.

AtomCrawler is an application that collects data from different nuclear reactors worldwide, generates new data based on the information already gathered, and conducts analyses to present the processed information through graphs and files.

<hr>

## Overview

![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/images/atomcrawler_map.png)

### 1. Data Collection

The data for each nuclear power plant is gathered through web scraping from the website of the Power Reactor Information System (PRIS), which belongs to the International Atomic Energy Agency (IAEA). 

**IAEA | PRIS : https://pris.iaea.org/PRIS/home.aspx**

The type of scraping used is for Static Data, as PRIS currently does not provide any public API for querying its database.

Technologies:<br>
 - **BeautifulSoup** (*beautifulsoup4 == 4.13.3*)

![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_status.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_country.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_types.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_energyefficiency.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_thermalefficiency.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_gross.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_hours.png)



