print("Which two numbers do you want to add together?")

user_input1 = input("Input your first number: ")
user_input2 = input("Input your second number: ")

try:
    print(float(user_input1) + float(user_input2))
except:
    print("At least one of your inputs was not a number!")