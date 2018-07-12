num1, num2 = input('Enter 2 numbers \n').split()
num1 = float(num1)
num2 = float(num2)

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
reminder = num1 % num2
floor_division = num1 // num2

print("{0} + {1} = {2}".format(num1, num2, "%.3f" % sum))
print("{0} - {1} = {2}".format(num1, num2, "%.3f" % difference))
print("{0} * {1} = {2}".format(num1, num2, "%.3f" % product))
print("{0} / {1} = {2}".format(num1, num2, "%.3f" % quotient))
print("{0} % {1} = {2}".format(num1, num2, "%.3f" % reminder))
print("{0} // {1} = {2}".format(num1, num2, "%.3f" % floor_division))
