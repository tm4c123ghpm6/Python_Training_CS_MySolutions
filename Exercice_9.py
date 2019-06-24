"""
Exercise 1
Write a code that asks the operator for its name and throws an exception if the string is longer than 20 characters

"""


def get_info_from_user(param):
    if(param=="name"):
        data = input("What is your name ? \n")
    else:
        data = input("What is your age ? \n")
    return data
def get_exercise_from_user():
    name = input("What exercise do you want to run:exercise1 or exercise2 ? \n")
    return name


def exercise1():
    name = get_info_from_user("name")
    if(len(name)<=20):
        print("your name is ", name)
    else:
        raise Exception("your name is longer than 20 character.")


"""
Exercise 2
Write a code that asks the operator for its age and tries to convert it to int
Use the int(string) function: https://docs.python.org/3/library/functions.html#int
This function will throw an ValueError if it cannot be converted, use the try-catch-else construct to inform 
the user if the age given was correct or not

"""


def exercise2():
    name = get_info_from_user("age")
    try:
        print("you are: ", int(name), "years old")
    except ValueError:
        print('the age you entered is not a number, please enter a number')

    pass


if __name__ == '__main__':
    exercise = get_exercise_from_user()
    if(exercise=="exercise1"):
        exercise1()
    elif (exercise=="exercise2"):
        exercise2()
    else:
        print("the option you choosed does not exist, the programm is closing now ")
