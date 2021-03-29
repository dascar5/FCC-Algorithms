# Given a,b,i, return the list and sum of elements between a,b that are divisible by i, including a,b

def segment(a, b, i):
    arr = list(range(a, b + 1))
    arr1 = []
    sum = 0

    for x in arr:
        if x % i == 0:
            arr1.append(x)
            sum+= x

    return arr1,sum


a = int(input('Insert a: '))
b = int(input('Insert b: '))
i = int(input('Insert i: '))

print(segment(a, b, i))

# Insert a: 3
# Insert b: 9
# Insert i: 3
# ([3, 6, 9], 18)