import pandas as pd
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

titanic = pd.read_csv(url)
print(titanic.shape)

titanic.head()

#titanic.info()

df = pd.DataFrame(titanic)
s = df['Survived'] == 1

sobreviventes = df[s]
print(f' Total de sobreviventes', s.sum())