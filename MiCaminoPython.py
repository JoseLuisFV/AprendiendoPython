# Se pueden ingresar nuevas variables a la lista hay varais formas
# Si queremos agregar una nueva solamente utilizamos append
numbers = [99, 123, 2313, 1, 1231411, 343, 435345]
numbers.append(111)
print(numbers)
# Podemos usar insert para especificar donde lo colocamos, y eso hace que se
# desplacen las otras variables a otras posiciones
numbers.insert(2, 999)
print(numbers)

# Para Eliminar una varaible de la lista podemos usar remove, si hay mas de una
# variable que tenga el mismo valor entonces solo se borra la primera que
# tenga dicho valor
numbers.remove(1)
print(numbers)

# Si queremos acomodar nuestra lista podemos usar sort, este acomodo sera de
# manera ascendent
numbers.sort()
print(numbers)

# Podemos darle la vuelta a las posiciones que la ultima sea la primera,
# la penultima sera la segunda y asi sucesivamente
numbers.reverse()
print(numbers)

# Con el metodo pop que quita la variable de la ultima posiscion
numbers.pop()
print(numbers)

# Podemos limpiar la lista con clear
numbers.clear()
print(numbers)
