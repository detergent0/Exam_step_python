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

#Задание 7
def arip(a):
    sum=0
    for i in a:
        sum+=i
    arif=sum/len(a)
    print(f"Сумма всех чисел: {sum}, среднее арифметическое: {arif}")
arip([1,2,3])