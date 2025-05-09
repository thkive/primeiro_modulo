n = int(input("Digite quntos numeros quer ver: "))
t1 = 0
t2 = 1
# vai mostrar o primeiro e segundo numero que sempre vai ser 0 e 1
print('{} -> {}'.format(t1, t2), end='')
contador = 3
# 
while contador <= n:
# t3 sempre vai ser a soma do primeiro com o segundo numero
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
# a medida que for somando o t1 e t2 vao mudando de lugar 
# e avançando a medida que a soma for aumentando
    t1 = t2
    t2 = t3
    contador = contador + 1
print(" Acabou")
