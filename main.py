print("Welcome\n"
      "This is a Calculator.\n"
      "Insert your first nummer, the Operator and then your second nummer.\n"
      "Numbers can also be written like this: 123.00\n"
      "Valid Operators: +, -, *, /.\n")


def addition(a, b):
    return a + b


while True:
    user_input_a = int(input("Enter the first Number: "))
    operator = input("Enter a Operator: ")
    user_input_b = int(input("Enter the second Number: "))
    result_addition = addition(user_input_a, user_input_b)

    if operator == "+":
        addition(user_input_a, user_input_b)
        print(result_addition)
    elif operator == "-":
        print(user_input_a - user_input_b)
    elif operator == "*":
        print(user_input_a * user_input_b)
    elif operator == "/":
        print(user_input_a / user_input_b)
    else:
        print("Invalid Operator")
        print("Valid Operator are  +, -, *, /")
