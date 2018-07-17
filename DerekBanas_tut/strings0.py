print(type('string'))
print(type(5))
print(type(.225))

sample_string = 'This is a very important string'

print(sample_string[0])
print(sample_string[1])
print(sample_string[-1])
print(sample_string[1+5])

print('Length: ', len(sample_string))

# slices
print(sample_string[0:4])
print(sample_string[6:])
print("Spam + " + "Eggs")
print("Spam " * 6)

num_str = str(5)
print(num_str)

for char in sample_string:
    if char != ' ':
        print(char)

for z in range(0, len(sample_string) - 1, 2):
    print(sample_string[z] + sample_string[z+1])

print('Z = ', ord('Z'))
print('90 = ', chr(90))
