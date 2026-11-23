# ==========================================
# 1. GERAÇÃO DA MATRIZ BOOLEANA
# ==========================================

# Domínio S
S = [0, 1, 2, 3]
n = len(S)

# Definição da relação exemplo
relacao = [
    (0, 0), (0, 1), (0, 3),
    (1, 0), (1, 1),
    (2, 2),
    (3, 0), (3, 3)
]

# Inicializando a matriz quadrada n x n com zeros
matriz = [[0] * n for _ in range(n)]

#Criando matriz Booleana se par ordenado está na relação
for x, y in relacao:
    matriz[x][y] = 1

print("--- Matriz Booleana Gerada ---")
for linha in matriz:
    print(linha)
print("\n")

# ==========================================
# 2. FUNÇÕES DE AUDITORIA E VERIFICAÇÃO
# ==========================================

def verifica_reflexiva(M, n):
    for i in range(n):
        if M[i][i] == 0:
            return False
    return True

def verifica_simetrica(M, n):
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] != M[j][i]:
                return False
    return True

def verifica_anti_simetrica(M, n):
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] == 1 and M[j][i] == 1:
                return False
    return True

def verifica_transitiva(M, n):
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0:
                continue
            for k in range(n):
                if M[j][k] == 1 and M[i][k] == 0:
                    return False
    return True

# ==========================================
# 3. RELATÓRIO FINAL
# ==========================================
# print("--- Relatório de Auditoria e Verificação ---")
# print(f"Reflexiva: {verifica_reflexiva(matriz, n)}")
# print(f"Simétrica: {verifica_simetrica(matriz, n)}")
# print(f"Anti-simétrica: {verifica_anti_simetrica(matriz, n)}")
# print(f"Transitiva: {verifica_transitiva(matriz, n)}")

# Sistema Alpha
matriz_alpha = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

# Sistema Beta
matriz_beta = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Sistema Gama
matriz_gama = [
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
]


sistema =  [
    ("Sistema Alpha", matriz_alpha),
    ("sistema Beta", matriz_beta),
    ("sistema Gama", matriz_gama)
]

for nome, M in sistema:
    n= len(M)
    ref = "APROVADO" if verifica_reflexiva(M, n) else "FALHA"
    sim = "APROVADO" if verifica_simetrica(M, n) else "FALHA"
    antsim = "APROVADO" if verifica_anti_simetrica(M, n) else "FALHA"
    transi = "APROVADO" if verifica_transitiva(M, n) else "FALHA"

    print(f"\n--- {nome} ---")
    print(f"Reflexiva: {ref}")
    print(f"Simétrica: {sim}")
    print(f"Anti-simétrica: {antsim}")
    print(f"Transitiva: {transi}\n")

#Etapa 1: Definir o conjunto S e criar a matriz zerada

S = [1, 2, 3, 4, 6, 8, 12, 24]

numS = len(S)

linhas = 8
colunas = 8

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = 0
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)    

for i in range(numS):
    x = S[i]
    for j in range(numS):
        y = S[j]
        if y % x == 0 :
            matriz[i][j] = 1    
print("\n--- Matriz dos Servidores Preenchida ---")
for linha in matriz:
    print(linha)            

#Chamar funçoes de auditoria

is_ref = verifica_reflexiva(matriz, numS)

is_sim = verifica_simetrica(matriz, numS)

is_anti = verifica_anti_simetrica(matriz, numS)

is_trans = verifica_transitiva(matriz, numS)

if is_ref and is_sim and is_trans:
    print('[ALERTA] Relação de Equivalência detectada. Risco de loop infinito na rede.')
elif is_ref and is_anti and is_trans :
    print('[OK] Ordem Parcial validada. Hierarquia de roteamento segura.')
else:
    print('[ERRO] Topologia inconsistente.')    