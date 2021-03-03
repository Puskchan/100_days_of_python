import os

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

new = True
conti = True
operations_list = ["+","-","*","/"]

while new == True:
    print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
    user_input_1 = float(input("Enter the first number: "))

    conti = True

    while conti == True:
        for i in operations_list:
            print(i)
        operation_choice = input("Pick a operation: ")

        user_input_2 = float(input("Enter the second number: "))


        if operation_choice == "+":
            result = add(user_input_1,user_input_2)
            print(f"{user_input_1} {operation_choice} {user_input_2} = {result}")
        elif operation_choice == "-":
            result = sub(user_input_1,user_input_2)
            print(f"{user_input_1} {operation_choice} {user_input_2} = {result}")
        elif operation_choice == "*":
            result = mul(user_input_1,user_input_2)
            print(f"{user_input_1} {operation_choice} {user_input_2} = {result}")
        elif operation_choice == "/":
            result = div(user_input_1,user_input_2)
            print(f"{user_input_1} {operation_choice} {user_input_2} = {result}")
        else:
            print(f"{user_input_1} {operation_choice} {user_input_2} = Nonsense\nReally???")
        
        user_input_3 = input("Do you wnat to continue with the same number? Type 'yes' to continue and 'no' to restart: ")

        if user_input_3 == "yes":
            user_input_1 = result
            os.system("cls")
        elif user_input_3 == "no":
            conti = False
        else:
            new = False
            break

print("You typed some stupid shit, get lost!")
