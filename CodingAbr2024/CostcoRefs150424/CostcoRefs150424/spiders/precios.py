import scrapy
from datetime import date, datetime

today = date.today()
today = f'{today:%d-%m-%Y}'


class PreciosSpider(scrapy.Spider):
    name = "precios"
    allowed_domains = ["www.costco.com.mx"]
    start_urls = [
        # Refrigeradores
        "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Refrigeradores-y-Congeladores/c/cos_6.1.1",
        "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Refrigeradores-y-Congeladores/c/cos_6.1.1"

    ]

    def parse(self, response):
        container = response.xpath("//div[@class='product-listing-container']/ul/sip-product-list-item")
        for c in container:
            # try:
            descripcion = c.xpath("./li/div[2]/div[2]/div/a/span/text()").get()
            # except None:
            #     descripcion =
            try:
                precio = c.xpath(".//span[@class='notranslate ng-star-inserted']/text()").get()
                precio = precio.split(".")[0]
                # # precio = precio.split('"')

            except precio == 'None':
                break
            # # marca = descripcion
            # marca = marca.split(" ")
            # # print(precio)
            # # ahorro = c.xpath("./li/div[2]/div[2]/div/a/@href").get()
            link = response.urljoin(c.xpath("./li/div[2]/div[2]/div/a/@href").get())
            try:
                marca = link.rsplit("/")[-3]
                marca = marca.split("-")[0]
                # marca = descripcion.split(" ")
            except marca == 'Null':
                break
            categoria = link.rsplit("/")[-4]




            yield {
                'Canal': 'Costco',
                'Fecha': today,
                #
                #
                # # 'categoria': link.rsplit("/")[-4],
                'categoria': categoria,
                # 'subcategoria': categoria,
                # 'sku':link.rsplit("/")[-1],

                # 'marca': marca,
                'descripcion': descripcion,
                'marca': marca,
                # 'type':type(descripcion),
                'precio': precio,
                'precio_type': type(precio),

                # # 'ahorro': ahorro,
                # 'link':link,
                # 'categoria_01':categoria_01,
                # 'categoria_02':categoria_02,
                # 'categoria_03':categoria_03,
                # 'categoria_00': categoria_00,
                # 'link':link,
            }












        next_page = response.xpath("//a[@class='page-link']/@href").get()
        if next_page:
           yield scrapy.Request(url=next_page,callback=self.parse)
