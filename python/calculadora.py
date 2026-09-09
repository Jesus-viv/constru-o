print('escolha uma opção desejada')

print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')

opcao = int(input('escolha uma operação desejada'))
numero1 =  float(input('primeiro numero'))
numero2 = float(input('segundo numero'))



match opcao:
    case 1:
        print(f' a soma é {numero1+numero2}')
    case 2:
            print(f' a Subtração é {numero1-numero2}')
    case 3:
            print(f' a Multiplicação é {numero1*numero2}')
    case 4:
            print(f' a Divisão é {numero1/numero2}')
    case _:
            print('opção invalida')
    