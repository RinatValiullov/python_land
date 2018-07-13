# your_float = input("Enter a float:\t")
#
# your_float = float(your_float)
#
# print("Round to 2 decimals: {:.2f}".format(your_float))
#
# print("***************")

money = input("Your desire investment, $: ")
interest_rate = input("Interest rate, %: ")

money = float(money)
interest_rate = float(interest_rate) * .01

for i in range(10):
    money += money * interest_rate

print("Your investment after 10 years: {:.2f} dollars".format(money))

