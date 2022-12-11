#Hay un fallo y no lee todo el cógido relacionado con el Elenco
#Aparece Signal:Killed 

#1
import pandas as pd

#2
titulos = pd.read_csv('imdb_titulos.csv')
print(titulos.head(5))

#3
#elenco = pd.read_csv('imdb_elenco.csv')
#print(elenco.head(5))

#4
registros_titulos=len(titulos.axes[0])
print(registros_titulos)

#5
#registros_elenco=len(elenco.axes[0])
#print(registros_elenco)

#6
print(titulos.nsmallest(5,'year'))

#7
#df = pd.read_csv('imdb_elenco.csv')
#df = df[df['title'].str.contains('Dracula')]
#print(df)
#print(df['title'].count())

#8
print(titulos.title.value_counts().head(10))
#print(elenco.title.value_counts().head(10))

#9
Romeo_Julieta = titulos[titulos['title'] == 'Romeo and Juliet']
print(Romeo_Julieta.sort_values(by='year').head(1))

#10
Exorcista = titulos[titulos.title.str.contains('Exorcist')].sort_values(by='year')
print(Exorcista)

#11
print(titulos[titulos['year'] == 1950].count())
#print(elenco[elenco['year'] == 1950].count())

#12
print(titulos[(titulos.year >= 50) & (titulos.year <= 1959)].count())
#print(elenco[(elenco.year >= 50) & (elenco.year <= 1959)].count())

#13
#rol1 = titulos[titulos.title == "The Godfather"]
#print(rol1)
#rol2 = roles_titulos1.iloc[:,4]
#print(rol2)
#rol3 = roles_titulos2.value_counts()
#print(rol3)


#14
#print(elenco[(elenco.title == "Dracula") & (elenco.year == 1958)].sort_values(by='n'))

#15
#print(titulos[titulos.character == "Bruce Wayne"].count())
#print(elenco[elenco.character == "Bruce Wayne"].count())

#16
#print(titulos[titulos.name == "Robert De Niro"].count())
#print(elenco[elenco.name == "Robert De Niro"].count())

#17
#protagonista_titulos = titulos[(titulos.name == "Charlton Heston") & (titulos.n == 1) & (titulos.year >= 1960) & (titulos.year <= 1969)].sort_values(by='year', ascending=False)
#print(protagonista_titulos)
#protagonista_elenco = elenco[(elenco.name == "Charlton Heston") & (elenco.n == 1) & (elenco.year >= 1960) & (elenco.year <= 1969)].sort_values(by='year', ascending=False)
#print(protagonista_elenco)

# 18
#print(titulos[(titulos.type == "actor") & (titulos.year >= 1950) & (titulos.year <= 1959)].count())
#print(elenco[(elenco.type == "actor") & (elenco.year >= 1950) & (elenco.year <= 1959)].count())

# 19
#print(titulos[(titulos.type == "actress") & (titulos.year >= 1950) & (titulos.year <= 1959)].count())
#print(elenco[(elenco.type == "actress") & (elenco.year >= 1950) & (elenco.year <= 1959)].count())




