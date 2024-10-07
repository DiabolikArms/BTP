# Analysis of Bias in User Engagement on Indian News Media (TOI)

## Overview

This project investigates user engagement bias within the Indian news media, specifically focusing on The Times of India (TOI). As media consumption significantly impacts public opinion, this analysis aims to identify patterns in user interactions that align with specific political, social, or communal ideologies. By understanding these trends, we aspire to promote media literacy and accountability, contributing to a more balanced media landscape in India.

## Features

- Systematic web crawling and data scraping of TOI articles and user comments.
- Analysis of user engagement patterns to identify potential biases.
- Scalable data processing through parallel execution and chunked scraping.

## Technologies Used

- **Selenium**: For automating browser interactions and handling dynamic web content.
- **Scrapy**: For efficient web scraping and data extraction.
- **Jupyter Notebook**: For exploratory data analysis and prototyping.
- **Python**: The primary programming language used for development.
- **Pickle**: For data storage and serialization.

## Data Collection

The data collection process involved:

1. **Category Links Extraction**: Extracting links to various categories on the TOI homepage.
2. **Article Links Collection**: Gathering article links from different categories, resulting in a total of 27,108 articles.
3. **Data Crawling**: Extracting relevant data from each article, including user comments and engagement metrics.

## Execution

To run the scripts, ensure you have the required dependencies installed. You can execute the scripts by running the main Python file or individual Jupyter Notebooks for specific tasks.

### Prerequisites

- Python 3.x
- Required libraries (install via `pip install -r requirements.txt`)

## References

1. [Research Paper on Selenium Webdriver UI Automation](https://www.researchgate.net/publication/276437851_Analysis_and_Design_of_Selenium_WebDriver_Automation_Testing_Framework)
2. [Guru99 - Selenium Tutorial](https://www.guru99.com/selenium-tutorial.html)
3. [Scrapy Course - Python Web Scraping for Beginners](https://www.youtube.com/watch?v=mBoX_JCKZTE)
4. [XPath in Selenium](https://www.youtube.com/watch?v=9-iVt0MIqNY)
