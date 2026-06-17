#Задание 1
sum=0
a=int(input("Введите число(больше одного): "))
if a<=1:
    print("я же написал больше одного")
else:
    for i in range(1,a):
        sum+=i
    print(f"сумма от 1 до {a}: {sum}")

#Задание 2
for i in range(1, 11):
    print(f"{i}*3={i*3}")

#Задание 3
sqr=1
N=int(input("Введите число(больше одного): "))
if N<=1:
    print("я же написал больше одного")
else:
    while sqr<N:
        print(f"квадрат {sqr}={sqr**2}")
        sqr+=1

#Задание 4
sum=0
while True:
    a=int(input("Введите число(0 заканчивает цикл): "))
    sum+=a
    if a==0:
        print(f"сумма всех чисел: {sum}")
        break

#Задание 5
a=[1,2,3,4,5,6,7,8,9,10]
print(sum(a))

#Задание 6
a=[1,-2,3,4,-5,-6,-7,8,-9,10]
neg=0
pos=0
for i in a:
    if i<0:
        neg+=1
    else:
        pos+=1
print (f"положительных: {pos}, отрицательных: {neg}")

#Задание 7
def arip(a):
    sum=0
    for i in a:
        sum+=i
    arif=sum/len(a)
    print(f"Сумма всех чисел: {sum}, среднее арифметическое: {arif}")
arip([1,2,3])

#Задание 8
from math import sqrt, pi
def area (a,b):
    match(b):
        case("квадрат"):
            return a**2
        case("треугольник"):
            return a**2*sqrt(3)/4
        case("круг"):
            return pi*(a**2)
print (area(4,"квадрат"))
print (area(4,"треугольник"))
print (area(4,"круг"))