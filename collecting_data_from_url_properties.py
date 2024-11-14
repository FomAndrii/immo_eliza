import requests

# Define the HouseApartmentScraping class
class HouseApartmentScraping:
    '''
    Define a class through which properties' data will be scraped.

    Each URL represents a property (house or apartment), 
    each of which has a number of attributes (e.g., locality, type_property, etc.). 
    We thus create a class defining the attributes of each property.

    :param url: URL of the property.
    :param html: HTML content of the URL.
    :param soup: BeautifulSoup object for parsing the HTML.
    :param house_dict: Dictionary with data of the property.
    '''    
    
    def __init__(self, url):
        self.url = url
        
# Fetch page with headers
        response = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            print(f"Failed to fetch {self.url}: Status code {response.status_code}")
            self.house_dict = None
            return

        # Attributes to obtain HTML content (self.html) and parse it with BeautifulSoup (self.soup)
        self.html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.html, 'html.parser')
        
        # Attribute that holds data extracted into a dictionary format
        self.house_dict = self.extract_house_dict()
        
        # Set of attributes collected in the dictionary
        self.type_property = self.type_property()
        self.locality = self.locality()
        self.subtype = self.subtype()
        self.price = self.price()
        self.type_sale = self.type_sale()
        self.num_rooms = self.num_rooms()
        self.area = self.area()
        self.kitchen = self.kitchen()
        self.furnished = self.furnished()
        self.fire = self.fire()
        self.terrace_area = self.terrace_area()
        self.garden_area = self.garden_area()
        self.land = self.land()
        self.num_facade = self.num_facade()
        self.pool = self.pool()
        self.state = self.state()
        
    def extract_house_dict(self):
        '''
        Extracts and returns a dictionary with house data from the page's script.
        '''
        try:
            result_set = self.soup.find_all('script', attrs={"type": "text/javascript"})
            for tag in result_set:
                if 'window.classified' in str(tag.string):
                    window_classified = tag
                    break
            
            wcs = window_classified.string.strip()
            wcs = wcs[wcs.find("{"):wcs.rfind("}") + 1]
            house_dict = json.loads(wcs)
            return house_dict
        except:
            return None

    def type_property(self):
        try:
            return self.house_dict['property']['type']
        except:
            return None

    def locality(self):
        try:
            return self.house_dict['property']['location']['postalCode']
        except:
            return None

    def subtype(self):
        try:
            return self.house_dict['property']['subtype']
        except:
            return None

    def price(self):
        try:
            return int(self.house_dict['transaction']['sale']['price'])
        except:
            return None

    def type_sale(self):
        try:
            if self.house_dict['flags']['isPublicSale']:
                return 'Public Sale'
            elif self.house_dict['flags']['isNotarySale']:
                return 'Notary Sale'
            elif self.house_dict['flags']['isAnInteractiveSale']:
                return 'Interactive Sale'
            else:
                return None
        except:
            return None

    def num_rooms(self):
        try:
            return int(self.house_dict['property']['bedroomCount'])
        except:
            return None

    def area(self):
        try:
            return int(self.house_dict['property']['netHabitableSurface'])
        except:
            return None

    def kitchen(self):
        try:
            kitchen_type = self.house_dict['property']['kitchen']['type']
            return 1 if kitchen_type else 0
        except:
            return None

    def furnished(self):
        try:
            return 1 if self.house_dict['transaction']['sale']['isFurnished'] else 0
        except:
            return None

    def fire(self):
        try:
            return 1 if self.house_dict['property']['fireplaceExists'] else 0
        except:
            return None

    def terrace_area(self):
        try:
            if self.house_dict['property']['hasTerrace']:
                return int(self.house_dict['property']['terraceSurface'])
            return 0
        except:
            return None

    def garden_area(self):
        try:
            if self.house_dict['property']['hasGarden']:
                return int(self.house_dict['property']['gardenSurface'])
            return 0
        except:
            return None

    def land(self):
        try:
            return int(self.house_dict['property']['land']['surface']) if self.house_dict['property']['land'] else 0
        except:
            return None

    def num_facade(self):
        try:
            return int(self.house_dict['property']['building']['facadeCount'])
        except:
            return None

    def pool(self):
        try:
            return 1 if 'swimming pool' in str(self.html).lower() else 0
        except:
            return None

    def state(self):
        try:
            return self.house_dict['property']['building']['condition']
        except:
            return None
