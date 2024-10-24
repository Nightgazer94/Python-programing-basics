print("Equation a*x**2 + b*x + c == 0")

print("Equation a*x**2 + b*x + c == 0")

print("Enter a")
a = float(input())

print("Enter b")
b = float(input())

print("Enter c")
c = float(input())

delta = b**2 - 4*a*c

if delta > 0:
    x_1 = (-b - delta**0.5) / (2 * a)
    x_2 = (-b + delta**0.5) / (2 * a)
    print(f"x_1 = {x_1}")
    print(f"x_2 = {x_2}")
elif delta == 0:
    x_1 = x_2 = -b / (2 * a)
    print(f"x_1 = x_2 = {x_1}")
else:
    print("no solution")
