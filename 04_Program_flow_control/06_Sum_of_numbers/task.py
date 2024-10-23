# tady je poslední hodnota přidána pomocí user +1
user = int(input("please insert number: "))
result = 0

for number in range(0, user +1):
    result += number

print(result)

# Tady je poslední hodnota doplněná rovnou na žačátku

user = int(input("please insert number: "))
for number in range(0, user):
    user += number
print(user)
