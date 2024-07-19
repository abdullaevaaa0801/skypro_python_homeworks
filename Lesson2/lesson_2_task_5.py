def month_to_season(number_of_month):
    number_of_month = int(input("Введите число месяца:"))
    if number_of_month in [12,1,2]:
        return "Winter"
    if number_of_month in [3,4,5]:
        return "Spring"
    if number_of_month in [6,7,8]:
        return "Summer"
    if number_of_month in [9,10,11]:
        return "Autumn"
print(month_to_season("number_of_month"))