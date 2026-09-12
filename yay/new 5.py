name = input("What is your name? ")

while True:
    age_str = input("What is your age? ")
    if age_str.isdigit():
        age = int(age_str)
        break
    else:
        print("Invalid input. Please enter a number for age.")

print(f"Hello, {name}! You are {age} years old.")