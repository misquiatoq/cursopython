print("Bienvenido al conversor de millas a kilómetros")

print("Por favor escribe un número en millas")

millas = input() # Imput siempre nos regresara variables del tipo string(de texto)
print("Millas ingresadas:", millas) # 1 milla = 1.609 kms
print("Tipo de dato de millas", type(millas))
#Utilizaremos una funcion de conversión para cambiar millas(string) a variable de tipo numerico (float o int)
millas = float(millas)
print("Tipo de dato de millas", type(millas))

kilometros = millas * 1.609
print(millas, "Millas ingresadas")
print(kilometros, "Kilómetros")