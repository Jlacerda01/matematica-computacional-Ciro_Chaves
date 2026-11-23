linhas = 5
colunas = 5

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = 0
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)    
# linhas  = 5
# colunas = 5

# matriz_zeros = [[0 for j in range(colunas)] for i in range(linhas)]
# print(matriz_zeros)