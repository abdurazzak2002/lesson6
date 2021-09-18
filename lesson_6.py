#Кортеж - tuple 
# products = ('milk', 'orange', 'apple')
# for product in products:
#     print(product)

#print(products[::2])


# users = ['Ahmed', 'Askar', 'admin2', 'admin']
# for user in users:
#     if user == 'admin':
#         print('Welcom! Admin')

# users = ['Ahmed', 'Askar', 'admin2', 'admin']
# baned_users = ['ahmed', 'Jonh']
# user= input('please enter your name: ')
# if user in baned_users:
#     print('you are baned')
# else:
#     password = input('please enter you password: ')
#     if password == 'qwerty':
#         print('Welcom')
#     else:
#         print('не правильный пароль')

#    != - не равно 


number = int(input('Enter random number: '))
while number == 42:
    if number != 42:
        print('это не сорок два')
    else:
        print('это сорок два')
    pass
