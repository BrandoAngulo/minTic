n = 2 #int(input()); 
sumaIva = 0;
sumaProduct = 0;
listCode=[];
listName=[];
listCantBuy=[];
listCosto=[];
listTypeIva=[];
for i in range(n):
    code = 1205 #int(input());
    listCode.append(code);
    name = "balde"#input();
    listName.append(name);
    cantBuy = 2 #float(input());  
    listCantBuy.append(cantBuy);
    costo = 1500 #float(input());
    listCosto.append(costo);  
    typeIva =  int(input());
    listTypeIva.append(typeIva); 
    priceTsin = cantBuy * costo;   
for j in range(n):
    print(f'{listCode[j]} {listName[j]}');
    if typeIva == 1:
        totalProducts = priceTsin;
        total = priceTsin *cantBuy;
        print(total);
    elif typeIva == 2:
        assets = (costo * 5)/100;  
        ProductAssets = costo + assets;
        totalProducts = ProductAssets*cantBuy;
        totalIva = assets * cantBuy;
        print(totalProducts);
    elif typeIva == 3:
        iva = (costo * 19)/100; 
        ProductIva = costo+iva;
        totalProducts = ProductIva*cantBuy;
        totalIva = iva*cantBuy;
        print(totalProducts);
    sumaIva += totalIva;
    sumaProduct += totalProducts;
print(f'{len(listCode)}\n{len(listName)}\n{len(listCantBuy)}\n{len(listCosto)}\n{len(listTypeIva)}');
print(f'{sumaProduct}\n{sumaIva}');