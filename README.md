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

**Technologies used:**  
`beautifulsoup4 == 4.13.3`

### 1. Sanitization  
Data sanitization processes are applied to the collected data:  
- Correction of erroneous data  
- Standardization of formats  
- Handling of missing values  

### 1. Retrieve More Data  
Once the data is cleaned, a process is carried out to generate additional data based on the existing ones (Thermal Efficiency [%], Hours On Line, Total Power Supplied [TW.h], etc.).  

**Technologies used:**  
 `pandas == 2.2.3`  

### 1. Processing  
Data stored in JSON files is processed to generate graphs for visualizations (Top Countries by Reactor Count, Nuclear Plant Status, etc.)

These processed data are also stored in different formats, such as **XML** files for web services (SOAP, REST) and **CSV** for presentation in spreadsheet applications (Microsoft Excel, Google Sheets, LibreOffice Calc).  

**Technologies used:**  
 `pandas == 2.2.3`  
 `matplotlib == 3.10.1` 