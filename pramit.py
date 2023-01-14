def manage_hobbies():
    dict = {}
    print(dict)
    # Taking inputs
    n = int(input("How many entries? "))
    # Storing Values irrespective of Key Case
    for i in range(0, n):
        s = input("Enter name: ")
        val = input("Enter hobby: ")
        p = s[0].upper() + s[1:].lower()
        dict[p] = val
    print("Dictionary stored..")
    print(dict)
    # Prompt for change
    a = input("Do you want to make changes? ")
    if a == "Yes" or a == "Y" or a == "yes" or a == "y":
        # Prompt for Deletion
        b = input("Do you want to delete any entry? ")
        if b == "Yes" or b == "Y" or b == "yes" or b == "y":
            print(dict)
            s = input("Whose entry do you want to delete? ")
            del dict[s]
            print("People in the list:")
            for k, v in dict.items():
                print(k, ": ", v)
            print("Hobbies in the list:")
            for k, v in dict.items():
                print(v)

        else:
            print("Update dictionary..")
            s = input("Enter name: ")
            val = input("Enter hobby: ")
            p = s[0].upper() + s[1:].lower()
            dict[p] = val
            print("People in the list:")
            for k, v in dict.items():
                print(k, ": ", v)
            print("Hobbies in the list:")
            for k, v in dict.items():
                print(v)
    else:
        print("Okay..")
        print("People in the list:")
        for k, v in dict.items():
            print(k, ": ", v)
        print("Hobbies in the list:")
        for k, v in dict.items():
            print(v)


# Function Call
manage_hobbies()
