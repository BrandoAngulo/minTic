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
    elif typeIva == 2:
        totalProducts = (costo + assets)*cantBuy;
        totalIva = assets * cantBuy;
    elif typeIva == 1:
        totalProducts = priceTsin;
        total = priceTsin *cantBuy;
        excento = False;
    if  excento == True:
        sumaIva += totalIva;
    print(f'{code}\n{name}\n{priceTsin}\n{totalProducts}');
    sumaProduct += totalProducts ;
print(f'{sumaProduct}\n{sumaIva}');


""" 
COMO DEBIA HABER RESPONDIDO SIN TANTO CODIGO REPETIDO
N=int(input())
total_ventas=0
total_iva=0
for i in range(N):
    codigo=int(input())
    nombre=input()
    cantidad=float(input())
    valor_unitario=float(input())
    tipo=int(input())
    valor_producto=cantidad*valor_unitario
    if tipo==1:
        iva=0
    elif tipo==2:
        iva=valor_producto*0.05
    else:
        iva=valor_producto*0.19
    valor_final=valor_producto+iva
    total_iva+=iva
    total_ventas+=valor_final
    print(codigo)
    print(nombre)
    print(valor_producto)
    print(valor_final)
print(total_ventas)
print(total_iva)

 """