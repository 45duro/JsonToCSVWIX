import json
#import csv

head = ("handeld", "fieldType","name", "description","productImageUrl",
			"collection","sku","ribbon","price", "surcharge",
			"visible", "discountMode", "discountValue","inventory","weight",
			"productOptionName1","productOptionType1","productOptionDescription1",
			"additionalInfoTitle1",	"additionalInfoDescription1",
			"productOptionName2","productOptionType2","productOptionDescription2",
			"additionalInfoTitle2",	"additionalInfoDescription2",
			"productOptionName3", "productOptionType3", "productOptionDescription3",
			"additionalInfoTitle3",	"additionalInfoDescription3", "productOptionName4",
			"productOptionType4", "productOptionDescription4", "additionalInfoTitle4",
			"additionalInfoDescription4", "productOptionName5",	"productOptionDescription5",
			"additionalInfoTitle5",	"additionalInfoDescription5",	
			"productOptionName6",	"productOptionType6",	"productOptionDescription6",	
			"additionalInfoTitle6",	"additionalInfoDescription6",	"customTextField1",	"customTextCharLimit1",	"customTextMandatory1",	"customTextField2",	"customTextCharLimit2",	"customTextMandatory2"
)


def sacarImagenes(elementos):
	cadena = ""
	for elemento in elementos['productImageUrl']:
		if cadena == "":
			cadena = elemento
		else:
			cadena = cadena + ";" + elemento
		
	print(cadena)



row = ""

   
with open('Descarga.json', encoding="utf8") as file:
    data = json.load(file);

    contador = 0 #numero de iteraciones
    row = ""
    for p in data['Producto']:
        contador += 1;
    
        
        if contador == -1:
        	flag = "" #variable temporal
	        for img in p['productImageUrl']:
	        	if flag == "":
	        		flag = img
	        	else:
	        		flag = flag + ";" + img

        		row=row+flag


        else:
        	for i in range(50):
        		print(i) 

    print(row);

	    	




