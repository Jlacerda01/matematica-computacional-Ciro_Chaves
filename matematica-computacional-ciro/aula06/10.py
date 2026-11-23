from itertools import product

servidores = ['APP_1', 'APP_2', 'APP_3', 'APP_4']
bancos = ['DB_A', 'DB_B', 'DB_C']

rotas = set(product(servidores, bancos))
bloqueadas = {('APP_2', 'DB_B'), ('APP_3', 'DB_C')}
rotas_fil = rotas - bloqueadas

print("Rotas possíveis:")
for r in rotas:
    print(r)

print("Quantidade total:", len(rotas))

for j in rotas_fil:
    print(j)



