age = input("Enter age:\n")
age = int(age)


if age < 5:
    print("To young for school")
elif age == 5:
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
else:
    print("Go to college")

