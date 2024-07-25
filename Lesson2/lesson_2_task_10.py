def bank():
    rate = 10
    a = int(input("Сколько хотите положить на вклад? ""\n""-> "))
    years = int(input("На сколько лет будет открыт вклад? ""\n""-> "))
    x = a*(1*rate)**years
    print("Вы получите", x, "рублей")
bank()