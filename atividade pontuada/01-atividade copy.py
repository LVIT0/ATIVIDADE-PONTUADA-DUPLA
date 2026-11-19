import os
os.system('cls' if os.name == 'nt' else 'clear')





saldo = 500


def saldos(saldo):
    print(f'Saldo: R$ {saldo}')
    return saldo


def calculo_soma(saldo, valor):
    print('Deposito realizado com sucesso! ')
    print(f'Resultado: R$ {calculo_soma(valor, saldo)}')


def calculo_subtracao(saldo, valor):
    resultado = saldo - valor
    return resultado

print('BANCO COFRINHO')
print(' ')
print('1 | VER SALDO ')
print('2 | DEPOSITAR ')
print('3 | SACAR ')
print('4 | VER EXTRATO ')
print('0 | SAIR ')

while True:
    opcao = input('\nEscolha a opção: ')

    match opcao:
        case '1':
            print('')
            input('Pressione enter para continuar')

        case '2':
            valor = float(input('Digite o valor que deseja depositar: '))

        case '3':
            valor = float(input('Digite o valor que deseja sacar: '))
            print('Saque realizado com sucesso! ')
            print(f'Resultado: R$ {calculo_subtracao(saldo, valor)}')






        case '0':
            input('Pressione enter para finalizar: ')
            print('Consulta finalizada com sucesso! ')
            break

        case _:
            print('Inválido, tente novamente')
            continue

