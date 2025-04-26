from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import certifi
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")  # Run without opening browser
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://ecsc.gov.sy/home")

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.find_all('a'))
driver.quit()


# --------------------------------------------------------------------------------------------------------------------------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://ecsc.gov.sy/',
    'Connection': 'keep-alive'
}

response = requests.get('https://ecsc.gov.sy/home', headers=headers, verify='/home/abo_alzeek/ecsc_ca_bundle.pem')

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find_all('a'))
