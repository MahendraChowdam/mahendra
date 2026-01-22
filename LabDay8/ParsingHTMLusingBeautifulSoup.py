import requests
from bs4 import BeautifulSoup
import json

def fetch_and_parse_webpage():
    url = "https://www.example.com"

    try:
        # Fetch the HTML webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse HTML using BeautifulSoup with lxml parser
        soup = BeautifulSoup(response.text, "lxml")

        # Extract page title
        page_title = soup.title.string if soup.title else "No title found"

        # Extract all hyperlinks
        links = []
        for a_tag in soup.find_all("a", href=True):
            links.append(a_tag["href"])

        # Extract list data (example: all <li> items)
        list_items = []
        for li in soup.find_all("li"):
            text = li.get_text(strip=True)
            if text:
                list_items.append(text)

        # Prepare extracted data
        extracted_data = {
            "page_title": page_title,
            "total_links": len(links),
            "links": links,
            "list_items": list_items
        }

        # Convert to JSON and save to file
        with open("webpage_data.json", "w", encoding="utf-8") as file:
            json.dump(extracted_data, file, indent=4)

        print("Webpage data successfully saved to webpage_data.json")

    except requests.exceptions.HTTPError as http_error:
        print(f"HTTP error occurred: {http_error}")

    except requests.exceptions.ConnectionError:
        print("Connection error occurred")

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.RequestException as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    fetch_and_parse_webpage()
