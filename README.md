
# Collection and Sentiment Analysis Tool

This project automates the process of scraping product information and reviews from e-commerce websites using Selenium and performs sentiment analysis on the scraped reviews. The goal is to identify top products based on customer sentiments.

## Features

- **Web Scraping**: Extract product details, reviews, and ratings using Selenium.
- **CSV Handling**: Store scraped data into CSV files with proper formatting.
- **Sentiment Analysis**: Analyze sentiments of reviews using a pre-trained Hugging Face model.
- **Visualization**: Visualize sentiment data and identify top-performing products.

## Prerequisites

Ensure the following software is installed:
- Python 3.7+
- Google Chrome Browser
- ChromeDriver (managed via `webdriver_manager`)

Install the required Python libraries:
```bash
pip install selenium webdriver-manager pandas transformers matplotlib seaborn pyarrow
```

## Usage

1. **Scraping Data**:
   - Update `links.csv` in the `datasets/` folder with the URLs of products to scrape.
   - Run the script:
     ```bash
     python collection.py
     ```
   - Scraped data will be saved in `datasets/data_2.csv` and `datasets/reviews_2.csv`.

2. **Analyzing Sentiments**:
   - Use the provided Jupyter Notebook to clean the reviews, remove emojis, and analyze sentiments.
   - Sentiment analysis is performed using Hugging Face's pipeline.

3. **Visualizing Results**:
   - Use tools like Matplotlib and Seaborn to visualize sentiment distributions and identify top products.

## Project Structure
```
.
├── collection.py            # Main scraping script
├── datasets/                # Folder to store input/output data
│   ├── links.csv            # List of product links
│   ├── data_2.csv           # Scraped product information
│   ├── reviews_2.csv        # Scraped reviews
├── notebook.ipynb           # Jupyter Notebook for sentiment analysis
└── README.md                # Documentation
```

## Notes

- Ensure the target website's structure aligns with the XPath expressions in `collection.py`. Update XPaths if the website changes.
- Adhere to the website's Terms of Service and scraping policies.

## Contributors
- Santhosh Kannan S P ([GitHub](https://github.com/SanthoshKannanSP))
- Bagiya Lakshmi ([GitHub](https://github.com/bagiyalakshmi))
