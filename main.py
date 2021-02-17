from scrapers.indeedScraper import indeedScraper
QUERY = "software developer"


if __name__ == '__main__':
    scraper = indeedScraper(QUERY)
    page = scraper.search()
    print(page.content)