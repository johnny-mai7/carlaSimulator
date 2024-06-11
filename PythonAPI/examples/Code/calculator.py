""" My Calculator Program """
__author__ = "Johnny"

import random
import cmath


# function to generate n amount of n
def random_generator(highest_num, num_of_random):
    for x in range(num_of_random):
        random1 = [random.randint(1, highest_num)]
        print("Your random number is:", random1)
    random_num_menu = 0
    while random_num_menu != 1:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    highest_num = int(input("What is the range for your Random Number Generator? 1-(?) "))
                    num_of_random = int(input("How many random numbers do you want? "))
                    for x in range(num_of_random):
                        random1 = [random.randint(1, highest_num)]
                        print("Your random number is:", random1)
                    tryLoop = 0
                except ValueError:
                    print("Sorry, that is not a number. Please try again. ")
        else:
            random_num_menu = 1


# function to find the exponent
def exponent(power_num, base_num):
    final_ans = base_num ** power_num
    print(final_ans)
    exponentMenu = 0
    while exponentMenu != 1:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    base_num = float(input("Enter the base: "))
                    power_num = float(input("Enter the power: "))
                    final_ans = base_num ** power_num
                    print(final_ans)
                    tryLoop = 0
                except ValueError:
                    print("Please try again.")
        else:
            exponentMenu = 1


# function to find the square root of n
def square_roots(root_num):
    sqrt = cmath.sqrt(root_num)
    print("Square Root:", sqrt, "\n")
    rootMenu = 0
    while rootMenu != 1:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    root_num = float(input("Enter number: "))
                    sqrt = cmath.sqrt(root_num)
                    print("Square Root: ", sqrt, "\n")
                    tryLoop = 0
                except ValueError:
                    print("Please try again.")
        else:
            rootMenu = 1


# function to divide
def division(div_num1, div_num2):
    print('{} / {}'.format(div_num1, div_num2))
    print(div_num1 / div_num2, "\n")
    divisionMenu = 0
    while divisionMenu == 0:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    div_num1 = float(input("Enter first number: "))
                    div_num2 = float(input("Enter second number: "))
                    print('{} / {}'.format(div_num1, div_num2))
                    print(div_num1 / div_num2, "\n")
                    tryLoop = 0
                except ZeroDivisionError:
                    print("Sorry. Invalid Selection. ")
                except ValueError:
                    print("Please try again.")
        else:
            divisionMenu = 1


# function to multiply
def multiplication(mult_num1, mult_num2):
    print('{} * {}'.format(mult_num1, mult_num2))
    print(mult_num1 * mult_num2, "\n")
    multiplicationMenu = 0
    while multiplicationMenu == 0:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    mult_num1 = float(input("Enter first number: "))
                    mult_num2 = float(input("Enter second number: "))
                    print('{} * {}'.format(mult_num1, mult_num2))
                    print(mult_num1 * mult_num2, "\n")
                    tryLoop = 0
                except ValueError:
                    print("Please try again.")
        else:
            multiplicationMenu = 1


# function to subtract
def subtraction(sub_num1, sub_num2):
    print('{} - {}'.format(sub_num1, sub_num2))
    print(sub_num1 - sub_num2, "\n")
    subtractionMenu = 0
    while subtractionMenu == 0:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    sub_num1 = float(input("Enter first number: "))
                    sub_num2 = float(input("Enter second number: "))
                    print('{} - {}'.format(sub_num1, sub_num2))
                    print(sub_num1 - sub_num2, "\n")
                    tryLoop = 0
                except ValueError:
                    print("Please try again.")
        else:
            subtractionMenu = 1


# function to add
def addition(add_num1, add_num2):
    print('{} + {}'.format(add_num1, add_num2))
    print(add_num1 + add_num2, "\n")
    additionMenu = 0
    while additionMenu == 0:
        leave = input("Would you like to return to the main menu? Y/N (Invalid selection = Return to Menu)").lower()
        if leave == "N" or leave == "n":
            tryLoop = 1
            while tryLoop == 1:
                try:
                    add_num1 = float(input("Enter first number: "))
                    add_num2 = float(input("Enter second number: "))
                    print('{} + {}'.format(add_num1, add_num2))
                    print(add_num1 + add_num2, "\n")
                    tryLoop = 0
                except ValueError:
                    print("Please try again.")
        else:
            additionMenu = 1


# menu selection
def menu(name):
    menuLoop = 1
    while menuLoop == 1:

        # prompt for user to choose what they want to do
        print("Welcome to the Calculator Program!", name)
        print("Press #1: Addition")
        print("Press #2: Subtraction")
        print("Press #3: Multiplication")
        print("Press #4: Division")
        print("Press #5: Roots")
        print("Press #6: Exponent")
        print("Press #7: Random Number Generator ")
        print("Press Q to quit ")

        # user input to choose they want to do
        menu_input = input("Menu Selection: ").lower()
        if menu_input == "1":
            inputLoop = 1
            add_num1 = 0
            add_num2 = 0
            while inputLoop == 1:
                try:
                    add_num1 = float(input("Enter first number: "))
                    add_num2 = float(input("Enter second number: "))
                    inputLoop = 0
                except ValueError:
                    print("please try again.")
            addition(add_num1, add_num2)

        elif menu_input == "2":
            inputLoop = 1
            sub_num1 = 0
            sub_num2 = 0
            while inputLoop == 1:
                try:
                    sub_num1 = float(input("Enter first number: "))
                    sub_num2 = float(input("Enter second number: "))
                    inputLoop = 0
                except ValueError:
                    print("please try again.")
            subtraction(sub_num1, sub_num2)

        elif menu_input == "3":
            inputLoop = 1
            mult_num1 = 0
            mult_num2 = 0
            while inputLoop == 1:
                try:
                    mult_num1 = float(input("Enter first number: "))
                    mult_num2: float = float(input("Enter second number: "))
                    inputLoop = 0
                except ValueError:
                    print("please try again.")
            multiplication(mult_num1, mult_num2)

        elif menu_input == "4":
            inputLoop = 1
            while inputLoop == 1:
                try:
                    div_num1 = float(input("Enter first number: "))
                    div_num2 = float(input("Enter second number: "))
                    division(div_num1, div_num2)
                    inputLoop = 0
                except ZeroDivisionError:
                    print("Invalid Selection. Please try again.")
                except ValueError:
                    print("please try again.")

        elif menu_input == "5":
            inputLoop = 1
            root_num = 0
            while inputLoop == 1:
                try:
                    root_num = float(input("Enter number: "))
                    inputLoop = 0
                except ValueError:
                    print("please try again.")
            square_roots(root_num)

        elif menu_input == "6":
            inputLoop = 1
            power_num = 0
            base_num = 0
            while inputLoop == 1:
                try:
                    base_num: float = float(input("Enter the base: "))
                    power_num = float(input("Enter the power: "))
                    inputLoop = 0
                except ValueError:
                    print("please try again.")
            exponent(power_num, base_num)

        elif menu_input == "7":
            inputLoop = 1
            highest_num = 0
            num_of_random = 0
            while inputLoop == 1:
                try:
                    highest_num = int(input("What is the range for your Random Number Generator? 1-(?) "))
                    if highest_num <= 0:
                        raise ValueError
                    num_of_random = int(input("How many random numbers do you want? "))
                    if num_of_random <= 0:
                        raise ValueError
                    inputLoop = 0
                except ValueError:
                    print("Value must be greater than zero. Please try again. \n")
            random_generator(highest_num, num_of_random)

        elif menu_input == "q":
            quit()
        else:
            print("Invalid selection, Please try again.")


def main():
    print("Hello there, What is your name?")
    name = input("")
    menu(name)


if __name__ == '__main__':
    main()
