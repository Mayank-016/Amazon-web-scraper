import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_product_listings(pages=20):
    base_url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    all_products = []
    for page in range(1, pages + 1):
        url = base_url + str(page)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        products = soup.find_all("div", {"data-component-type": "s-search-result"})

        for product in products:
            product_url = "https://www.amazon.in" + product.find("a", {"class": "a-link-normal"})["href"]
            product_name = product.find("span", {"class": "a-size-medium"}).text.strip()
            product_price = product.find("span", {"class": "a-price"}).find("span", {"class": "a-offscreen"}).text.strip()
            product_rating = product.find("span", {"class": "a-icon-alt"}).text.split()[0]
            num_reviews = product.find("span", {"class": "a-size-base"}).text.strip()

            # Fetch the product page and get the URL from the "Share" section
            share_response = requests.get(product_url, headers=headers)
            share_soup = BeautifulSoup(share_response.content, "html.parser")
            share_section = share_soup.find("div", {"id": "wl-share-section"})
            share_url = share_section.find("input", {"id": "wl-share-text-box"}).get("value") if share_section else None

            product_data = {
                "Product URL": product_url,
                "Share URL": share_url,  # Add the share URL to the data
                "Product Name": product_name,
                "Product Price": product_price,
                "Rating": product_rating,
                "Number of Reviews": num_reviews
            }
            all_products.append(product_data)

    return all_products

if __name__ == "__main__":
    num_pages_to_scrape = 20
    product_listings = scrape_product_listings(pages=num_pages_to_scrape)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(product_listings)

    # Save the data to a CSV file
    df.to_csv("amazon_product_listings.csv", index=False)
