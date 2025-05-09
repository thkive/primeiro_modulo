#soma: guarda o total das notas
soma = 0
#contador: conta quantas notas foram digitadas.
contador = 0
#O while continua pedindo notas até o usuário digitar uma negativa.
while True:
    nota = float(input("digite uma nova nota(ou valor negativo para sair): "))
#se o usuario digitar uma nota negativa para de rodar o codigo
    if nota < 0:
        break
    soma = soma + nota
# contador + 1 vai contando quantas notas foram digitadas pelo usuario
    contador = contador + 1
#Se tiver pelo menos uma nota válida, calcula a média.
if contador > 0:
    media = soma / contador
    print("A média das notas é: ", media)
else:
    print("Nenhuma nota valida foi digitada")
    