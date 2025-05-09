num1 = int(input("Digite um numero para calcular o fatoria: "))
contadaor = num1
fatorial = 1
#enquanto c que é o numero que o usuaria vai digitar for maior que 0
while contadaor > 0:
#mostre c que foi o numero digitado pelo usuario
# o end é usado para o codigo continuar na mesma linha 
    print(contadaor, end='')
#se o numero que o usuario digitou for maior que 1 coloque x para continuar a conta
    if contadaor > 1:
        print(" x ", end='')
#senao mostre = para mostrar o resultado da conta   
    else:
        print(" = ", end='')
# f =  1 multiplicado pelo numero digitado pelo usuario
# c = o numero digitado pelo usuario menos 1 
# assim a cada multiplicaçao ele vai tirando um numero
    fatorial = fatorial * contadaor
    contadaor = contadaor - 1
print(fatorial)

