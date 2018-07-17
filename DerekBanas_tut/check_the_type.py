letter_a = "a"
num_5 = "5"
num_5point2 = "5.14"
a_space = " "

print("Is a a letter or number:", letter_a.isalnum())

print("Is a a letter:", letter_a.isalpha())

print("Is 5 a number:", num_5.isdigit())

print("Is 5.2 a number:", num_5point2.isdigit())

print("Is a a lowercase:", letter_a.islower())

print("Is a a uppercase:", letter_a.isupper())

print("Is a_space a space:", a_space.isspace())

num_pi = "3.14"


def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False


print("Is PI a float: ", isfloat(num_pi))
