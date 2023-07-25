import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

# Rest of the code remains unchanged.


def get_product_details(url, max_retries=3):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise exception for 4xx and 5xx status codes
            break
        except (requests.RequestException, requests.ConnectionError, requests.Timeout) as e:
            print(f"Request failed: {e}")
            retries += 1
            print(f"Retrying... Attempt {retries}")
            time.sleep(2 * retries)  # Wait before retrying

    if retries >= max_retries:
        print(f"Failed to fetch data for URL: {url}")
        return None, None, None

    soup = BeautifulSoup(response.content, "html.parser")

    asin_elem = soup.find("span", string="ASIN")
    asin = asin_elem.find_next("span").text.strip() if asin_elem else None

    manufacturer_elem = soup.find("span", string="Manufacturer")
    manufacturer = manufacturer_elem.find_next("span").text.strip() if manufacturer_elem else None

    product_desc_elem = soup.find("div", {"id": "productDescription"})
    product_desc = product_desc_elem.text.strip() if product_desc_elem else None

    return asin, product_desc, manufacturer


# ... (The rest of the code remains unchanged)

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time

# Rest of the code remains unchanged.

def update_csv_with_product_details(input_file, output_file):
    df = pd.read_csv(input_file)

    asin_list, product_desc_list, manufacturer_list = [], [], []
    for url in df['Product URL']:
        print(f"Processing URL: {url}")
        asin, product_desc, manufacturer = get_product_details(url)
        print("ASIN:", asin)
        print("Product Description:", product_desc)
        print("Manufacturer:", manufacturer)

        asin_list.append(asin)
        product_desc_list.append(product_desc)
        manufacturer_list.append(manufacturer)

    df['ASIN'] = asin_list
    df['Product Description'] = product_desc_list
    df['Manufacturer'] = manufacturer_list

    df.to_csv(output_file, index=False)

# ... (Rest of the code remains unchanged)



# ... (Rest of the code remains unchanged)


if __name__ == "__main__":
    input_csv_file = "amazon_product_listings.csv"
    output_csv_file = "amazon_product_listings_with_details.csv"

    update_csv_with_product_details(input_csv_file, output_csv_file)
