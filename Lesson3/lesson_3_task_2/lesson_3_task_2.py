from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "iPhone 13 Pro", "+79819649240")
phone2 = Smartphone("POCO", "X6 Pro", "+79828351051")
phone3 = Smartphone("Samsung", "Galaxy S23+", "+79817530754")
phone4 = Smartphone("Xiaomi", "14 Ultra", "+79894429480")
phone5 = Smartphone("Google", "Pixel 7 Pro", "+79035241398")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}.")