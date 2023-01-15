
# Evaluation Comments by Rolstan

# Good -

# Works
# Could be iterative & not to show the dict or hobbies without asked by the user, only print it when user selects that option

# Things to improve -

# Structured but variable names are not meaningful
# Bit confusing to navigate
# Output is not user friendly ex. Name & Hobby instead of { 'Name': 'Hobby' }...
# Type of answer is not mentioned for making any changes to the dictionary ex Do you want to make changes ( Y / N ) ?
# Similar case with Do you want to delete any entry? , entered nope but eitherways it told me to update the dictionary & showed the hobby list without me mentioning it



def manage_hobbies():
    dict = {}


    #Pradeep - input not in the way described in the question
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
    # Pradeep - unless I see the program to enter yes or no is not very obvious. May be displaying in the text itself would help
    # pradeep - case sensitive errors coming up
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



#==words not capitalized while printing
#removing entry does not work if i give input of a diff case
