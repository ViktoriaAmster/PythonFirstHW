# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

quaterList = ['(x>0,y>0)', '(x<0,y>0)', '(x<0,y<0)', '(x>0,y<0)']
quarter = int(input("Введите номер четверти: "))
while (quarter < 1) or (quarter > 4):
    quarter = int(input("Номер четверти может быть от 1 до 4 "))

print(quaterList[quarter-1])