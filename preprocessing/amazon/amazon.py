import csv
from bs4 import BeautifulSoup
import requests


url = 'https://www.amazon.in/Inovera-Label-Women-Handbags-Shoulder/dp/B08CMQD4BC/ref=sr_1_2?dib=eyJ2IjoiMSJ9.3WkjJ8VAZd9UTTYtmWRd4WDWRAOQyI7PjfzVPo2MJa91PCSawDLCTHzOkCDUCxSpbpV3-L1tNes9mi92CtopVJBMyXBfW3jQwz83cMH44mJCZU6DDMweziaeV7RQ9x_fJK3hVTyv5VFE38IxqLYj3Xp_m-6r8FTBXqMDhFUJYJq-ngqozUUbt7MEtkO8CGOIgw3nzgDaFrta2ZKQQdSgTjBtFuQAYHjw41iD29G4hh4EnDX97fy-KnGrCIPx9xr1HJuvYwdj3DTkuXJSq5i8c7R-bdlhm18sPjKF6gF4G9A.zj7hKGyen7d2a_IS-CJIcenePPvfTPLZjDyf_MEKcDE&dib_tag=se&keywords=totes&pf_rd_i=1983338031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=c7e8e914-873a-4174-87af-ba314653bb89&pf_rd_r=990TGCJKRQZP21WMY1NW&pf_rd_s=merchandised-search-16&qid=1725277129&refinements=p_n_feature_nineteen_browse-bin%3A11301363031&rnid=11301362031&s=shoes&sr=1-2&th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"
}

#making the request to the URL
page = requests.get(url, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#open csv file for appending data
with open("amazon.csv", "a", newline='', encoding='utf-8') as File:
    writer = csv.writer(File)

    #retrieving product title
    try:
        title = soup2.find("span", attrs={"id": 'productTitle'})
        title_string = title.get_text().strip().replace(',', '')  #clean the title string
    except AttributeError:
        title_string = "NA"
    print("Product Title = ", title_string)

    #retrieving the product's category from the 'img' tag
    try:
        category_img = soup2.find("img", attrs={"class": 'nav-categ-image'})
        category = category_img.get("alt").strip()  #extracting the 'alt' attribute as the category
    except AttributeError:
        category = "NA"
    print("Product Category = ", category)

    #retrieving the product's price
    try:
        price = soup2.find("span", attrs={"class": 'a-price-whole'}).get_text().strip().replace(',', '')  # Clean the price
    except AttributeError:
        price = "NA"
    print("Product Price = ", price)

    #retrieving the product brand name
    try:
        brand = soup2.find("a", attrs={"id": 'bylineInfo'}).get_text().strip()
    except AttributeError:
        brand = "NA"
    print("Product Brand Name = ", brand)

    #write to csv: product title, category, price, and brand name
    writer.writerow([title_string, category, price, brand])


#csv file is automatically closed with the 'with' statement


