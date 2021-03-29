#Write a function that only returns the count of elements of a list that are less than the given max

def less_than_max(a, max):
    return el


el = 0
a = []
n = int(input("Insert number of elements: "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)

max = int(input("Max: "))

for x in a:
    if x < max:
        el += 1

print(less_than_max(a, max))

# Insert number of elements: 3
# 2
# 4
# 6
# Max: 5
# 2