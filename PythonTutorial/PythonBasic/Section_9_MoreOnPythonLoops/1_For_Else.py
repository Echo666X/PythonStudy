# in this tutorial, you’ll learn about the Python for else statement and how to use it effectively.
# suppose that you have a list of people, where each person is a dictionary that consists of name and age
# and you want to search for a person by name, if the list contains the person, you want to display the information of that person, otherwise, you want to show a message saying that the name is not found
people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = input('Please enter a name: ')

for person in people:
    if person['name'] == name:
        print(person)
        break
    else:
        print(f"{name} not found!")
# the if else statement can make you code more shorter, when the loop encounters the break statement, the else clause won't execute
