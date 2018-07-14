# 1 task

# i = .111111111111111111111111111111111
# z = .000000000000000100000000000000001
#
# print('Answer: {:.32f}'.format(i + z))

# 2 task

# import random
#
#
# rand_number = random.randrange(1, 51)
#
# i = 1
#
# while i != rand_number:
#     i += 1
#
# print("The random value is: ", rand_number)


# z = 1
# while z <= 20:
#     if z % 2 == 0:
#         z += 1
#         continue
#     if z == 15:
#         break
#
#     print("Odd: ", z)
#     z += 1

# 3 task

'''
    #
   ###
  #####
 #######
#########
    #
'''

# Use 1 while loop and 3 for loops
# 4 spaces : 1 hash
# 3 spaces : 2 hashes
# 2 spaces : 5 hashes
# 1 spaces : 7 hashes
# 0 spaces : 9 hashes

# Need to do

# 1. Decrement spaces by 1 each time through the loop
# 2. Increment hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and hashes for each row
# 6. Print stump spaces and then 1 hash

tree_height = int(input("How tall is the tree? "))
print(tree_height)

spaces = tree_height - 1

hashes = 1

stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end='')
    for i in range(hashes):
        print('#', end='')

    print()

    spaces -= 1

    hashes += 2

    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end='')

print('#')
