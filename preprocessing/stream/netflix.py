import requests
from bs4 import BeautifulSoup

def extract_netflix_details(url):
    # Check if the URL is a browsing page
    if "browse" in url and "jbv=" not in url:
        return {"browsing": True}

    # Making the GET request
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: Status code {response.status_code}")

    # Extract information using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting basic information
    details = {
        "name": soup.find("h1", {"class": "title-title"}).text.strip() if soup.find("h1", {"class": "title-title"}) else "NA",
        "seasons": soup.find("span", {"class": "duration"}).text.strip() if soup.find("span", {"class": "duration"}) else "NA",
        "about": soup.find("div", {"class": "hook-text"}).text.strip() if soup.find("div", {"class": "hook-text"}) else "NA",
        "genre": soup.find("span", {"class": "item-genres"}).text.strip() if soup.find("span", {"class": "item-genres"}) else "NA",
        "total_episodes": "NA"  # Default value
    }

    # Extracting episodes count
    episodes = soup.find("ol", {"class": "episodes-container"})
    if episodes:
        # Count the number of episodes
        episode_count = len(episodes.find_all("li"))
        details["total_episodes"] = episode_count

    return details

def netflix_category(url):
    return extract_netflix_details(url)
