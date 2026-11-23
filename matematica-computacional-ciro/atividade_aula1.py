# Dados de log brutos
log_bruto_frontend = [101, 102, 103, 104, 105, 101, 102, 103]
log_bruto_backend = [103, 104, 106, 107, 108, 103, 106]
log_bruto_devops = [103, 105, 108, 109, 110, 109, 103]

# 1. Transformar listas em conjuntos para eliminar duplicatas
frontend = set(log_bruto_frontend)
backend = set(log_bruto_backend)
devops = set(log_bruto_devops)

print("Conjunto Frontend:", frontend)
print("Conjunto Backend:", backend)
print("Conjunto DevOps:", devops)

# 2. Usuários Fullstack (intersecção entre Frontend e Backend)
users_fullstack = frontend & backend
print("\nUsers Fullstack (Front & Back):", users_fullstack)

# 3. Usuários que NÃO estão no Frontend (União de Back e DevOps minus Frontend)
users_no_front = (backend | devops) - frontend
print("Users sem Frontend:", users_no_front)

# 4. Usuários EXCLUSIVAMENTE Frontend (Diferença de conjuntos)
users_xor_front = frontend - (backend | devops)
print("Users exclusivamente Frontend:", users_xor_front) 

#+------++-+-+-+--------+-++-+-----------+-+-+-+-+------------------+-+-+-+-+-+-+

# Status inicial: Servidor 3 e Servidor 1 ativos (101 em binário = 5 em decimal)
status_servidores = 0b101

# 1. Máscara de bits para ativar o Servidor 2 (posição do segundo bit = 0b010 ou 1 << 1)
mascara = 0b010

# Exibição antes da modificação
print(f"Status Antes:  {bin(status_servidores)} (Decimal: {status_servidores})")

# Aplicação do Bitmask (Operador OR '|' para SETAR o bit do servidor 2)
status_servidores_atualizado = status_servidores | mascara

# Exibição depois da modificação
print(f"Status Depois: {bin(status_servidores_atualizado)} (Decimal: {status_servidores_atualizado})")

# Verificação com a condicional if (Operador AND '&' para checar a flag)
if (status_servidores_atualizado & mascara) == mascara:
    print("\n[VERIFICAÇÃO]: O Servidor 2 foi ativado com sucesso! Todos os 3 servidores estão operacionais.")
else:
    print("\n[VERIFICAÇÃO]: O Servidor 2 permanece offline.")