import os

print('------------------------------------------')
print('|                fackbook                |')
print('|----------------------------------------|')
print('|  1. Registrarion                       |')
print('|  2. Login                              |')
print('|  3. exit                               |')
print('|----------------------------------------|')
option = int(input('| Choose your option: '))
if option == 1:
    Reg = input('| Choose your name: ')
    Pass = input('| Choose your password: ')
    print('------------------------------------------')
    print('|             Please login:              |')
    print('------------------------------------------')
    a = input('| Choose your name: ')
    b = input('| Choose your password: ')
    if a == Reg and b == Pass:
        print('------------------------------------------')
        print(f'|             Welcome:{a}                ')
        print('------------------------------------------')
        os.system('py test.py')
    else:
        print('------------------------------------------')
        print(f'|         Wrong name or password         |')
        print('------------------------------------------')
        os.system('py test.py')

elif option == 2:
    logname = input('| Choose your name: ')
    logpass = input('| Choose your password: ')
    a1 = 'test'
    b2 = '1234'
    if a1 == logname and logpass:
        print('------------------------------------------')
        print(f'|             Welcome:{logname}         |')
        print('------------------------------------------')
        os.system('py test.py')
    else:
        print('------------------------------------------')
        print(f'|         Wrong name or password         |')
        print('------------------------------------------')
        os.system('py test.py')

elif option == 3:
    exit()

else:
    print('------------------------------------------')
    print('|             Wrong option               |')
    print('------------------------------------------')
    os.system('py test.py')