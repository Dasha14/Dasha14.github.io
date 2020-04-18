import random  # добовления библиотеки 
#print(5)
#print(5+5)
#print("Hello")  # ввывод строки на экран 
#print("Hello "+"World")
#name="dasha" # переменная
#print(name)
#name=input("ввидите ваше имя ")  # ввод даных с клавиатуры 
#print(name)
secret=random.randint(1,10)  # генерация случайного числа
attempts = 3
while attempts > 0:  # цыкл, исполняется пока условие верное
    user=input("ввидите число")
    user=int(user)  # обращение в числовой вид
    #print(secret,user)
    if secret > user:  # сравнение переменных
        print("секретное число больше")
    if secret < user:
        print("секретное число меньше")
    if secret == user:
        print("ты победил")
        break  # остоновка цыкла
    attempts= attempts - 1
