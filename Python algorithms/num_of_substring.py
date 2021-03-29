#Check how many times an input substring appears in an input string

def num_of_substring(string, substring):
    return counter

string = input('Insert string: ')
substring = input('Insert substring to check: ')
counter = 0
status = True
start = 0

while status:
    a = string.find(substring, start)
    if a == -1:
        status = False
    else:
        counter += 1
        start = a + 1

print(num_of_substring(string, substring))

#Insert string: To see the world in a grain of sand, and to see heaven in a wild flower, hold infinity in the palm of your hands, and eternity in an hour.
#Insert substring to check: in
#7