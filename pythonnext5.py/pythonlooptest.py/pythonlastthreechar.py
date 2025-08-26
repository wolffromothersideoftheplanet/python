text = input("Enter a string: ")
if len(text) >= 3:
    first_three = text[:3]    
    last_three = text[-3:]    
    print("First three characters:", first_three)
    print("Last three characters:", last_three)
else:
    print("The string is too short!")