import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://example.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract and print specific information from the page
    title = soup.title.string
    print(f'Title: {title}')
else:
    print('Failed to fetch the page.')
