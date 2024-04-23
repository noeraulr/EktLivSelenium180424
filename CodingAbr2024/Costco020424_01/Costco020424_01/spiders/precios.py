import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import date, datetime
today = date.today()


class PreciosSpider(CrawlSpider):
    name = "precios"
    allowed_domains = ["www.costco.com.mx"]
    start_urls = ["https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Refrigeradores-y-Congeladores/c/cos_6.1.1"]

    # download_delay = 1
    # rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="lister-name js-lister-name"]'), callback="parse_item", follow=True),
        #Follow True is set by default
        Rule(LinkExtractor(restrict_xpaths='(//a[@class="page-link"])[4]')),
    )

    def parse_item(self, response):
        # subcategoria = response.xpath("//tr[@class='ng-star-inserted'])[6]/text()").get()
        # # sku = response.xpath("normalize-space(substring(./div[2]/div[2]/span/text(),6,6))").get()

        sku = response.xpath("normalize-space(//span[@class='notranslate']/text())").get()
        marca = response.xpath("normalize-space(//h1[@class='product-name']/text())").get()
        marca = marca.split()[0]
        descripcion = response.xpath("normalize-space(//h1[@class='product-name']/text())").get()

        # precio= response.xpath("substring(normalize-space(//span[@class='you-pay-value']/text())").get()
        precio= response.xpath("normalize-space(//span[@class='you-pay-value']/text())").get()


        # link = response.xpath("normalize-space(./div[2]/div[2]/a/@href)").get()
        # link_01 = response.urljoin(link)
        links = response.url
        yield {
            'Canal': 'Costco',
            'Fecha': today,
            'categoria': 'Refigeradores',
            # 'subcategoria': subcategoria,
            #
            'sku': sku,
            'marca': marca,
            'descripcion': descripcion,
            # # 'precio_de':precio_de,
            'precio': precio,
            # 'ahorro':ahorro,
            # 'link':link,
            # 'link_01':link_01

            'links':links,
        }
        next_page = response.xpath("//a[@class='page-link']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

