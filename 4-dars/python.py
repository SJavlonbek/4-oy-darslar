from collections import namedtuple

Telfon=namedtuple('Telfon','phone_model, phone_year,phone_price')

Telfon1=["Samsung S22 ultra",2022, 500]
Telfon2=["Iphone 14 max",2023,1000]
print(Telfon._make(Telfon1))
print(Telfon._make(Telfon2))