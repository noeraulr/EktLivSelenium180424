import scrapy
from datetime import date, datetime
today = date.today()
today = f'{today:%d-%m-%Y}'




class PreciosSpider(scrapy.Spider):
    name = "precios"
    allowed_domains = ["www.elektra.mx"]
    start_urls = [
    # for _ in range(1,4):
    #     start_url = f'"https://www.elektra.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores?page={_}"'
    #     start_urls.append(start_url)
    # #     start_urls = [
    #     "https://www.elektra.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores",
    #     "https://www.elektra.mx/linea-blanca/lavado-y-secado/lavadoras"
    # #
        "https://www.elektra.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores?page=1",
        "https://www.elektra.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores?page=2",
        "https://www.elektra.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores?page=3",
    ]

    def parse(self, response):
        container = response.xpath("//div[@id='gallery-layout-container']/div")
        for c in container:
            # try:
            descripcion = c.xpath("./section/a/article/div[2]/div[2]/div/h3/span/text()").get()
            # except:
            #     break
            #
            # try:
            #     link = response.urljoin(c.xpath("./section/a/@href").get())
            # except:
            #     break
            # try:
            #     sku = link.rsplit("/")[-2]
            #     sku = sku.rsplit("-")[-1]
            # except:
            #     break
            # try:
            #     marca = descripcion.rsplit()[-1]
            #     if marca == 'Samsung':
            #        marca = 'Samsung'
            #     elif marca == 'LG':
            #         marca = 'LG'
            #     else:
            #         None
            # except:
            #     break
            # try:
            #     categoria = descripcion.split()[0]
            # except:
            #     break
            # try:
            precio_a = c.xpath("./section/a/article/div[2]/div[3]/div/div/div/div[1]/div[2]/span/span/span/text()").get()
            # except:
            #     break
            yield {
                'Canal': 'Elektra',
                'Fecha': today,
                # 'sku':sku,
                # 'marca': marca,
                # 'categoria': categoria,
                # 'subcategoria': 'Refrigeradores',
                #
                'descripcion':descripcion,
                'precio':precio_a,
                # 'link':link
            }

        next_page = response.xpath("//button[@class='vtex-button bw1 ba fw5 v-mid relative pa0 lh-solid br2 min-h-small t-action--small bg-action-primary b--action-primary c-on-action-primary hover-bg-action-primary hover-b--action-primary hover-c-on-action-primary pointer ']/@href").get()
        if next_page:
           yield scrapy.Request(url=next_page, callback=self.parse)
