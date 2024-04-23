import scrapy
import csv
from datetime import date, datetime
today = date.today()
today = f'{today:%d-%m-%Y}'

class PreciosSpider(scrapy.Spider):
    name = "precios"
    allowed_domains = ["www.costco.com.mx"]
    start_urls = [
                  "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Refrigeradores-y-Congeladores/c/cos_6.1.1",
                  "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Lavadoras-y-Secadoras/c/cos_6.1.3",
                  "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Hornos-y-Parrillas/c/cos_6.1.5",
                  "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Estufas-y-Campanas-de-Cocina/c/cos_6.1.6",
                  "https://www.costco.com.mx/Linea-Blanca-y-Cocina/Linea-Blanca/Lavavajillas/c/cos_6.1.4",
                  "https://www.costco.com.mx/Electrodomesticos/Electrodomesticos-de-Cocina/Hornos-Electricos-y-Microondas/c/cos_22.1.2",
                  "https://www.costco.com.mx/Electrodomesticos/Climatizacion/Aires-Acondicionados/c/cos_22.3.1",
                  "https://www.costco.com.mx/Electrodomesticos/Climatizacion/Calentadores/c/cos_22.3.3",
                  ]


    def parse(self, response):
        container = response.xpath("//div[@class='product-listing-container']/ul/sip-product-list-item")
        items = []

        header = ['Canal','Fecha','categoria','subcategoria','sku','marca','descripcion','precio']
        for c in container:
            item = []
            # try:
            descripcion = c.xpath("./li/div[2]/div[2]/div/a/span/text()").get()
            # except None:
            #     descripcion =
            # try:
            precio = c.xpath(".//span[@class='notranslate ng-star-inserted']/text()").get()
            if precio != None:
                precio = precio.split(".")[0]
            else:
                None
            link = response.urljoin(c.xpath("./li/div[2]/div[2]/div/a/@href").get())
            categoria = link.rsplit("/")[-4]
            categoria_00 = link.rsplit("/")[-3]
            categoria_00 = categoria_00.split('-')[0]
            categoria_01 = link.rsplit("/")[-3]
            categoria_01 = categoria_01.split("-")[0]
            # categoria00 = type(categoria00)
            subcategoria = ""
            try:
                marca = link.rsplit("/")[-3]
                marca = marca.split("-")[0]
                # marca = descripcion.split(" ")
            except:
                break
            # if categoria != None:
            if categoria == 'Refrigeradores-y-Congeladores':
               categoria = 'Refrigeradores'
               subcategoria = 'Refrigeradores'
            elif categoria == 'Lavadoras-y-Secadoras':
                categoria = 'Lavadoras'
                subcategoria = 'Lavadoras'
            elif categoria == 'Lavavajillas':
                categoria = 'Lavavajillas'
                subcategoria = 'Lavavajillas'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[2] == 'Estufa':
                categoria = 'Estufa'
                subcategoria = 'Estufa'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[2] == 'Campana':
                categoria = 'Campanas'
                subcategoria = 'Campanas'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[1] == 'Campana':
                categoria = 'Campanas'
                subcategoria = 'Campanas'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[2] == 'Combo de Campana y Estufa':
                categoria = 'Combos'
                subcategoria == 'Combos'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[1] == 'Combo' and descripcion.split()[3] == 'Estufa':
                categoria = 'Estufa'
                subcategoria = 'Estufa'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and descripcion.split()[1] == 'Combo' and descripcion.split()[3] == 'Estufa':
                categoria = 'Estufa'
                subcategoria = 'Estufa'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and categoria_01 == 'Estufa':
                categoria = 'Estufa'
                subcategoria = 'Estufa'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and categoria_01 == 'Estufa':
                categoria = 'Estufa'
                subcategoria = 'Estufa'
            elif categoria == 'Estufas-y-Campanas-de-Cocina' and categoria_01 == 'Combo':
                categoria = 'Estufa'
                subcategoria = 'Estufa'

            # elif categoria == 'Hornos-Electricos-y-Microondas' and descripcion.split()[1] or descripcion.split()[3] == 'Microondas':
            #     categoria = 'Microondas'
            #     subcategoria = 'Microondas'
            elif categoria == 'Hornos-Electricos-y-Microondas' and descripcion.split()[1] == 'Microondas':
                categoria = 'Microondas'
                subcategoria = 'Microondas'
            elif categoria == 'Aires-Acondicionados':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Aires-Acondicionados' and descripcion.split()[1] == 'Aire' and descripcion.split()[2] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and descripcion.split()[0] == 'Aire' and descripcion.split()[1] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            elif categoria == 'Calentadores' and descripcion.split()[1] == 'Aire' and descripcion.split()[2] == 'Acondiconado':
                categoria = 'Aires Acondicionados'
            # elif categoria == 'Calentadores' and  categoria_01 == 'Aire' and  categoria_02 == 'Acondicionado':
            #     categoria = 'Aires Acondicionados'

            # elif categoria == 'Calentadores' and descripcion.split()[2] == 'Aire' and descripcion.split()[3] == 'Acondiconado':
            #     categoria = 'Aires Acondicionados'
            #
            # elif categoria == 'Calentadores' and descripcion.split()[1] == 'Calentador' and descripcion.split()[2] == 'Portatil':
            #     categoria = 'Calentadores'
            #     subcategoria = 'Calentadores'
            elif categoria == 'Calentadores' and  categoria_01 == 'Calentador' :
                categoria = 'Calentadores'
                subcategoria = 'Calentadores'
            sku = link.rsplit("/")[-1]
            item.append('Costco')
            item.append(today)
            item.append(categoria)
            item.append(subcategoria)
            item.append(sku)
            item.append(marca)
            item.append(descripcion)
            item.append(precio)
            items.append(item)
            with open('precios01.py','w')as f:
                w = csv.writer(f,delimiter=',')
                w.writerow(header)
                w.writerows(items)

            # pass
            yield {
                'Canal': 'Costco',
                'Fecha': today,
                #
                #
                # # 'categoria': link.rsplit("/")[-4],
                'categoria': categoria,
                # 'categoria_00': categoria_00,

                'subcategoria': subcategoria,
                # 'lista':lista,
                'sku':link.rsplit("/")[-1],

                'marca': marca,
                'descripcion': descripcion,
                # 'marca': marca,
                # 'type':type(descripcion),
                'precio': precio,
                # 'precio_type': type(precio),

                # # 'ahorro': ahorro,
                # 'link':link,
                # 'categoria_01':categoria_01,
                # 'categoria_02':categoria_02,
                # 'categoria_03':categoria_03,
                # 'categoria_00': categoria_00,
                # 'link':link,
            }
