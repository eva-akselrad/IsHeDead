import requests
from bs4 import BeautifulSoup
import time
import os
class NewsFetcher:
    """
    A Python class to fetch and print recent news headlines via web scraping.
    This program demonstrates how to get live news directly from a website's
    HTML content using the requests and BeautifulSoup libraries.
    """

    def __init__(self, url):
        """Initializes the NewsFetcher."""
        # The URL of the news website to scrape.
        self.NEWS_URL = url

    def return_news_as_array(self):
        """
        Makes a GET request to the news website, scrapes the headlines,
        and returns them as a list of dictionaries.
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        articles = []

        try:
            response = requests.get(self.NEWS_URL, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = soup.find_all('h3')

            if headlines:
                for headline in headlines:
                    link_tag = headline.find_parent('a')
                    title = headline.get_text(strip=True)
                    url = self.NEWS_URL + link_tag['href'] if link_tag and link_tag.has_attr('href') and not link_tag['href'].startswith('http') else link_tag['href'] if link_tag else "N/A"

                    if title:
                        articles.append({"title": title, "url": url})
            else:
                print("No headlines found. The website's structure may have changed.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return articles



    def get_and_print_news(self):
        """
        Makes a GET request to the news website, scrapes the headlines,
        and prints them.
        """
        # User-Agent header to mimic a web browser and avoid being blocked
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        
        try:
            # Send the HTTP GET request to the website
            response = requests.get(self.NEWS_URL, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            print("----------------------------------------")
            print(f"  Recent News Headlines from {self.NEWS_URL}")
            print("----------------------------------------")

            # Find all headline elements. This specific selector might need to be
            # updated if the website's HTML structure changes.
            headlines = soup.find_all('h3')

            if headlines:
                for headline in headlines:
                    # Look for the parent 'a' tag to get the link, if available
                    link_tag = headline.find_parent('a')
                    title = headline.get_text(strip=True)
                    url = self.NEWS_URL + link_tag['href'] if link_tag and link_tag.has_attr('href') and not link_tag['href'].startswith('http') else link_tag['href'] if link_tag else "N/A"

                    if title:
                        print(f"Title: {title}")
                        print(f"URL: {url}")
                        print("----------------------------------------")
            else:
                print("No headlines found. The website's structure may have changed.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



             
           
