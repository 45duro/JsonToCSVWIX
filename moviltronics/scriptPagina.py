import json
import os
#import csv

head = ("handleId","fieldType","name","description",
	"productImageUrl","collection","sku","ribbon",
	"price","surcharge","visible","discountMode",
	"discountValue","inventory","weight","productOptionName1","productOptionType1","productOptionDescription1","productOptionName2","productOptionType2","productOptionDescription2","productOptionName3","productOptionType3","productOptionDescription3","productOptionName4","productOptionType4","productOptionDescription4","productOptionName5","productOptionType5","productOptionDescription5","productOptionName6","productOptionType6","productOptionDescription6","additionalInfoTitle1","additionalInfoDescription1","additionalInfoTitle2","additionalInfoDescription2","additionalInfoTitle3","additionalInfoDescription3","additionalInfoTitle4","additionalInfoDescription4","additionalInfoTitle5","additionalInfoDescription5","additionalInfoTitle6","additionalInfoDescription6","customTextField1","customTextCharLimit1","customTextMandatory1")


def sacarImagenes(elementos):
	cadena = ""
	for elemento in elementos['productImageUrl']:
		if cadena == "":
			cadena = elemento
		else:
			cadena = cadena + ";" + elemento
		
	print(cadena)

def sacar_precio(valor):
	X = valor.replace(",00","");
	Y = X.replace("$","");
	Z = Y.replace(".","");
	
	return Z;


def escribirHead(head):
	cadena = ""
	for i in head:
		if cadena == "":
			cadena = i
		else:
			cadena = cadena + "," + i;

	cadena = cadena  + ";;;;;"

	return cadena;




row1 = ""
row2 = ""
row3 = ""
row4 = ""
   
with open('Descarga.json', encoding="utf8") as file:
    data = json.load(file);
    contador = 159 #numero de iteraciones
    row = ""
    print(len(data['Producto']))
    for p in data['Producto']:
        contador = contador + 1;

        for i in range(50):
            if i == 0:
                row = row + "Producto" + str(contador)

            elif i == 1:
                    row = row + "," + "Product"

            elif i == 4:
                    flag = "" #variable temporal
                    for img in p['productImageUrl']:
                            if flag == "":
                                    flag = img['image']
                            else:
                                    flag = flag + ";" + img['image']

                    row = row + "," + flag
            elif i == 8:
                    print(head[i])
                    bandera = sacar_precio(p[head[i]])
                    row = row + "," + bandera

            elif i == 13:
                    row = row + "," + "InStock"

            elif i == 33:
                    row = row + "," + "Caracteristicas"

            elif i == 34:
                    row = row + ',"' + p[head[i]] + '"'

            else:
                    try:
                            row = row + ',"' + p[head[i]] + '"' #if i > 1 else row+p[head[i]]

                    except:
                            row = row + ","


        row = row  + ";;;;;\n"
    
            



    print("estamos listos");



archvoCreado = open("productosFiltrados.csv", "a", encoding="utf8")
archvoCreado.write(escribirHead(head) + os.linesep)
archvoCreado.write(row)
archvoCreado.close()
	




