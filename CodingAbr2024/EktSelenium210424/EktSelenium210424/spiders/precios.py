import scrapy


class PreciosSpider(scrapy.Spider):
    name = "precios"
    allowed_domains = ["www.elektra.mx"]
    start_urls = ["https://www.elektra.mx"]

    def parse(self, response):
        pass
