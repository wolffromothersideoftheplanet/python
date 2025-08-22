user_input = ""

while user_input.lower() != "exit":
    user_input = input("Enter something (type 'exit' to stop): ")
    if user_input.lower() != "exit":
        print("You entered:", user_input)

print("Program ended.")
