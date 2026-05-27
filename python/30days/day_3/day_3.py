#Day 2: 30 days of python programming

edad = 24
altura = 1.78
num_complejo = 2+3j

#Area del triangulo
base_triangulo = int(input("Ingresa la base del triangulo: "))
altura_triangulo = int(input("Ingresa la altura del triangulo: "))
area = (base_triangulo * altura_triangulo) / 2
print("El area del triangulo es: ",area)

#Perimetro triangulo
a = int(input("Ingresa el lado a del triangulo: "))
b = int(input("Ingresa el lado b del triangulo: "))
c = int(input("Ingresa el lado c del triangulo: "))
perimetro = a + b + c
print("El perimetro del triangulo es: ",perimetro)

#Rectangulo
base_rectangulo = int(input("Ingresa la base del rectangulo: "))
altura_rectangulo = int(input("Ingresa la altura del rectangulo: "))
area_rectangulo = base_rectangulo * altura_rectangulo
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
print("El area del rectangulo es: ",area_rectangulo)
print("El perimetro del rectangulo es: ",perimetro_rectangulo)

#Circulo
pi = 3.14
radio = int(input("Ingresa el radio del circulo: "))
area = pi * (radio ** 2)
circunferencia = 2 * pi * radio
print("El area del circulo es: ",area)
print("La circunferencia del circulo es: ",circunferencia)

#Pendiente
m = 2
b = -2

y_intercept = (0,b)
x = (0-b)/m
x_intercept = (x,0)
print("La pendiente es: ",m)
print("La intersección con el eje y es: ",y_intercept)
print("La intersección con el eje x es: ",x_intercept)

#Ecuacion
p1=2
p2=2
q1=6
q2=10
distancia=((p1-q1)**2+(p2-q2)**2)**0.5
pendiente = (q2-p2)/(q1-p1)
print("La distancia entre los puntos es: ",distancia)
print("La pendiente de la recta que pasa por los puntos es: ",pendiente)
comparacion = m==pendiente
print("¿La pendiente de la recta es igual a la pendiente calculada? ",comparacion)

#Ecuacion 2
x1 = -3
y1 = (x1**2) + 6*x1 + 9
x2 = -5
y2 = (x2**2) + 6*x2 + 9
print("El valor de y para x = -3 es: ",y1)
print("El valor de y para x = -5 es: ",y2)

#palabras
print(len('python') != len('dragon'))  # False
print("I hope this course is not full of jargon", "jargon" in "I hope this course is not full of jargon")  # True
print("python and dragon", "on" in "python and dragon")  # True

palabra = "python"
length = len(palabra)
length_float = float(length)
length_str = str(length)
print("Length:", length)
print("As float:", length_float)
print("As string:", length_str)

num = 8
is_even = num % 2 == 0
print("Is the number even?", is_even)

resultado = (7//3) == int(2.7)
print("Es 7 dividido por 3 igual a 2.7?", resultado)

resultado_2 = type('10') == type(10)
print("¿El tipo de '10' es igual al tipo de 10?", resultado_2)
print(int(float('9.8')) == 10)

#Horas
horas = int(input("Ingresa el número de horas trabajadas: "))
pago = int(input("Ingresa el pago por hora: "))
salario = horas * pago
print("El salario semanal es: ",salario)


#años vividos
edad = int(input("Ingresa tus años vividos: "))
segundos_por_año = 365 * 24 * 60 * 60
print("Has vivido aproximadamente ", edad * segundos_por_año, " segundos.")

for i in range (1,6):
    print(i, 1, i**2, i**3)
    