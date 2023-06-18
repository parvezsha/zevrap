number = int(input("Enter any 2 digit number"))
reversenumber = 0
while number != 0:
    digit = number % 10
    reversenumber = reversenumber * 10 + digit
    number //= 10
#subract greater number with smaller number
print(reversenumber)    