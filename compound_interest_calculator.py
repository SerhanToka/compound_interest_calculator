print("*--------------------------------------*")
print("Welcome to Compound Interest Calculator!")
print("*--------------------------------------*\n")

amount = 0
rate = 0
time = 0

while amount <= 0:
    amount = float(input("Enter the principle amount: "))
    if amount <= 0:
        print("The amount can't be less than or equal to zero!")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("The rate can't be less than or equal to zero!")

while time <= 0:
    time = int(input("Enter the time in year/s: "))
    if time <= 0:
        print("The time can't be less than or equal to zero!")

total = amount * pow((1 + rate / 100), time) # A = P(1 + r/n) ** t

print(f"Balance after {time} year/s: ${total: .2f}")