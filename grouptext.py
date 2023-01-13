Problem:
You are building a program that keeps track of a list of people and their hobbies. The program should allow the user to:

- Add a new person to the list
- Remove a person from the list
- View all the people in the list and their hobbies
- View all the hobbies in the list

You need to write a function called "manage_hobbies()" that does the following:

1. Prompts the user to enter a name and a hobby for a new person, separated by a comma. It should then check if the inputs are strings using the isinstance function. If the inputs are not strings, it should print an error message. If the inputs are valid, it should add the person and their hobby to the list of people and their hobbies.
2. Prompts the user to enter a name of a person they wish to remove from the list. It should then check if the input is a string using the isinstance function. If the input is not a string, it should print an error message. If the input is valid, it should remove the person and their hobby from the list.
3. Name must not be case-sensitive. Rolstan or rolstAN or rOLsTan - all should be considered as same.
4. If a name is input twice, it should update the latest hobby.
5. Prints the names of all the people in the list and their hobbies.
6. Prints all the hobbies in the list using a nested loop.

You should use a list to store the people and their hobbies, where each person is represented as a dictionary with keys 'name' and 'hobby' and values entered by the user.
You should use set to keep track of the hobbies.

manage_hobbies()
# Output:
# Enter a name and hobby separated by a comma: Pramit, Cooking
# Enter a name and hobby separated by a comma: Rolstan, Touring
# Enter a name and hobby separated by a comma: Pradeep, Coding
# Enter a name and hobby separated by a comma: Shubham, Dancing
# Enter a name and hobby separated by a comma: Swetha, Reading
# Enter a name and hobby separated by a comma: Robin, Singing
# Enter a name and hobby separated by a comma: shUBHam, Playing
# Enter a name to remove: Robin

# People in the list:
# Pramit: Cooking
# Rolstan: Touring
# Pradeep: Coding
# Shubham: Playing
# Swetha: Reading

# Hobbies in the list:
# Cooking
# Touring
# Coding
# Playing
# Reading
