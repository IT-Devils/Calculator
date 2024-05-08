print("Welcome\n"
      "This is a Calculator.\n"
      "Insert your first nummer, the Operator and then your second nummer.\n"
      "Numbers can also be written like this: 123.00\n"
      "Valid Operators: +, -, *, /.\n")


def re_use():
    user_input_c = input("You want use the result? Enter yes or no: ")
    return user_input_c


while True:
    user_input_a = int(input("Enter the first Number: "))
    operator = input("Enter a Operator: ")
    user_input_b = int(input("Enter the second Number: "))
    last_result = 0

    if operator == "+":
        result = user_input_a + user_input_b
        print(result)
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

    user_input_c = re_use()

    if user_input_c == "yes":
        print(last_result)
    else:
        continue
