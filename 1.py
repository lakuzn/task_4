print("Введите имя студента.")
a = str(input())
print("Введите фамилию студента.")
b = str(input())
print("Введите дату рождения студента.")
c = str(input())
print(a+"_"+b+"_"+c)
d = a
a = b
b = d
c = c + "60"
print("Измененные данные:")
print(a+"_"+b+"_"+c)