#1)argtg рационального числа приближаем к рациональным числом
#Приближаем полиномом argt(1/2)
#На вход поступает: точность, аргумент(m/n) - ввоядт через пробел
#Разложение рациональных чисел Макларена 
#Роман
#2)a^n x^n

''' Ввод
Точность
m n
'''
''' Вывод
arctg - через math
приближение (мое значение)
кол-во членов
'''


#2) BD апроксимация для artg

import math
a = int(input("Введите точность "))
m,n = map(int,input("Введите члены m n через пробел: ").split())
grad = 0
i = 0
proshl = 0
while True:
    
    grad += ((pow(-1,i) * pow(m,2*i+1)) / ((2*i + 1)*pow(n,2*i+1)))

    prov = int(grad)
    prov1 = list(str(grad-prov).split('.'))
    chisl = str(prov1[1])
    now = chisl[0:a:1]
    #print(now, proshl)
    if proshl == now:
        break
    i += 1
    proshl = now
t = m/n
etalon = math.atan(t)
print(etalon)
print(f'{int(grad)}.{chisl[0:a:1]}')# Учитывать отрицательные числа
print(i)


