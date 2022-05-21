import math


import math

x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = round(math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2), 2)
print(distance)

# Если брать первый пример: А(3, 6) и В(2, 1), то результат получается 5,099...
# При округлении до 2 знаков после запятой результат будет 5,1, а не 5,09.
# То есть если исходить из примеров, то необходимо окргулить вниз до двух знаков после запятой
# Готового функционала в Python для этого нет
# Поэтому, как вариант возможно, следующее решение:

# distance = math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2)
# distance = int(distance * 100)
# distance = float(distance/100)

# В таком виде программа будет округлять, как в примере.
# Но не уверен, что в задании именно это подразумевалось, поэтомуоставляю это только в комментариях