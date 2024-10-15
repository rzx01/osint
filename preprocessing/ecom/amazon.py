from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, parse_qs

def extract_amazon_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"
    }

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_string = title.get_text().strip().replace(',', '')
    except AttributeError:
        title_string = "NA"

    try:
        category_list = soup.find("div", attrs={"id": 'wayfinding-breadcrumbs_feature_div'})
        if category_list:
            categories = [cat.get_text().strip() for cat in category_list.find_all("a")]
            category = " > ".join(categories)
        else:
            category = "NA"
    except AttributeError:
        category = "NA"

    try:
        price = soup.find("span", attrs={"class": 'a-price-whole'}).get_text().strip().replace(',', '')
    except AttributeError:
        price = "NA"

    try:
        brand = soup.find("a", attrs={"id": 'bylineInfo'}).get_text().strip()
    except AttributeError:
        brand = "NA"

    return {
        "title": title_string,
        "category": category,
        "price": price,
        "brand": brand
    }


def extract_amazon_category(url):
    # Extracts the category from URL path or parameter
    path_parts = url.split('/')
    if len(path_parts) > 3:
        category = path_parts[3]
        return {"category": category.replace('-', ' ')}
    else:
        return {"category": "NA"}


def extract_gcx(url):
    return {"category": url.split('/')[4]}


def extract_amazon_search_query(url):
    # Extracts the search query from URL parameters
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query = query_params.get('k', ['NA'])[0]
    return {"search_query": query}


def amazon_category(url):
    if 'gp/product' in url or 'dp' in url:
        return extract_amazon_product_details(url)
    elif 'gcx/' in url:
        return extract_gcx(url)
    elif "node=" in url:
        return extract_amazon_category(url)
    elif 's?' in url:
        return extract_amazon_search_query(url)
    else:
        return {"error": "Unknown URL type"}

