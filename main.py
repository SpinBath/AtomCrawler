import os
from src.scraping import get_Urls, get_nuclearPlantInfo, get_nuclearPlantAnnualData, sanitize_Data, sanitize_AnnualData
from src.analysis import Data, Graph, converter_method


logo = ('''
            ┏┓      ┏┓       ┓    
            ┣┫╋┏┓┏┳┓┃ ┏┓┏┓┓┏┏┃┏┓┏┓
            ┛┗┗┗┛┛┗┗┗┛┛ ┗┻┗┻┛┗┗ ┛ 
          ''')

def scraping_menu():

    print(f''' {logo} 
          
    Choose an option (1-6):       
          
        1. Get Countries and Nuclear Plant URLs
        2. Get Nuclear Plant Data (General)
        3. Get Nuclear Plant Data (Annual)
        4. Get Nuclear Plant Data (All)
        5. Sanitize Data
        6. <-- 
        7. Exit''')

    while True:
        option = input(">> ")

        if option == "1":
            get_Urls()
        elif option == "2":
            get_nuclearPlantInfo()
        elif option == "3":
            get_nuclearPlantAnnualData()
        elif option == "4":
            get_nuclearPlantInfo()
            get_nuclearPlantAnnualData()
        elif option == "5":
            sanitize_Data()
            sanitize_AnnualData()
        elif option == "6":
            main()
        elif option == "7":
            os.system('cls')
            exit()

def analysis_menu():

    print(f''' {logo} 
          
    Choose an option (1-3):       
          
        1. Retrieve More Data
        2. Generate Graphs
        3. Generate Docs
        4. Run all analizer
        5. <-- 
        6. Exit ''')

    while True:
        option = input(">> ")

        if option == "1":
            Data()
        elif option == "2":
            Graph()
        elif option == "3":
            converter_method()
        elif option == "4":
            Data()
            Graph()
            converter_method()
        elif option == "5":
            main()
        elif option == "6":
            os.system('cls')
            exit()

def main():
    
    os.system('cls')

    print(f''' {logo} 
          
    Choose an option (1-3):       
          
        1. Scrapping
        2. Analysis
        3. Exit ''')

    while True:
        option = input(">> ")

        if option == "1":
            os.system('cls')
            scraping_menu()
            
        elif option == "2":
            os.system('cls')
            analysis_menu()

        elif option == "3":
            os.system('cls')
            exit()


if __name__ == "__main__":
    main()

