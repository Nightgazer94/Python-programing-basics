import datetime

print("Enter your name: ")
name = input()

print("Enter your year of birth: ")
year = int(input())

age = datetime.date.today().year - year

print(f"User: {name} is {age} years old")
