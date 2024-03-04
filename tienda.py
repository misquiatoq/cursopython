print("**************************************")
print("*******     BIENVENIDO A     *********")
print("***     LA TIENDA DE  MASCOTAS     ***")
print("**************************************")

num_perros = 40
num_gatos = 30
num_pajaros = 10

animales_totales = num_perros + num_gatos + num_pajaros
print("Por favor ingresa tu numbre")
nombre = input()

print("Ahora por favor escribe tu apellido")
apellido = input()

#Concatenación variable(nombre) + espacio(string) + variable(apellido) = nombre_completo
nombre_completo = nombre + " " + apellido + ","
print("Hola", nombre_completo, "gracias por visitar La Tienda de Mascotas.")

print("Actualente contamos con:")
print(num_perros ,"Perros ,", num_gatos, "Gatos y", num_pajaros, "Pajaros.")
print("En total tenemos", animales_totales, "animales")