def encode(user_in):  # Created by Ian Cabrera
    output = ''
    for char in user_in:
        add = int(char) + 3
        if add >= 10:
            add -= 10
        output += str(add)
    return output

def decode(user_in):
    pass     # FIXME


if __name__=='__main__':  # Created by Ian Cabrera
    password = ''
    while True:
        print("Menu\n-------------")
        print('1. Encode\n2. Decode\n3. Quit')
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            user_pass = input('Please enter your password to encode: ')
            password = encode(user_pass)
            print('Your password has been encoded and stored!\n')
        elif user_input == 2:
            decoded_pass = decode(password)
            print(f'The encoded password is {password}, and the original password is {decoded_pass}.\n')
        elif user_input == 3:
            break