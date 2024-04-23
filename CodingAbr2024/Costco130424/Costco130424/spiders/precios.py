import scrapy
from datetime import date, datetime
today = date.today()
today = f'{today:%d-%m-%Y}'

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
            descripcion = c.xpath("./li/div[2]/div[2]/div/a/span/text()").get()

            precio = c.xpath(".//span[@class='notranslate ng-star-inserted']/text()").get()
            # # marca = descripcion.split(" ")
            # marca = descripcion
            # # marca = marca.split(" ")
            precio = precio.split(".")[0]
            precio = precio.split('"')
            # # print(precio)
            # # ahorro = c.xpath("./li/div[2]/div[2]/div/a/@href").get()
            link = response.urljoin(c.xpath("./li/div[2]/div[2]/div/a/@href").get())
            marca = link.rsplit("/")[-3]
            categoria = link.rsplit("/")[-4]
            categoria_01 = link.rsplit("/")[-3]
            categoria_01 = categoria_01.rsplit("-")[1]
            categoria_04 = link.rsplit("/")[-3]
            categoria_00 = (link.rsplit("/")[-3]).split("-")[0]

            # if categoria == 'Refrigeradores-y-Congeladores':
            #    categoria = 'Refrigeradores'
            #    for _ in categoria_04:
            #        try:
            #             _ == 'French'
            #             subcategoria == 'Bottom Mount'
            #             break
            #             # return subcategoria
            #        except _ == 'Bottom':
            #             subcategoria == 'Bottom Mount'
            #             break
            #             # return subcategoria
            #        except _ == 'Duplex':
            #             subcategoria == 'Duplex'
            #             break
            #             # return subcategoria
            #        except _ == 'Door':
            #             subcategoria == 'Duplex'
            #             break
            #             # return subcategoria
            #        except _ == 'Top':
            #             subcategoria == 'Top Mount'
            #             break
            #             # return subcategoria
            #        except _ == 'Congelador':
            #             subcategoria == 'Congeladores'
            #             break
            #             # return subcategoria
            #        else:
            #            subcategoria == 'Refrigerador'
            #            # return subcategoria
            #        # elif _ == 'Duplex':
            #        #     subcategoria == 'Duplex'
            #        # # elif _ ==
            #
            # elif categoria == 'Lavadoras-y-Secadoras':
            #     categoria = 'Lavadoras'
            #     if categoria_01 == 'Lavasecadora':
            #         subcategoria = 'Lavasecadoras'
            #     # elif categoria_01 == 'Lavasecadora':
            # elif categoria == 'Lavavajillas':
            #     categoria = 'Lavavajillas'
            #     subcategoria = 'Lavavajillas'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[2] == 'Estufa':
            #         categoria = 'Estufa'
            #         subcategoria = 'Estufa'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[2] == 'Campana':
            #         categoria = 'Campanas'
            #         subcategoria = 'Campanas'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[1] == 'Campana':
            #         categoria = 'Campanas'
            #         subcategoria = 'Campanas'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[2] == 'Combo de Campana y Estufa':
            #         categoria = 'Combos'
            #         subcategoria == 'Combos'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[1] == 'Combo' and descripcion.split()[3] == 'Estufa':
            #         categoria = 'Estufa'
            #         subcategoria = 'Estufa'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[1] == 'Combo' and descripcion.split()[3] == 'Estufa':
            #         categoria = 'Estufa'
            #         subcategoria = 'Estufa'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and categoria_01 == 'Estufa':
            #         categoria = 'Estufa'
            #         subcategoria = 'Estufa'
            #
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and categoria_00 == 'Estufa':
            #         categoria = 'Estufa'
            #         subcategoria = 'Estufa'
            # elif categoria == 'Estufas-y-Campanas-de-Cocina' and categoria_00 == 'Combo':
            #         categoria = 'Estufa'
            #         subcategoria = 'Estufa'
            # elif categoria == 'Hornos-Electricos-y-Microondas' and descripcion.split()[1] or descripcion.split()[3] == 'Microondas':
            #         categoria = 'Microondas'
            #         subcategoria = 'Microondas'
            # elif categoria == 'Hornos-Electricos-y-Microondas' and descripcion.split()[1] == 'Microondas':
            #         categoria = 'Microondas'
            #         subcategoria = 'Microondas'
            # elif categoria == 'Aires-Acondicionados':
            #     categoria = 'Aires Acondicionados'
            # elif categoria == 'Aires-Acondicionados' and descripcion.split()[1] == 'Aire' and descripcion.split()[2] == 'Acondiconado':
            #     categoria = 'Aires Acondicionados'
            # elif categoria == 'Calentadores' and descripcion.split()[0] == 'Aire' and descripcion.split()[1] == 'Acondiconado':
            #     categoria = 'Aires Acondicionados'
            # elif categoria == 'Calentadores' and descripcion.split()[1] == 'Aire' and descripcion.split()[2] == 'Acondiconado':
            #     categoria = 'Aires Acondicionados'
            # elif categoria == 'Calentadores' and  categoria_01 == 'Aire' and  categoria_02 == 'Acondicionado':
            #     categoria = 'Aires Acondicionados'
            #
            # elif categoria == 'Calentadores' and descripcion.split()[2] == 'Aire' and descripcion.split()[3] == 'Acondiconado':
            #     categoria = 'Aires Acondicionados'
            #
            # elif categoria == 'Calentadores' and descripcion.split()[1] == 'Calentador' and descripcion.split()[2] == 'Portatil':
            #     categoria = 'Calentadores'
            #     subcategoria = 'Calentadores'
            # elif categoria == 'Calentadores' and  categoria_01 == 'Calentador' :
            #     categoria = 'Calentadores'
            #     subcategoria = 'Calentadores'
            #
            # elif categoria == 'Hornos-y-Parrillas' and descripcion.split()[0] or descripcion.split()[1] == 'horno':
            #     categoria = 'Hornos'
            # elif categoria == 'Hornos-Electricos-y-Microondas' and descripcion.split()[1]  == 'horno' and descripcion.split()[3] == 'microondas':
            #     categoria = 'Microondas'
            # elif categoria == 'Calentadores' and descripcion.split()[1]  == 'horno' and descripcion.split()[3] == 'microondas':
            #     categoria = 'Aires Acondicionados'
            # else:
            #     categoria = ''
            #     subcategoria = subcategoria





            yield {
                # 'Canal': 'Costco',
                # 'Fecha': today,
                #
                #
                # # 'categoria': link.rsplit("/")[-4],
                # 'categoria': categoria,
                # 'subcategoria': categoria,
                # 'sku':link.rsplit("/")[-1],
                # 'marca':link.rsplit("/")[-1],
                # 'marca': marca.split("-")[0],
                # 'descripcion': descripcion,
                # # 'type':type(descripcion),
                # 'precio': precio,
                # # 'ahorro': ahorro,
                # 'link':link,
                # 'categoria_01':categoria_01,
                # 'categoria_02':categoria_02,
                # 'categoria_03':categoria_03,
                # 'categoria_00': categoria_00,
                # 'link':link,


            }

