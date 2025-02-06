import os
import json
from datetime import datetime
from social_scraper import SocialScraper
from document_processor import DocumentProcessor
from ocr_extractor import OCRExtractor
from email_fetcher import EmailFetcher
from meeting_scheduler import MeetingScheduler

class DigitalTwin:
    def __init__(self, worker_id, data_dir="../data"):
        self.worker_id = worker_id
        self.data_dir = os.path.join(data_dir, worker_id)
        os.makedirs(self.data_dir, exist_ok=True)
        self.corpus = []
        self.scraper = SocialScraper()
        self.doc_processor = DocumentProcessor()
        self.ocr = OCRExtractor()
        self.email_fetcher = EmailFetcher()
        self.scheduler = MeetingScheduler()

    def scrape_social_media(self, urls):
        data = self.scraper.scrape(urls)
        self._store_data("social_media", data)

    def collect_documents(self, doc_paths):
        data = self.doc_processor.process(doc_paths)
        self._store_data("documents", data)

    def extract_text_from_image(self, image_path):
        text = self.ocr.extract_text(image_path)
        self._store_data("image_text", text)

    def fetch_emails(self, email_account, password, imap_url='imap.gmail.com'):
        data = self.email_fetcher.fetch(email_account, password, imap_url)
        self._store_data("emails", data)

    def schedule_meeting(self, date_time, location, topic):
        return self.scheduler.schedule(date_time, location, topic, self.query_corpus(topic))

    def _store_data(self, category, text):
        timestamp = datetime.utcnow().isoformat()
        entry = {"category": category, "timestamp": timestamp, "text": text}
        self.corpus.append(entry)
        with open(os.path.join(self.data_dir, "corpus.json"), "w", encoding='utf-8') as file:
            json.dump(self.corpus, file, indent=4)

    def query_corpus(self, keyword):
        return [entry for entry in self.corpus if keyword.lower() in entry["text"].lower()]
