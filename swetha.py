def manage_hobbies():
    name_list = {'Pramit': 'Cooking', 'Rolstan': 'Touring', 'Pradeep': 'Coding', 'Shubham': 'Playing',
                 'Swetha': 'Reading'}
    print(name_list)
    action_var = int(input(
        "Enter action \n 1. Add new person \n 2. Remove person \n 3. view all people and hobbies in dict \n 4. view "
        "all hobbies in dict \n : "))
    if action_var == 1:
        input_num = int(input("Enter total number of names and hobbies to add: "))
        for num in range(0, input_num):
            name = input("Enter a name: ")
            hobby = input("Enter a hobby: ")
            name_list[name] = hobby
        print(name_list)
    elif action_var == 2:
        name_to_delete = input("Enter name to delete: ")
        del name_list[name_to_delete]
        print(name_list)
    elif action_var == 3:
        print(name_list)
    elif action_var == 4:
        print(name_list.values())
    else:
        print("action not valid")


manage_hobbies()
