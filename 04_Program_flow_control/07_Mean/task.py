numbers = []
printed_number = ""
n = int(input('Enter n: '))

for _ in range (0, n):
    user_input = int(input('Enter a number: '))
    printed_number += str(user_input) + " "
    numbers.append(user_input)

average = sum(numbers) / len(numbers)
result = sum(numbers)


print(f"Entered numbers: {printed_number}")
print(f"sum: {result}")
print(f"average: {average}")
if result > average:
    print("The sum is greater!")
else:
    print("The sum is lower!")