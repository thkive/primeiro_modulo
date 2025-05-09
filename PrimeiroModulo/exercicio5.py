num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
par = 0

for contador in range (num1, num2):
    if contador % 2 == 0:
        par = par + 1
        print(contador)
print("A quantidade de numero par é: ", par)
