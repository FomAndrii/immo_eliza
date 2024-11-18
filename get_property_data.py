# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
from PropertyDataScraper import PropertyDataScraper

start_time = time.perf_counter()

def get_cookie(url):
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url) 
    time.sleep(5)

    shadow_host = driver.find_element(By.ID, 'usercentrics-root')
    shadow_root = shadow_host.shadow_root
    elem = shadow_root.find_element(By.CSS_SELECTOR, "button[data-testid='uc-accept-all-button']")
    elem.click()

    cookies = driver.get_cookies()
    driver.quit()
    return cookies

# Function to set cookies for the session
def set_cookie(url,session):
    cookies = get_cookie(url)
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale"
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36', #mimics browser
}
set_cookie(url,session)

# Script to collect data from the links stored in a file
with open("subset_100properties.txt", "r") as file:
    property_urls = [line.strip() for line in file]

with open("PropertyData.csv", "w") as outfile:
    for url in property_urls:
        response = session.get(url, headers=headers)

        if response.status_code != 200:
            set_cookie(url,session)
            response = session.get(url, headers=headers)

        html = response.content
        soup = BeautifulSoup(response.content, 'html.parser')

        property_data = PropertyDataScraper(soup)
        outfile.write(property_data.return_data())
        outfile.write("\n")

print(f"\nTime taken to scrape {time.perf_counter() - start_time} seconds.") 