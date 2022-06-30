n = 2 #int(input()); 
sumaIva = 0;
sumaProduct = 0;
listCode=[];
listName=[];
listCantBuy=[];
listCosto=[];
listTypeIva=[];
listpriceTsin = []
for i in range(n):
    code = int(input());
    listCode.append(code);
    name = input();
    listName.append(name);
    cantBuy = float(input());  
    listCantBuy.append(cantBuy);
    costo = float(input());
    listCosto.append(costo);  
    typeIva =  int(input());
    listTypeIva.append(typeIva); 
    listpriceTsin.append(listCantBuy[i] * listCosto[i])
for j in range(n):
    print(f'{listCode[j]} {listName[j]}');
    if listTypeIva[j] == 1:
        totalProducts = listpriceTsin[j];
        total = listpriceTsin[j] *listCantBuy[j];
        totalIva= 0;
        print(f'{total} {totalProducts}');
    elif listTypeIva[j] == 2:
        assets = (listCosto[j] * 5)/100;  
        ProductAssets = listCosto[j] + assets;
        totalProducts = ProductAssets*listCantBuy[j];
        totalIva = assets * listCantBuy[j];
        print(f'{totalProducts} {listpriceTsin[j]}');
    elif listTypeIva[j] == 3:
        iva = (listCosto[j] * 19)/100; 
        ProductIva = listCosto[j]+iva;
        totalProducts = ProductIva*listCantBuy[j];
        totalIva = iva*listCantBuy[j];
        print(f'{totalProducts} {listpriceTsin[j]}');
    sumaIva += totalIva;
    sumaProduct += totalProducts;
print(f'{len(listCode)}\n{len(listName)}\n{len(listCantBuy)}\n{len(listCosto)}\n{len(listTypeIva)}');
print(f'{sumaProduct}\n{sumaIva}');