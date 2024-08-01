from address import Address
from mailing import Mailing

to_address = Address("125391", "Москва", "8 Марта", 16, 47)
from_address = Address("193521", "Тюмень", "Пикмана", 44, 97)
mailing = Mailing(to_address, from_address, 1500, "МТ2024")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartament} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartament}. Стоимость {mailing.cost} рублей.")