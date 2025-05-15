# AtomCrawler

![ATOMCRAWLER-LOGO](https://github.com/SpinBath/assets/blob/main/AtomCrawler-Logo.png)

## About the project

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

### 2. Sanitization  
Data sanitization processes are applied to the collected data:  
- Correction of erroneous data  
- Standardization of formats  
- Handling of missing values  

### 3. Retrieve More Data  
Once the data is cleaned, a process is carried out to generate additional data based on the existing ones (Thermal Efficiency [%], Hours On Line, Total Power Supplied [TW.h], etc.).  

**Technologies used:**  
 `pandas == 2.2.3`  

### 4. Processing  
Data stored in JSON files is processed to generate graphs for visualizations (Top Countries by Reactor Count, Nuclear Plant Status, etc.)

These processed data are also stored in different formats, such as **XML** files for web services (SOAP, REST) and **CSV** for presentation in spreadsheet applications (Microsoft Excel, Google Sheets, LibreOffice Calc).  

**Technologies used:**  
 `pandas == 2.2.3`  
 `matplotlib == 3.10.1` 

![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/images/data.png)
![ATOMCRAWLER-graph](https://github.com/XRayBinary/AtomCrawler/blob/main/images/data2.png)

<hr>

<details>
   <summary><h2>Gallery</h2></summary>

  <details>
    <summary><h3>Graphs</h3></summary>

  ![AtomCrawler-Graph](https://github.com/SpinBath/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_country.png)    
  ![AtomCrawler-Graph](https://github.com/SpinBath/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_gross.png)
  ![AtomCrawler-Graph](https://github.com/SpinBath/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_status.png)
  ![AtomCrawler-Graph](https://github.com/SpinBath/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_thermalefficiency.png)
  ![AtomCrawler-Graph](https://github.com/SpinBath/AtomCrawler/blob/main/data/analized_data/graphs/nuclear_plants_hours.png)   

  </details>
</details>

<hr>

## How to Setup

To set up this project on your local machine, follow these steps:

### Prerequisites

Before starting, ensure that you have the following installed:

- Python 3.x (Recommended: 3.7+)
- pip (Python package installer)

You can download Python from [here](https://www.python.org/downloads/).

### 1. Clone the Repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/XRayBinary/AtomCrawler.git
cd AtomCrawler
```

### 2. Create a Virtual Environment (Optional but Recommended)
It’s a good practice to create a virtual environment to isolate the dependencies for your project. To create a virtual environment, use the following commands:


```bash
python3 -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
.\venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install the dependencies

With the virtual environment activated, install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```
### 4. Iniciar el Proyecto

To run the main.py file, make sure you're in the directory where the file is located and then execute the following command:

```bash
python3 main.py
```
