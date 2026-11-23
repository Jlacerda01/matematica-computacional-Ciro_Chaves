import pandas as pd

dados = {
    'nome': ['ana', 'Bruno', 'Carla', "Juliano"],
    'idade' : [22,25,19]
}


df = pd.DataFrame(dados)

print(df)