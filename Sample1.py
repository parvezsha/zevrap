number = int(input("Enter any 2 digit number"))
reversenumber = 0
while number != 0:
    digit = number % 10
    second = reversenumber
    reversenumber = reversenumber * 10 + digit
    number //= 10
#subract greater number with smaller number
if (second > digit):
    sub = second - digit
else:
    sub = digit -second
result =float(sub /9)
print("Reserved Digit :", reversenumber)   
print("Subraction Diffirence is :", sub) 
print("Difference Subracted by 9 :", result)
 