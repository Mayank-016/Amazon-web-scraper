# Amazon-web-scraper
The above code consists of two main parts. The first part scrapes product listings from Amazon.in for bags and saves the data in a CSV file. The second part enriches the product listings data with additional details such as ASIN, product description, and manufacturer, and then saves the enriched data in another CSV file.


## Installation

To use this code, you need to have Python installed on your machine. Additionally, install the required libraries using pip:
```
pip install pandas
pip install requests
pip install beautifulsoup4
```

Usage Instructions: Provide a step-by-step guide on how to use the code. Describe the purpose of each Python file and how they interact with each other.


## Usage

1. To scrape product listings from Amazon, run the following command:
   ```
   python Part1.py
   ```

   This will generate a CSV file named "amazon_product_listings.csv" containing product details such as name, price, rating, and number of reviews.

2. To enrich the product listings with additional details (ASIN, product description, and manufacturer) from Amazon, run the following command:
   ```
   python Part2.py
   ```

   This will create a new CSV file named "amazon_product_listings_with_details.csv" that includes the additional details.

3. (Optional) To run the entire process in a single step, run the following command:
   ```
   python run_all.py
   ```
   This will execute both Part1.py and Part2.py in sequence.


