# Napisane przez p. mgr R. Cybulskiego, przeanalizowałem zadania
import pandas as pd
import xlrd
import openpy

# zad1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.rea
d_excel(xlsx, header=0)
print(df)

#zad2
print(df[df['Liczba'] > 1000])

print(df[df['Imie'] == 'RADOSŁAW'])

print(df.agg({'Liczba': ['sum']}))

print(df[(df.Rok > 2006)].agg({'Liczba': ['sum']}))

print(df.groupby(['Plec']).agg({'Liczba': ['sum']}))

#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok','Plec']).nth(0))
new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(new_df, start=1):
    print(f"{index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end='')
    print(f" {group[1].iloc[0]['Liczba']}")

print("Chłopiec")
print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'),
                                                                                      ascending=False).iloc[0])
print("Dziewczynka")
print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                       ascending=False).iloc[0])
#zad3
df = pd.read_csv("zamowienia.csv", header=0, sep=';', decimal=".")
print(df)

print(df['Sprzedawca'].unique())

print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])

print(df.groupby(['Sprzedawca']).size())

print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))

print(df[((df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') &
              (df['Kraj'] == 'Polska'))].agg({'Utarg':['sum']}))

# możemy również oprócz zwracania określonej liczby wierszy Series lub DataFrame zwrócić określony fragment samego
# wiersza, np. stringa. Tutaj dla każdego wiersze z kolumny 'Data zamowienia' zwracane są 4 pierwsze znaki czyli
# wartość roku
print(df[((df['Data zamowienia'].str[:4] == '2004'))]['Utarg'].mean())

# stosując tę samą technikę filtrujemy dane dla wyznaczonych lat
rok_2004 = df[((df['Data zamowienia'].str[:4] == '2004'))]
rok_2005 = df[((df[ 'Data zamowienia'].str[ :4 ] == '2005'))]
rok_2004.to_csv("zamowienia_2004.csv", sep=';', index=False)
rok_2005.to_csv("zamowienia_2005.csv", sep=';', index=False)
