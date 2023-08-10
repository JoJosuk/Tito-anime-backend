import scrapy


class MalSpider(scrapy.Spider):
    name = "mal"
    allowed_domains = ["myanimelist.net"]
    start_urls = ["https://myanimelist.net/topanime.php"]

    def parse(self, response):
        pass
