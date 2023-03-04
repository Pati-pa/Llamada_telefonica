# Programa para saber el costo de una llamada

print("--------------------------------------")
print("------------Costo de tu llamada--------")
print("---------------------------------------")

#input
dl= int(input("Digite el valor de dl= "))

#Procesing
if dl<=3 :
    Cl = "300"
else :
    t = dl-3
    Cl = 300 + t*50

#output 
print("------------------------------------------")
print("---------Resultado------------------------")
print("------------------------------------------")
print("El costo de tu llamada es : " + str(Cl) )