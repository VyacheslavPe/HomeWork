from address import Address
from mail import Mailing

to_address = Address("420008", "Казань", "Кремлёвская", "18", "101")
from_address = Address("109012", "Москва", "Ильинка", "3/8 с 5", "101")
cost = 100
track = "1234567890"
mailing = Mailing(to_address, from_address, cost, track)

print("Отправление " + mailing.track + " из " + mailing.from_address.index + ", " + mailing.from_address.city + ", " + mailing.from_address.street + ", " + mailing.from_address.house + " - " + mailing.from_address.apartment + " в " + mailing.to_address.index + ", " + mailing.to_address.city + ", " + mailing.to_address.street + ", " + mailing.to_address.house + " - " + mailing.to_address.apartment + ". " + "Стоимость " + mailing.cost + " рублей.")