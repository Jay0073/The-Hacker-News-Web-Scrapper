import requests
from bs4 import BeautifulSoup

# Function to request and parse HTML content from The Hacker News website
def requestSoup():
    # Send a GET request to the website
    r = requests.get('https://thehackernews.com/')
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Return the parsed HTML content
    return soup
