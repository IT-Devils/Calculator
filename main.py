user_input_a = int(input("Enter the first Number: "))
operator = input("Enter a Operator: ")
user_input_c = int(input("Enter the second Number: "))

if operator == "+":
    print(user_input_a + user_input_c)
elif operator == "-":
    print(user_input_a - user_input_c)
elif operator == "*":
    print(user_input_a * user_input_c)
elif operator == "/":
    print(user_input_a / user_input_c)
else:
    print("Invalid Operator")
    print("Valid Operator are  +, -, *, /")
