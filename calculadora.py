def potencia(num1, num2):
    total = num1 ** num2
    return total
    
def raiz(num1, num2):
    total = num1 * (1/num2)
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
    

print('                           Calculadora')
print('')
print('                                 Menu')
print('------------------------------------------------------------------')
print('|                            1 -> Soma                           |')
print('|                            2 -> Subtração                      |')
print('|                            3 -> Multiplicação                  |')
print('|                            4 -> Divisão                        |')
print('|                                                                |')
print('|                            0 -> Sair                           |')
print('------------------------------------------------------------------')
opcao = int(input('Operação: '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if opcao == 1:
    resultado = soma(num1, num2)
    print(f'{num1} + {num2} = {resultado:.2f}')

elif opcao == 2:
    resultado = subtracao(num1, num2)
    print(f'{num1} - {num2} = {resultado}')

elif opcao == 3:
    resultado = multiplocacao(num1, num2)
    print(f'{num1} * {num2} = {resultado}')

elif opcao == 4:
    resultado = multiplicacao(num1, num2)
    print(f'{num1} + {num2} = {resultado}')
elif opcao == 0:
    resultado = raiz(num1, num2)
    print(f'{num2}  ✓  {num1} = {resultado}')
#    print('Obrigado por usar nossos sistemas!')
#    print('Volte sempre!')
 #   break

#if opcao == 0:
 #   print(f'Obrigado por usar nossa aplicação!')
#break
#resultado = potencia(num1, num2)
#print(resultado)