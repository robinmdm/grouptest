

users = dict()


def manage_hobbies():
    print('----------------------------------------------------------------')
    print('User Dictionary...   ')
    print('----------------------------------------------------------------')
    print('1 : Add New Person')
    print('2 : Remove Person')
    print('3 : View All')
    print('4 : View Hobbies')
    print('q : Quit')
    print('----------------------------------------------------------------')
    return input('Select Option : ')


exit = True

while exit:

    option = manage_hobbies()

    print('----------------------------------------------------------------')

    if option.isdigit() and int(option) == 1:

        nameHobby = input(
            'Enter a name and hobby separated by a comma: ').split(',')

        if isinstance(nameHobby, str):
            print('Inputs are not string')
        else:
            users[nameHobby[0].lower()] = nameHobby[1].lower()

    elif option.isdigit() and int(option) == 2:

        name = input('Enter a name to remove: ')
        users.pop(name.lower())

    elif option.isdigit() and int(option) == 3:

        print('\nPeople in the list: \n')

        for i in users.keys():
            print(i +
                  ': ' + users.get(i))

        print('\n')

    elif option.isdigit() and int(option) == 4:

        print('\nHobbies in the list: \n')

        for i in users.keys():
            print(users.get(i))

        print('\n')

    else:

        exit = False

# Pramit
# Did not find any flaws, everything seems good
