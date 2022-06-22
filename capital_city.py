from bs4 import BeautifulSoup 
import requests 



def start():

    print("Please selection the options below: Enter 1 to find a country national capital. Enter Option 2 to find a state capital (Only works for Australia). Enter 'q' to quit. ")

    user_choice = input()

    if user_choice == 'q':
        exit(0)

    if int(user_choice) == 1:
        country()


    elif int(user_choice) == 2:
        state()
        
def country():


        print("Data not guaranteed to be accurate, as it's sourced from third party-source.")

        dest = input("Please Enter Your Country: ").strip().lower()

        dest_found = False

        city_countries = []

        URL = 'https://geographyfieldwork.com/WorldCapitalCities.htm'

        req = requests.get(URL)

        req_content = req.text

        soup = BeautifulSoup(req_content, 'html.parser')
            
        '''Let's find the table classes within the page and the table that we specifcally want'''

        for collection_tables in soup.find_all('table'):
            #print(collection_tables.get('class'))
            pass

        # This prints out the class names. We can see from this that we need the wikitable sortable class and the rest are irrelevant to our project.

        table = soup.find('table', class_='sortable')

        for country in table.find_all('td'):
            city_countries.append(country.text)
        
        city_countries = city_countries[:-2] # This removes the last two values that occur due to nature of website and are not needed. 


        for i in range(len(city_countries)):
            if str(city_countries[i]).lower() == dest:
                print("The capital city of", dest, "is", city_countries[i + 1])
                dest_found = True
            
        if dest_found == False:
            print("Sorry. :( You have either not entered a valid country or the website is missing data.")
        
        start()


def state():

        print("Data not guaranteed to be accurate, as it's sourced from third party-source.")
        
        dest = input("Please Enter Your Australian State: ").strip().lower()

        if dest == 'victoria':
            dest = dest + ' ' + '(australia)' # Had to do do this because of Wikipedia's inconsistent formatting.

        dest_found = False

        states_city = []

        URL = 'https://en.wikipedia.org/wiki/List_of_Australian_capital_cities'

        req = requests.get(URL)

        req_content = req.text

        soup  = BeautifulSoup(req_content,'html.parser')

        table = soup.find('table', class_ = 'wikitable sortable')

        for states in table.find_all('a'):

            if (states.get('title')) != None:
                states_city.append(states.get('title'))
            
        for i in range(len(states_city)):

            if str(states_city[i]).lower() == dest:
                print("The captial city for", dest, "is", states_city[i + 1])
                dest_found = True
        

        if dest_found == False:
            print("Sorry. You have entered a wrong State (Check Spelling)")
        
        start()


if __name__ == "__main__":

    start()

