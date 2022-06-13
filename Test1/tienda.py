codPro = int(input());
namePro = str(input());
cantidad = float(input());
valUndPro = float(input());
iva = 0.19;
# valor producto sin iva
valPro = (valUndPro * cantidad);
# valor producto mas iva
proFinal = (valPro * iva) + valPro;

#print(codPro,namePro,valpro,proFinal);
print(codPro);
print(namePro);
print(valPro);
print(proFinal);
#mensaje = (f'{codPro}\n{namePro}\n{valpro}\n{proFinal}');
#print(mensaje);

