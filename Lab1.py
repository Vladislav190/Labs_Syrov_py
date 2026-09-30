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
if m * n < 0: znak = '-' 
else: znak = '' 
t = m/n 
m,n = abs(m), abs(n)
now, i, proshl = 0, 0, 0
stepen = pow(10,a+10)
perevert = False

if m > n: m,n = n,m; perevert = True

while True:
    up_dr = (pow(-1,i) * pow(m,2*i+1)) *stepen
    down_dr = ((2*i + 1)*pow(n,2*i+1))
    
    now += int((up_dr//down_dr))
    if str(proshl)[:a] == str(now)[:a]: break
    i += 1
    proshl = now 

nul = (a+10) - len(str(now))
nach = int(str(int(math.pi*stepen))[:nul+1])

cel, drob = divmod(((int((math.pi/2)*stepen)) - now), stepen)

print(math.atan(t))
if perevert: print(f'{znak}{cel}.{str(drob)[:a]}')
else: print(znak + '0.' + '0'*nul + str(now)[:a-nul]) 
print(i)