def bank():
    rate = 0.1
    a = int(input("Сколько хотите положить на вклад? "))
    years = int(input("На сколько лет будет открыт вклад? "))
    x = a*(1*rate)**years
    print("Вы получите", x, "рублей")
bank()