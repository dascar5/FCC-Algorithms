#Write a function that squares all the elements of an array in between 2 input numbers that are divisible by 3,
#but not by 6, including them, and then sums all the squares

def square_and_sum(start, end):
    return sum

start = int(input('Enter start of array: '))
end = int(input('Enter end of array: '))
sum = 0

for i in range(start, end + 1):
    if (i % 3 == 0 and i % 6 != 0):
        sum += i**2

print(square_and_sum(start, end))

#Enter start of array: 2
#Enter end of array: 9
#90

#because 3**2 + 9**2 = 90