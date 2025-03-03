import os
from src.scraping import get_countries, get_nuclearPlant

logo = ('''
            ┏┓      ┏┓       ┓    
            ┣┫╋┏┓┏┳┓┃ ┏┓┏┓┓┏┏┃┏┓┏┓
            ┛┗┗┗┛┛┗┗┗┛┛ ┗┻┗┻┛┗┗ ┛ 
          ''')

def scraping_menu():

    print(f''' {logo} 
          
    Choose an option (1-5):       
          
        1. Get Countries URLs
        2. Get Nuclear Plant Data
        3. Get Nuclear Plant General Data
        4. Get Nuclear Plant Annual Data
        5. <-- 
        6. Exit''')

    while True:
        option = input(">> ")

        if option == "1":
            get_countries()
        elif option == "2":
            get_nuclearPlant()
        elif option == "3":
            exit()
        elif option == "4":
            exit()
        elif option == "5":
            main()
        elif option == "6":
            os.system('cls')
            exit()

def analysis_menu():

    print(f''' {logo} 
          
    Choose an option (1-3):       
          
        1. Get Countries URLs
        2. Get Nuclear Plant General Data
        3. Get Nuclear Plant Annual Data
        4. <--
        5. Exit ''')

    while True:
        option = input(">> ")

        if option == "1":
            get_countries()
        elif option == "4":
            main()
        elif option == "5":
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

