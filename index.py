name = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
peso = int(input("Digite su peso: "))

if edad >= 50:
    categoria = "una persona de edad"
elif edad >= 30:
    categoria = "un adulto"
elif edad >= 18:
    categoria = "joven"
else:
    categoria = "menor de edad"

print("Hola" +name +", su edad es "+edad+ " años, usted es "+ categoria)

print (peso)



