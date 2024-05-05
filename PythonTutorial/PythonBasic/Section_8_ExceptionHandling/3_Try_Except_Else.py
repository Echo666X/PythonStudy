# in this tutorial, you’ll learn how to use the Python try...except...else statement.
# the try...except...else statement work as follows:
# if an exception occurs in the try clause, Python skips the rest of the statement in the try clause and the except statement execute
# in case no exception occurs in the try clause, the else clause will execute
# when you include the finally clause, the else clause executes after the try clause and before the finally clause.

# let's take some example:
# control flow (a program that calculates the body mass index):
def calculate(height, weight):
    """the first step is to calculate the BMI"""
    return weight/height**2

def evaluate(bmi):
    """the second step is to evaluate the BMI"""
    if 18.5 <= bmi <= 24.9:
        return "healthy"
    elif bmi >= 25:
        return "overweight"
    else:
        return "underweight"
    
try:
    height_test, weight_test = map(float,input().split(','))
except ValueError:
    print("ERROR")
else:
    BMI = calculate(height_test,weight_test)
    evaluation = evaluate(BMI)
    print(f"Your body mass index is {BMI}")
    print(f'This is considered {evaluation}')