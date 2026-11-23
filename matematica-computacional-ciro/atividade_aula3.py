
usuarios = ["Alice", "Bob", "Clara", "David", "Zeca"]

filmes = ["Matrix", "Inception", "Avatar"]
matriz = []
linhas = len(usuarios)
colunas = len(filmes)
for i in range(linhas):
    linha = [0] * colunas
    matriz.append(linha)

for linha in matriz:
    print(linha)

assistidos = [
    ("Alice", "Matrix"),
    ("Alice", "Inception"),
    ("Bob", "Avatar"),
    ("Clara", "Matrix"),
    ("Clara", "Avatar"),
    ("David", "Inception")
]
for usuario, filme in assistidos:
    print(usuario,filme)
    linha = usuarios.index(usuario)
    coluna = filmes.index(filme)
    print(linha,coluna)
    matriz[linha][coluna] = 1
for linha in matriz:
    print(linha)


linha_clara = usuarios.index('Clara')
linha = matriz[linha_clara]
contador = 0
for i in linha:
    if i == 1:
        contador += 1
print(f'clara assistiu um total de {contador} de filmes')

coluna_matrix = filmes.index("Matrix")

contador = 0

for i in range(linhas):

    if matriz[i][coluna_matrix] == 1:
        contador += 1

print(f'A audiência total acumulada pelo filme "Matrix" = {contador}')

for i in range(linhas):
    contador = 0

    for valor in matriz[i]:
        if valor == 1:
            contador += 1
    if contador == 0:
        usuarios[i]
        print(f'ALERTA: Usuário {usuarios[i]} Inativo.')  