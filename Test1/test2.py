""" Continuando con el proceso de sistematización del proceso de venta de productos de   la super tienda por departamentos “Tu Vecino”, además de la información ya suministrada en el Reto No. 1, ahora mencionan que se deben procesar N productos (N es suministrado) y adicionalmente el producto tiene una información adicional sobre el tipo de IVA que se debe aplicar, quedando la entrada de la siguiente forma:

N, como la cantidad de productos a procesar.
Para cada producto, ingresar:
Código del producto.
Nombre al producto.
Cantidad comprada.
Valor unitario (sin IVA).
Tipo de IVA, que puede ser:
1: Exento de IVA
2: Bienes, donde se aplica como IVA el 5%
3: General, donde se aplica como IVA el 19%
El gerente de la tienda desea que a través de un programa se calcule, para cada producto, el valor del producto, que corresponde a la cantidad comprada por el valor unitario, el valor del IVA y el valor final del producto, que corresponde a la suma del valor del producto más el valor de IVA. Además, se desea conocer el valor total de la compra, es decir, la suma de los N productos (tomando el valor final del producto, es decir con IVA aplicado) y el valor total de IVA de la compra (La suma del valor de IVA de los N productos)

 

Para este Reto, con la información suministrada se solicita resolver la situación problema, generando como salida, para cada uno de los N productos, el código del producto, nombre del producto, valor del producto sin aplicar IVA y el valor final del producto, una vez aplicada el IVA, el valor total de la compra, sumando el valor final de los N productos y el valor total de IVA, sumando el valor de IVA de los N productos

 

Recomendaciones importantes:

El orden en la entrada de la información al programa es tal y como se suministra, es decir, primero la cantidad de productos (N, como dato entero)), luego para cada producto se ingresa el código del artículo como dato entero, nombre del producto, la cantidad comprada como dato flotante, el valor unitario como dato flotante y finalmente el tipo de IVA aplicar al producto (1,2 o 3)
En las instrucciones de lectura y escritura (input y print) no utilizar mensajes, debido a que el programa se comprobará a través de datos de prueba.
Ejemplos: codigo=int(input())

                             print(codigo)   

El método de comprobación es a través de casos de prueba, ya definidos en plataforma, que validarán la eficacia del programa. """