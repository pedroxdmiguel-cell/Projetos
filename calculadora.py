
num1 = 0
num2 = 0
result = 0
op     = ''

while True:
    num1 = float(input('Digite o primeiro núemro: '))
    num2 = float(input('Digite o primeiro núemro: '))
    op   = input('Digite a operação a ser feita: ')

    if op == ' ':
        result = num1 + num2
    elif op == '-':
         result = num1 - num2
    elif op == '/':
        result = num1 / num2
    elif op == '*':
        result = num1 * num2
    else:
        print("Comando não reconhecido")

    print('{} {} {} = {}' .format(num1, op, num2, result))

