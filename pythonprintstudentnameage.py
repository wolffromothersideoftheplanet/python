name = input("Enter the student's name: ")
age = input("Enter the student's age: "))
passed = input("Did the student pass? (yes/no): ")

if passed.lower() == "yes":
    passed = True
else:
    passed = False

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("Passed:", passed)
