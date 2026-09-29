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
now = 0
i = 0
proshl = 0
stepen = pow(10,a+10)
while True:
    
    up_dr = (pow(-1,i) * pow(m,2*i+1)) 
    down_dr = ((2*i + 1)*pow(n,2*i+1))
    now += int((up_dr/down_dr)*stepen)
    if str(proshl)[:a] == str(now)[:a]: break
    i += 1
    proshl = now
t = m/n 

print(math.atan(t))
print('0.' + str(now)[:a])# Учитывать отрицательные числа
print(i)


