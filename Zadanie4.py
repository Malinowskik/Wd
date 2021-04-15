# Zadanie 1
import numpy as np
print("Zadanie 1")
a = np.linspace(3, 45, 15) # poczatek 3, końcowa liczba 45, liczba powtórzeń
print(a)
print('\n')

# Zadanie 2
print("Zadenie 2")
b = np.arange(10, dtype='float') # tworzenie listy float
c = b.astype('int') # przypisanie wartości z listy 1 do 2 i zmiana na int
print(b)
print(b.dtype) # sprawdzenie typu danych
print(c)
print(c.dtype) #sprawdzenie typu danych
print('\n')

# Zadanie 3
'''print("Zadanie 3")
n = input("Wpisz liczbę całkowitą: ")
n = int(n)
d = np.arange(1, n*n+1)
print(d)
print('\n')

# Zadanie 4
print("Zadanie 4")
e = input("Podaj 1 parametr: ")
f = input("Podaj 2 parametr: ")
e = int(e)
f = int(f)
def g(p, l):
    k = np.logspace(1, l, num=l, base=p)
    return k

print(g(e,f))
print('\n')

# Zadanie 5
print("Zadanie 5")
g = input("Podaj długość wektora: ")
g = int(g)
def generate_vector(i):
    w = [x for x in range(i+1)]
    w = w[::-1]
    y = np.diag(w)
    return y
print((generate_vector(g)))
print('\n') '''

#Zad6
# malina = np.array(list('malina'))
# mrowka = np.array(list('mrówka'))
# armata = np.array(list('armata'))
# #armata = np.flip(armata)
#
# wykreslanka = np.zeros((6,6), dtype='str')
#
# print(wykreslanka)
#
# wykreslanka = np.diag(mrowka)
# wykreslanka[:, 0] = malina
# wykreslanka[5,::-1] = armata
# #wykreslanka[5,:] = armata
# print(wykreslanka)
# print("")
# # wykreslanka[:, 0] = mrowka
# # wykreslanka[5,::-1] = armata
# # for a in range(5):
# #     wykreslanka[a,a] = malina[a]
# # print(wykreslanka)

#zad7
# def zad7(n):
#     mat = np.diag([2 for _ in range(n)])
#     for indeks in range(1, n):
#         vec = [2+(2*indeks) for _ in range(n-indeks)]
#         mat += np.diag(vec, indeks)
#         mat += np.diag(vec, -indeks)
#     print(mat)
#
# zad7(3)
#zad7(3)
# def zad8(tab, kierunek='poziomo'):
#     print(tab)
#     if kierunek == 'poziomo':
#         # nieparzysta liczba wierszy
#         if tab.shape[0] % 2 != 0:
#             print("Tablica posiada nieprzystą liczbę wierszy")
#             return
#         p1 = tab[0:int(tab.shape[0]/2), :]
#         p2 = tab[int(tab.shape[0]/2):, :]
#         print("***** część 1 *****")
#         print(p1)
#         print("***** część 2 *****")
#         print(p2)
#     elif kierunek == "pionowo":
#         if tab.shape[1] % 2 != 0:
#             print("Tablica posiada nieprzystą liczbę kolumn")
#             return
#         p1 = tab[:, 0:int(tab.shape[1]/2)]
#         p2 = tab[:, int(tab.shape[1] / 2):]
#         print("***** część 1 *****")
#         print(p1)
#         print("***** część 2 *****")
#         print(p2)
#
# zad8(np.arange(36).reshape((6,6)), kierunek='pionowo')
#zad9
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
#
# macierz = np.arange(25).reshape((5,5))
# n = 1
# print(macierz)
# for a in range(5):
#     for b in range(5):
#         fibonaci = fibonacci(n)
#         macierz[a][b] = fibonaci
#         n += 1
#
# print(macierz)

