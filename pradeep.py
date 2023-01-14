dict = {}
condition = True
while (condition):
    def add(dict):

        list = input(
            "Enter a name and hobby separated by a comma:").split(", ")
        for l in list:
            l = l.lower()

        for key in dict:
            if (key not in dict.keys):
                dict.update({list[0]: list[1]})
            else:
                print("name already found.. updating hobby")
                dict[key] = list[1]

        list.clear

    def remove():
        remkey = input("Enter the name to be removed")
        remkey = remkey.lower
        if (dict.pop(remkey) != 0):
            dict.pop(remkey)
        else:
            print("name not found")

    istr = ""
    istr = input(
        "\n\n\nDo you want to add or remove or display or end? Type \n add \n remove \n display \n end\n")

    if (istr == "add"):
        add(dict)

    elif (istr == "remove"):
        remove()

    elif (istr == "display"):
        print("# People in the list:")
        for key in dict:
            keystr = key.capitalize()

            dictstr = dict[key].capitalize()
            print("# ", keystr, ": ", dictstr)
        print("\n#Hobbies in the list")
        for key in dict:
            dictstr = dict[key].capitalize()
            print("# ", dictstr)

    elif (istr == "end"):
        condition = False
    else:
        print("Enter right input")

# Could have added a counter before adding, that way I don't have to enter add command every time
# Dictionary not getting updated
# Display not WORKING!
