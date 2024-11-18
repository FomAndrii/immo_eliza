from bs4 import BeautifulSoup
import json

class PropertyDataScraper:
    
    def __init__(self, soup):
        self.soup = soup
        self.house_dict = self.extract_house_dict()
       
        # Attributes of the property
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
        self.terrace = self.terrace()
        self.terrace_area = self.terrace_area()
        self.garden = self.garden()
        self.garden_area = self.garden_area()
        self.land = self.land()
        self.num_facade = self.num_facade()
        self.pool = self.pool()
        self.state = self.state()

    def extract_house_dict(self):
        '''
        Extracts and returns the data of the property from the page's script.
        '''
        result_set = self.soup.find_all('script')
        for each in result_set:
            try:
                if 'window.classified' in each.string:
                    #print("Reached the data")
                    house_data = each.text.strip()[20:-1]
                    full_data = json.loads(house_data)
                    return full_data
            except:
                pass

    def type_property(self):
        try:
            return self.house_dict['property']['type']
        except:
            return 'None'

    def locality(self):
        try:
            return self.house_dict['property']['location']['postalCode']
        except:
            return 'None'

    def subtype(self):
        try:
            return self.house_dict['property']['subtype']
        except:
            return 'None'

    def price(self):
        try:
            return int(self.house_dict['transaction']['sale']['price'])
        except:
            return 'None'

    def type_sale(self):
        try:
            if self.house_dict['flags']['isPublicSale']:
                return 'Public Sale'
            elif self.house_dict['flags']['isNewClassified']:
                return 'New classified'
            elif self.house_dict['flags']['isNotarySale']:
                return 'Notary Sale'
            elif self.house_dict['flags']['isAnInteractiveSale']:
                return 'Interactive Sale'
            elif self.house_dict['flags']['isNewPrice']:
                return 'New Price'
            else:
                return 'None'
        except:
            return 'None'

    def num_rooms(self):
        try:
            return int(self.house_dict['property']['bedroomCount'])
        except:
            return 'None'

    def area(self):
        try:
            return int(self.house_dict['property']['netHabitableSurface'])
        except:
            return 'None'

    def kitchen(self):
        try:
            return 1 if self.house_dict['property']['kitchen']['type'] else 0
        except:
            return 'None'

    def furnished(self):
        try:
            return 1 if self.house_dict['transaction']['sale']['isFurnished'] else 0
        except:
            return 'None'

    def fire(self):
        try:
            return 1 if self.house_dict['property']['fireplaceExists'] else 0
        except:
            return 'None'

    def terrace(self):
        try:
            return 1 if self.house_dict['property']['hasTerrace'] else 0
        except:
            return 'None'

    def terrace_area(self):
        try:
            return int(self.house_dict['property']['terraceSurface']) if self.house_dict['property']['terraceSurface'] else 'None'
        except:
            return 'None'
        
    def garden(self):
        try:
            return 1 if self.house_dict['property']['hasGarden'] else 0
        except:
            return 'None'

    def garden_area(self):
        try:
            return int(self.house_dict['property']['gardenSurface']) if self.house_dict['property']['gardenSurface'] else 'None'
        except:
            return 'None'

    def land(self):
        try:
            return int(self.house_dict['property']['land']['surface']) if self.house_dict['property']['land'] else 0
        except:
            return 'None'

    def num_facade(self):
        try:
            return int(self.house_dict['property']['building']['facadeCount']) if self.house_dict['property']['building']['facadeCount'] else 'None'
        except:
            return 'None'

    def pool(self):
        try:
            return 1 if self.house_dict['property']['hasSwimmingPool'] else 0
        except:
            return 'None'

    def state(self):
        try:
            return self.house_dict['property']['building']['condition'] if self.house_dict['property']['building']['condition'] else 'None'
        except:
            return 'None'
        
    def return_data(self):
        to_print = [self.type_property,self.locality,self.subtype,self.price,self.type_sale,self.num_rooms,self.area,self.kitchen,self.furnished,self.fire,self.terrace,self.terrace_area,self.garden,self.garden_area,self.land,self.num_facade,self.pool,self.state]
        return ','.join(str(element) for element in to_print)       