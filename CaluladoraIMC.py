num1 = float(input("Digite sua altura: "))
num2 = float(input("Digite seu peso: " ))

imc = (num1 * 2 ) / num2

if imc >= 18:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso normal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 35:
    print("Obesidade grau 1")
elif imc <= 39:
    print("Obesidade grau 2")
else:
    print("Obseidade grau 3")
