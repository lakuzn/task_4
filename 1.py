print("Введите имя студента.")
a = str(input())
print("Введите фамилию студента.")
b = str(input())
print("Введите год рождения студента")
c = int(input())
print(a,b,c,sep="_")
d = a
a = b
b = d
c = c + 60
print("Измененные данные:")
print(a,b,c,sep="_")
