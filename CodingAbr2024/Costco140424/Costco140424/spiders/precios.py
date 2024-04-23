import scrapy


class PreciosSpider(scrapy.Spider):
    name = "precios"
    allowed_domains = ["www.costco.com.mx"]
    start_urls = [
        # "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Lavadoras-y-Secadoras/c/cos_6.1.3",
        # "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Hornos-y-Parrillas/c/cos_6.1.5",
        "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Estufas-y-Campanas-de-Cocina/c/cos_6.1.6",
        # "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Lavavajillas/c/cos_6.1.4",
        # "https://www.costco.com.mx/Electrodomesticos/Electrodomesticos-de-Cocina/Hornos-Electricos-y-Microondas/c/cos_22.1.2",
        # "https://www.costco.com.mx/Electrodomesticos/Climatizacion/Aires-Acondicionados/c/cos_22.3.1",
        # "https://www.costco.com.mx/Electrodomesticos/Climatizacion/Calentadores/c/cos_22.3.3",
    ]

    def parse(self, response):
        container = response.xpath("//div[@class='product-listing-container']/ul/sip-product-list-item")
        for c in container:
            link = response.urljoin(c.xpath("./li/div[2]/div[2]/div/a/@href").get())

            descripcion = c.xpath("./li/div[2]/div[2]/div/a/span/text()").get()

            marca = link.rsplit("/")[-3]
            marca = marca.split("-")[0]
            # descripcion = link.rsplit("/")[-3]
            # descripcion = descripcion.replace("-"," ")
            # # descripcion = descripcion.split("-")[1:]

            # descripcion = descripcion.rsplit("-")
            # descripcion =
            precio = c.xpath(".//span[@class='notranslate ng-star-inserted']/text()").get()
            precio = precio.split(".")[0]
            precio = precio.split('"')

            categoria = link.rsplit("/")[-4]
            if categoria == 'Refrigeradores-y-Congeladores':
               categoria = 'Refrigeradores'
            elif categoria == 'Lavadoras-y-Secadoras':
                categoria = 'Lavadoras'
            elif categoria == 'Aires-Acondicionados':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Aires-Acondicionados' and descripcion.split()[1] == 'Aire' and descripcion.split()[2] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and descripcion.split()[0] == 'Aire' and descripcion.split()[1] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and descripcion.split()[1] == 'Aire' and descripcion.split()[2] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and  categoria_01 == 'Aire' and  categoria_02 == 'Acondicionado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and descripcion.split()[2] == 'Aire' and descripcion.split()[3] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and descripcion.split()[1] == 'Calentador' and descripcion.split()[2] == 'Portatil':
                categoria = 'Calentadores'
            elif categoria == 'Calentadores' and  categoria_01 == 'Calentador' :
                categoria = 'Calentadores'
            elif categoria == 'Hornos-y-Parrillas' and descripcion.split()[0] or descripcion.split()[1] == 'horno':
                categoria = 'Hornos'
            elif categoria == 'Hornos-Electricos-y-Microondas' and descripcion.split()[1]  == 'horno' and descripcion.split()[3] == 'microondas':
                categoria = 'Microondas'
            elif categoria == 'Calentadores' and descripcion.split()[1]  == 'horno' and descripcion.split()[3] == 'microondas':
                categoria = 'Aires Acondicionados'
            else:
                categoria = ''
            subcategoria = subcategoria



            yield {
                # 'link':link,
                'categoria':categoria,
                'marca':marca,
                'descripcion':descripcion,
                # 'descripcion':descripcion,
                'precio':precio,
        }
