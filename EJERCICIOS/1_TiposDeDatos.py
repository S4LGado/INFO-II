# Crear variables y asignarles los siguientes tipos de datos

# Enteros: 1, 2, 3, 999
# Luego reste sucesivamente del último al primero y almacenelo
# en una variable llamada resultado

a = 1
b = 2
c = 3
d = 999

resultado = d-c-b-a

print ("Resultado 1 : ", resultado)

# Flotantes: 15.2, 29.5, 18.28
# Luego divida sucesivamente del primero al último
# y almacénelo en una variable llamada resultado2

e = 15.2
f = 29.5
g = 18.28

resultado2 = (e/f)/g

print ("Resultado 2 : ", resultado2)


# Strings: "123", "Cristian"
# Luego sume ambas variables y determina si la
# opreación es posible, si es así almacénelo en una variable
# de su elección

h = "123"
i = "Cristian"

resultado3 = h+i

print ("Resultado 3 : ", resultado3)


####### Para pensar #######

# Busque una manera de convertir:
# un entero a un flotante

a = float (a)
print (a, " es del tipo : ", type(a) )

# un flotante a un entero

e = int (e)
print (e, " es del tipo : ", type(e) )

# un string a un entero y flotante

h = int (h)
print (h, " es del tipo : ", type(h) )

h = float (h)
print (h, " es del tipo : ", type(h) )

# un número a un string

a = str (a)
print (a, " es del tipo : ", type(a) )
