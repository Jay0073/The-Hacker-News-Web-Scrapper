# The Hacker News Scraper Gui

This project is a Python-based web scraper that extracts the latest news articles from the Hacker News website and displays them in a user-friendly graphical interface. It utilizes the requests library to fetch web content and BeautifulSoup for parsing HTML. The GUI is built using customtkinter, making it easy to navigate and read the news directly from the application.

# Features
- Fetches the latest news articles from Hacker News.

- Displays news titles, descriptions, tags, and publication dates.

- Provides clickable links to the full articles.

- User-friendly dark mode interface.

# Installation

1. **Clone the Repository:**

```python
git clone https://github.com/Jay0073/The-Hacker-News-Web-Scrapper.git
cd The-Hacker-News-Web-Scrapper
```

2. **Install the required dependencies:**
```
pip install -r requirements.txt
```

# How to use
1. **Run the application:**

```
python main.py
```

2. **Interact with the GUI:**

- Click the “Get News” button to fetch the latest news articles.

- Browse through the list of news titles on the left.

- Click on a title to view the full details, including the description and tags.

- Use the “Web Link” button to open the full article in your web browser.


# Project Structure

- main.py: The main script to run the GUI application.
- requesting.py: Contains the function to request and parse HTML content from Hacker News.
- extractNews.py: Contains the function to extract news details from the parsed HTML.

# Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

