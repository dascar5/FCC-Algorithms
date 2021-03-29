#Return the count of hex numbers in a given string (hex starts with 0x)

def num_of_hex(a):
    return counter


counter = 0

x = input("Insert string: ")
a = x.split()

for x in a:
    if x.startswith("0x") == True:
        counter += 1

print(num_of_hex(a))

# Insert string: 23 55 22 11 53 632 23 hello jump 12 0x242 0x343 0x11
# 3