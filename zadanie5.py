import numpy as np

#Zad1
# a = np.array([1, 2, 3]) # tworzenie 1 macierzy 1x3
# b = np.array([4, 5, 6]) # druga macierz
# c = a * b #mnozenie
#
# print(c)

#Zad2
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #macierz 3x3
# b = np.array([[10, 11, 12, 13], [14, 15, 16, 18], [19, 20, 21, 22], [23, 24, 25, 26]]) #macierz 4x4
# print(a)
# print(b)
#
# print(a.min(axis=0)) # minimalna wartość z kolumn macierzy a
# print(a.min(axis=1)) # minimalna watość z wierszy macierzy a
# print(b.min(axis=0)) # minimalna wartość z kolumn macierzy b
# print(b.min(axis=1)) # minimalna watość z wierszy macierzy b

#Zad3
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# c = np.dot(a, b) #mnozenie macierzy za pomoca funkcji dot()
# print(a.dot(b)) # drugi sposób mnożenia (mniej kodu)
# print(c)
# print(a @ b) #trzeci sposób mnożenia macierzy

#Zad4
# a = np.array([3, 4, 5])
# b = np.linspace(1, 10, num=3) # start, stop, limit(domyślna wartość to 50)
# c = a * b
# print(c)

#Zad 5
# x = np.array([[64, 70], [40, 49],[8,12]])
# print(x)
# a = np.sin(x)
# print(a)

#Zad 6
# y = np.array([[22, 33], [54, 123], [6, 9]])
# b = np.sin(x)
# print(a)

#Zad 7
# z = np.add(a,b)
# print(z)

# #Zad8
# x = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for y in x:
#     print(y)
#     print("")

#Zad9
# a = np.array([[3, 7, 5], [6, 1, 9], [2, 7, 8]])
# for b in a.flat: # funkcja .flat spłaszcza macierz czyli sprowadza do pojedynczych wartości z  wiersza
#     print(b)
#     print("")

#Zad10
# m = np.arange(0,81,1).reshape(9,9) # tworzenie macierzy 9x9
# s = m.reshape(3,27) # .reshape(liczba wierszy, l kolumn)
# print(s)
#
# m2 = m.ravel() #spłaszczenie macierzy
# print(m2)

#Zad11
# a = np.arange(0,12,1)
# print(a)
# macierz_1 = a.reshape(3, 4)
# print(macierz_1)
# print(macierz_1.ravel())
# macierz_2 = macierz_1.reshape(4,3)
# print(macierz_2)
# print(macierz_2.ravel())
# macierz_3 = macierz_1.reshape(2,6)
# print(macierz_3)
# print(macierz_3.ravel())
