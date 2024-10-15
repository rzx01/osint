import requests
from bs4 import BeautifulSoup


def extract_prime_details(url):

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: Status code {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')

    details = {
        "name": soup.find("h1", {"class": "p-jAFk Qo+b2C"}).text.strip() if soup.find("h1", {
            "class": "p-jAFk Qo+b2C"}) else "N/A",
        "about": soup.find("span", {"class": "_1H6ABQ"}).text.strip() if soup.find("span",
                                                                                   {"class": "_1H6ABQ"}) else "N/A",
        "genre": soup.find("div", {"class": "I0iH2G"}).text.strip() if soup.find("div", {"class": "I0iH2G"}) else "N/A"
    }

    return details


def prime_category(url):
    return extract_prime_details(url)
