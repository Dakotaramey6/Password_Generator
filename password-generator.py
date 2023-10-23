import random

password_chars = list('qwertyuiopasdfghjklzxcvbnm1234567890ASDFGHJKLQWERTYUIOPZXCVBNM')

def generate_password(): 
    password_length = input('How long is the password: ')
    count = int(password_length)
    length = 0
    password = 'Password is: '

    while length < count :
        password_number = random.randint(0, 61)
        password += password_chars[password_number]
        length+= 1

    print(password)


generate_password()

acceptable_password = input('Try another? Yes for new password or no/enter to skip ')


while acceptable_password == 'yes' or acceptable_password == 'Yes':
    generate_password()
    acceptable_password = input('Another try? ')

