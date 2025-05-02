import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.geeksforgeeks.org/python-web-scraping-tutorial/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract titles (assuming they're in <h2> tags)
titles = soup.find_all('h2')

# Print the titles
for title in titles:
    print(title.get_text())
