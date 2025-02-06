import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer

class SocialScraper:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def scrape(self, urls):
        results = []
        for url in urls:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()
                sentiment = self.sia.polarity_scores(text)
                results.append({"url": url, "text": text, "sentiment": sentiment})
            except Exception as e:
                print(f"Error scraping {url}: {e}")
        return results
