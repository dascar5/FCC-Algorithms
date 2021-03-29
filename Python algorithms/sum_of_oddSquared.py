#Write a function that sums squares of all the odd elements in between a given start and an end

def square_and_sum(start, end):
    return sum

sum = 0
start = int(input('Insert start : '))
end = int(input('Insert end: '))

for i in range(start, end + 1):
    if (i % 2 != 0):
        sum += i** 2

print(square_and_sum(start, end))

#Insert start : 2
#Insert end: 5
#34

#because 3**2 + 5**2 = 35