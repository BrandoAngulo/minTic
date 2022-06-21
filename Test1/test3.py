
n = 2 #int(input()); 
sumaIva = 0;
sumaProduct = 0;
listCode=[];
listName=[];
listCantBuy=[];
listCosto=[];
listTypeIva=[];
listValorProducto=[];
listValorIva=[];
listValorFinal=[];
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
    iva = (costo * 19)/100;   
    assets = (costo * 5)/100;  
    excento = True;
    if typeIva == 3: 
        ProductIva = costo+iva;
        totalProducts = ProductIva*cantBuy;
        totalIva = iva*cantBuy;
        listValorFinal.append(ProductIva);
    elif typeIva == 2:
        ProductAssets = costo + assets;
        totalProducts = ProductAssets*cantBuy;
        totalIva = assets * cantBuy;
        listValorFinal.append(ProductAssets);
    elif typeIva == 1:
        totalProducts = priceTsin;
        total = priceTsin *cantBuy;
        listValorFinal.append(ProductIva);
        excento = False;
    if  excento == True:
        sumaIva += totalIva;
    print(f'{code}\n{name}\n{priceTsin}\n{totalProducts}');
    sumaProduct += totalProducts;
    listValorProducto.append(totalProducts);
    listValorIva.append(totalIva);
print(f'{sumaProduct}\n{sumaIva}');
print(f'{len(listCode)}\n{len(listName)}\n{len(listCantBuy)}\n{len(listCosto)}\n{len(listTypeIva)}\n{listValorProducto}\n{listValorIva}\n{listValorFinal}');

