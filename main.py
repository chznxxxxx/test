class Person1:
    adress = '14565'
    country = 'Ukraine'
    city = 'kharkiv'

class Person2:
    adress = '99704'
    country = 'Poland'
    city = 'varshava'

class Person3:
    adress = '54523'
    country = 'USA'
    city = 'New York'


print('ok')

    print(Person1.adress)
    print(Person2.city)
    print(Person3.country)
Pr1 = Person1()
print(Pr1.adress)
Pr2 = Person2()
print(Pr2.adress)
Pr2.adress = '99704'
print(Pr1.adress)
print(Pr2.adress)
print(Pr1.city)
print(Pr2.city)
Pr3 = Person3()
print(Pr3.adress)
Pr3.adress = '54523'
print(Pr3.city)