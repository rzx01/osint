import requests
from bs4 import BeautifulSoup
import pandas as pd

# Making a standard GET request
target_url = "https://www.primevideo.com/detail/0GYBG93YHMUUIIW4MN36BFKXAP/ref=atv_hm_hom_c_wD4dwb_brws_1_1?jic=8%7CEgRzdm9k"
resp = requests.get(target_url)
print(resp.status_code)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(resp.text, 'html.parser')

# Initialize an empty list to store the scraped data
arr = []

# Extract information and handle potential NoneType errors
try:
    name = soup.find("h1", {"class": "p-jAFk Qo+b2C"}).text.strip() if soup.find("h1", {"class": "p-jAFk Qo+b2C"}) else "N/A"
except AttributeError:
    name = "N/A"

# try:
#     seasons = soup.find("span", {"class": "_36qUej"}).text.strip() if soup.find("span", {"class": "_36qUej"}) else "N/A"
# except AttributeError:
#     seasons = "N/A"

try:
    about = soup.find("span", {"class": "_1H6ABQ"}).text.strip() if soup.find("span", {"class": "_1H6ABQ"}) else "N/A"
except AttributeError:
    about = "N/A"

try:
    genre = soup.find("div", {"class": "I0iH2G"}).text.strip() if soup.find("div", {"class": "I0iH2G"}) else "N/A"
except AttributeError:
    genre = "N/A"

# Create a dictionary to hold the scraped data
obj = {
    "name": name,
    # "seasons": seasons,
    "about": about,
    "genre": genre
}

# Append the data to the list
arr.append(obj)

# Convert the list to a DataFrame
df = pd.DataFrame(arr)

# Save the DataFrame to a CSV file
df.to_csv('amazonprime.csv', index=False, encoding='utf-8')

print("Scraping completed and data saved to 'amazonprime.csv'.")
