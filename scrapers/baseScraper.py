import requests

class baseScraper:
    query = ""
    url = ""

    def search(self):
        try:
            return requests.get(self.url + self.query)
        except Exception as e:
            print(self.url + self.query)
            print("\n")
            print(e)