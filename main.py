# Vamos a realizar una calculadora en Python / Let's make a calculator in Python. 
number1 = int(input("Por favor ingresa el primer numero/Please enter the first number: "))
operator = input("Por favor ingresa el operador/Please enter the operator: ")
number2 = int(input("Por favor ingresa el segundo numero/Please enter the second number: "))

if operator == "+":
  result = number1 + number2
elif operator == "*":
  result = number1 * number2
elif operator == "/":
  result = number1 / number2
elif operator == "-":
  result = number1 - number2
elif operator == "%":
  result = "Operador no soportador/Operator not supported"
  
print(result)