n = int(input()); 
sumaIva = 0;
sumaProduct = 0;
for i in range(n): 
    code = int(input());  
    name = input();  
    cantBuy = float(input());  
    costo = float(input()); 
    typeIva = int(input());
    priceTsin = cantBuy * costo;
    iva = (costo * 19)/100;   
    assets = (costo * 5)/100;  
    excento = True;
    if typeIva == 3: 
        totalProducts = (costo + iva)*cantBuy;
        totalIva = iva*cantBuy;
        #total = priceFinalProduct * cantBuy;
        print(f'{code}\n{name}\n{priceTsin}\n{totalProducts}');

    elif typeIva == 2:
        totalProducts = (costo + assets)*cantBuy;
        totalIva = assets * cantBuy;
        #total = priceFinalProduct * cantBuy;
        print(f'{code}\n{name}\n{priceTsin}\n{totalProducts}');

    elif typeIva == 1:
        totalProducts = priceTsin;
        total = priceTsin *cantBuy;
        print(f'{code}\n{name}\n{priceTsin}\n{totalProducts}');

        excento = False;
    if  excento == True:
        sumaIva += totalIva;
    sumaProduct += totalProducts ;
print(f'{sumaProduct}\n{sumaIva}');