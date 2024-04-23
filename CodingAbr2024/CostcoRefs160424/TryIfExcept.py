categoria = 'Refrigeradores-y-Congeladores'
categoria00 = ["LG" "Refrigerador" "25'" "French" "Door" "Door" "Cooling"]
subcategoria = ''

if categoria == 'Refrigeradores-y-Congeladores':
   categoria = 'Refrigeradores'
   for _ in categoria00:
        print(categoria00[0])
        print(_)
        # try:
        #     _ == 'French'
        #
        #     subcategoria == 'Bottom Mount'
        #     print(subcategoria)
        # except:
        #     break

print(categoria)
print(subcategoria)
