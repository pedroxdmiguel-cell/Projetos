num1 = float(input("Insira a 1 nota: "))
num2 = float(input("Insiara a 2 nota: "))
num3 = float(input("Insiara a 3 nota: "))

media = (num1 + num2 + num3) / 3

if media >= 7:
    print("ALuno passou")
elif media >= 5:
    print("Aluno precisa de recuperação")
else:
    print("Aluno reprovou")