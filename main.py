print("Welcome\n"
      "This is a Calculator.\n"
      "Insert your first nummer, the Operator and then your second nummer.\n"
      "Numbers can also be written like this: 123.00\n"
      "Valid Operators: +, -, *, /.\n")

last_result = 0
another_math_task = True
use_last_result = False


def another_math_task():
    user_input_c = input("You want calculate another Math task? Enter yes or no: ")

    if user_input_c == "yes":
        return True
    else:
        return False


def re_use():
    user_input_c = input("You want use the result? Enter yes or no: ")

    if user_input_c == "yes":
        return True
    else:
        return False


def calculator(user_input_a, operator, user_input_b):
    last_result = 0
    if operator == "+":
        result = user_input_a + user_input_b
        print(result)
        return result
        last_result = result
    elif operator == "-":
        result = user_input_a - user_input_b
        last_result = result
        print(result)
    elif operator == "*":
        print(user_input_a * user_input_b)
    elif operator == "/":
        print(user_input_a / user_input_b)
    else:
        print("Invalid Operator")
        print("Valid Operator are  +, -, *, /")


while another_math_task == True:
    if use_last_result == False:
        user_input_a = int(input("Enter the first Number: "))
    else:
        user_input_a = last_result

    operator = input("Enter a Operator: ")
    user_input_b = int(input("Enter the second Number: "))
