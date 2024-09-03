import requests
from bs4 import BeautifulSoup
import re

url = "https://www.webtoons.com/en/thriller/replaced/episode-15/viewer?title_no=6507&episode_no=15" 

#i couldve done the main page url with regex too but :sob: i wanted to feel like i actually scraped webtoon 
def webtoon_identifier(url):
    return url.rstrip('/').split('/')[-1]

def fetch_webtoon_main_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        webtoon_name_tag = soup.find('h1', class_='subj')
        webtoon_name = webtoon_name_tag.text.strip() if webtoon_name_tag else 'N/A'
        
        genre_tag = soup.find('h2', class_='genre')
        genre = genre_tag.text.strip() if genre_tag else 'N/A'

        print(f"name: {webtoon_name}")
        print(f"genre: {genre}")
    else:
        print(f"Failed to fetch main page. Status code: {response.status_code}")

def fetch_webtoon_episode(url):
    pattern = r'https://www\.webtoons\.com/en/([^/]+)/([^/]+)/.*\?title_no=\d+&episode_no=(\d+)'
    
    match = re.search(pattern, url)
    
    if match:
        genre = match.group(1)
        webtoon_name = match.group(2).replace('-', ' ').title()
        episode_no = match.group(3)

        print(f"name: {webtoon_name}")
        print(f"genre: {genre}")
        print(f"ep_no: {episode_no}")
    else:
        print("No match found.")

if "/list?" in url:
    #main page of comic url
    fetch_webtoon_main_page(url)
else:
    #episode page url
    fetch_webtoon_episode(url)