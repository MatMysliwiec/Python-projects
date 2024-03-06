import requests
from bs4 import BeautifulSoup


class PageScraper:
    def __init__(self, base_urf):
        self.base_url = base_urf
        self.links = set()
        self.images = set()

    def scrape_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all('a', href=True):
            self.links.add(link['href'])

        for img in soup.find_all('img', src=True):
            self.images.add(img['src'])

    def save_to_file(self, filename, data):
        with open(filename, 'w') as file:
            for item in data:
                file.write(item + "\n")

    def scrape_and_save(self):
        self.scrape_page(self.base_url)
        self.save_to_file("links.txt", self.links)
        self.save_to_file("images.txt", self.images)


if __name__ == "__main__":
    base_url = ""
    scraper = PageScraper(base_url)
    scraper.scrape_and_save()
