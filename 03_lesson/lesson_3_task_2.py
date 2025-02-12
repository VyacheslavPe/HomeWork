from smartphone import Smartphone

smartphone1 = Smartphone("Apple", "IPhone 3G", "+79000000000")
smartphone2 = Smartphone("Apple", "IPhone 4", "+79111111111")
smartphone3 = Smartphone("Apple", "IPhone 12", "+79222222222")
smartphone4 = Smartphone("Samsung", "Galaxy s24", "+79333333333")
smartphone5 = Smartphone("Huawei", "Honor 10i", "+79444444444")

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

i=0
while i < len(catalog):
    print(catalog[i].brand, catalog[i].model, catalog[i].number)
    i += 1