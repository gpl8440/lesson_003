import requests
from bs4 import BeautifulSoup

DOLLAR_RUBLE = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80&aqs=chrome.0.0i131i433i512j69i57j0i131i433i512l3j0i512l3j0i131i433i512j0i131i433.4146j1j7&sourceid=chrome&ie=UTF-8'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
full_page = requests.get(DOLLAR_RUBLE, headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision":2})
print(convert)
оаоалала