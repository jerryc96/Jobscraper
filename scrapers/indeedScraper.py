import requests
from enum import Enum
from scrapers.baseScraper import baseScraper

class indeedParams(Enum):
    searchTerm = "?q"
    location = "l"
    radius = "radius"
    daterange = "fromage"
    # jobtype = "jt"
    # language = "lang"
    # company = "rbc"


class indeedScraper(baseScraper):

    query = ""

    def __init__(self, searchTerm):
        self.url = "https://ca.indeed.com/"
        self.query = self.query + indeedParams['searchTerm'].value + searchTerm.replace(" ", "+")

    # def addQueryParam(self, param):
    #     if param in indeedParams.__members__:
