n = input()
numbers = []

for _ in range(int(n)):
    num = int(input())
    numbers.append(num)

total = sum(numbers)
avg = total / int(n)

print("Sum:", total)
print("Average:", avg)

if avg > total:
    print("Average is greater")
else:
    print("Sum is greater")
