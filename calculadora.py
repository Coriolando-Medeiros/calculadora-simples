def potencia(num1, num2):
    total = num1 ** num2
    return total
    
def raiz(num1, num2):
    total = num1 ** (1/num2)
    return total
    
def soma(num1, num2):
    total = num1 + num2
    return total
    
def subtracao(num1, num2):
    total = num1 - num2
    return total
    
def multiplicacao(num1, num2):
    total = num1 * num2
    return total
    
def divisao(num1, num2):
    total = num1/num2
    return total

def entradas():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    return num1, num2

def menu_principal():
    print('')
    print('                           Calculadora')
    print('')
    print('                                Menu')
    print('------------------------------------------------------------------')
    print('|                                                                |')
    print('|                            1 -> Calc. Científica               |')
    print('|                            2 -> Calc. Padrão                   |')
    print('|                                                                |')
    print('|                            0 -> Sair                           |')
    print('------------------------------------------------------------------')
    print('')

def menu_cient():
    print('')
    print('                           Calculadora Científica')
    print('')
    print('                                Menu')
    print('------------------------------------------------------------------')
    print('|                                                                |')
    print('|                            1 -> Soma                           |')
    print('|                            2 -> Subtração                      |')
    print('|                            3 -> Multiplicação                  |')
    print('|                            4 -> Divisão                        |')
    print('|                            5 -> Raiz quad.                     |')
    print('|                            6 -> Potência                       |')
    print('|                                                                |')
    print('|                            0 -> Sair                           |')
    print('------------------------------------------------------------------')
    print('')

def menu_padrao():
    print('')
    print('                           Calculadora Padrão')
    print('')
    print('                                Menu')
    print('------------------------------------------------------------------')
    print('|                                                                |')
    print('|                            1 -> Soma                           |')
    print('|                            2 -> Subtração                      |')
    print('|                            3 -> Multiplicação                  |')
    print('|                            4 -> Divisão                        |')
    print('|                                                                |')
    print('|                            0 -> Sair                           |')
    print('------------------------------------------------------------------')
    print('')
    
while True:
    menu_principal()
    opcao = int(input('Operação: '))
    if opcao == 1:
        while True:
            menu_cient()
            opcao = int(input('Operação: '))
            if opcao == 1:
                num1, num2 = entradas()
                resultado = soma(num1, num2)
                print(f'{num1} + {num2} = {resultado:.2f}')
                input('Pressione ENTER para continuar...')

            elif opcao == 2:
                num1, num2 = entradas()
                resultado = subtracao(num1, num2)
                print(f'{num1} - {num2} = {resultado}')
                input('Pressione ENTER para continuar...')

            elif opcao == 3:
                num1, num2 = entradas()
                resultado = multiplicacao(num1, num2)
                print(f'{num1} * {num2} = {resultado}')
                input('Pressione ENTER para continuar...')

            elif opcao == 4:
                num1, num2 = entradas()
                resultado = divisao(num1, num2)
                print(f'{num1} / {num2} = {resultado}')
                input('Pressione ENTER para continuar...')
                
            elif opcao == 5:
                num1 = float(input('Digite o número: '))
                num2 = float(input('Digite o expoente da raiz: '))
                resultado = raiz(num1, num2)
                print(f'{num1} √ {num2} = {resultado}')
                input('Pressione ENTER para continuar...')
                
            elif opcao == 6:
                num1 = float(input('Digite a base: '))
                num2 = float(input('Digite o expoente da potência: '))
                resultado = potencia(num1, num2)
                print(f'{num1} ^ {num2} = {resultado}')
                input('Pressione ENTER para continuar...')
                
            elif opcao == 0:
                print('Voltando para menu principal')
                break
            else:
                print('Opção inválida! Tente novamente.')
    elif opcao ==2:
            while True:
                menu_padrao()
                opcao = int(input('Operação: '))
                if opcao == 1:
                    num1, num2 = entradas()
                    resultado = soma(num1, num2)
                    print(f'{num1} + {num2} = {resultado:.2f}')
                    input('Pressione ENTER para continuar...')

                elif opcao == 2:
                    num1, num2 = entradas()
                    resultado = subtracao(num1, num2)
                    print(f'{num1} - {num2} = {resultado}')
                    input('Pressione ENTER para continuar...')

                elif opcao == 3:
                    num1, num2 = entradas()
                    resultado = multiplicacao(num1, num2)
                    print(f'{num1} * {num2} = {resultado}')
                    input('Pressione ENTER para continuar...')

                elif opcao == 4:
                    num1, num2 = entradas()
                    resultado = divisao(num1, num2)
                    print(f'{num1} / {num2} = {resultado}')
                    input('Pressione ENTER para continuar...')
                    
                elif opcao == 5:
                    num1 = float(input('Digite o número: '))
                    num2 = float(input('Digite o expoente da raiz: '))
                    resultado = raiz(num1, num2)
                    print(f'{num1} √ {num2} = {resultado}')
                    input('Pressione ENTER para continuar...')
                    
                elif opcao == 0:
                    print('Voltando para menu principal')
                    break
                else:
                    print('Opção inválida! Tente novamente.')
    elif opcao == 0:
        print('Obrigado por usar nossos sistemas!')
        print('Volte sempre!')
        break
    else:
        print('Opção inválida! Tente novamente.')