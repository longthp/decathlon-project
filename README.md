# Decathlon Data Analysis Project
![logo](assets/decathlon_logo.svg)

# Project's Overview
1. <ins>Web Scraping</ins>
    * Created a [scraper](scraper/) package/directory to collect data from Decathlon's online store
2. Exploratory Data Analysis
    * EDA using the collected data from above

# Project's Description
## 1. Web Scraping
### <ins>Tasks</ins>
* Scrape product data for mens, womens, kids, and babies categories.

### <ins>Problems</ins>
* The site was too complex, with 10k plus of products, making it even harder to navigate through all categories and pages from the frontend.
    * The approach was to use the sitemap of the website and loop through every product links to extract the data that we want.

* But still, there were way too many urls. Waiting for each response to comeback and parse the reponse object respectively is resource heavy.
    * The approach here was to use asynchrous code, waiting for all of the reponses, and then execute the parsing part.

### <ins>Solution</ins>
* Decathlon's online store is based on Shopify service, which means I could add the .js or .json to the end of every products url to retreive all the JSON data of the corresponding products.
    * For example: https://www.decathlon.com/products/mens-hiking-pants-nh100-308281.json
    * 
* 
* To handle the complexity of navigating through categories,


### <ins>Output</ins>


## 2. Exploratory Data Analysis
