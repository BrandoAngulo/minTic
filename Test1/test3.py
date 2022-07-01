n = int(input()); 
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
    listpriceTsin.append(listCantBuy[i] * listCosto[i]);
print(f'{len(listCode)}\n{len(listName)}\n{len(listCantBuy)}\n{len(listCosto)}\n{len(listTypeIva)}');
for j in range(n):
    print(f'{listCode[j]}\n{listName[j]}');
    if listTypeIva[j] == 1:
        totalProducts = listpriceTsin[j];
        total = listpriceTsin[j] *listCantBuy[j];
        totalIva= 0;
        print(f'{totalProducts}\n{total}');
    elif listTypeIva[j] == 2:
        assets = (listCosto[j] * 5)/100;  
        ProductAssets = listCosto[j] + assets;
        totalProducts = ProductAssets*listCantBuy[j];
        totalIva = assets * listCantBuy[j];
        print(f'{listpriceTsin[j]}\n{totalProducts}');
    elif listTypeIva[j] == 3:
        iva = (listCosto[j] * 19)/100; 
        ProductIva = listCosto[j]+iva;
        totalProducts = ProductIva*listCantBuy[j];
        totalIva = iva*listCantBuy[j];
        print(f'{listpriceTsin[j]}\n{totalProducts}');
    sumaIva += totalIva;
    sumaProduct += totalProducts;
print(f'{sumaProduct}\n{sumaIva}');

""" codigo de la respuesta  """
""" N=int(input())
total_ventas=0
total_iva=0
codigo=[]
nombre=[]
cantidad=[]
valor_unitario=[]
tipo=[]
valor_producto=[]
iva=[]
valor_final=[]
for i in range(N):
    codigo.append(int(input()))
    nombre.append(input())
    cantidad.append(float(input()))
    valor_unitario.append(float(input()))
    tipo.append(int(input()))
print(len(codigo))
print(len(nombre))
print(len(cantidad))
print(len(valor_unitario))
print(len(tipo))
for i in range(N):
    valor_producto.append(cantidad[i]*valor_unitario[i])
    if tipo[i]==1:
        iva.append(0)
    elif tipo[i]==2:
        iva.append(valor_producto[i]*0.05)
    else:
        iva.append(valor_producto[i]*0.19)
    valor_final.append(valor_producto[i]+iva[i])
    total_iva+=iva[i]
    total_ventas+=valor_final[i]
    print(codigo[i])
    print(nombre[i])
    print(valor_producto[i])
    print(valor_final[i])
print(total_ventas)
print(total_iva) """




