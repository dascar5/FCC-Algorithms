#Given 2 list inputs, find the elements that appear in both

def list_intersection(a, b):
    return list(set(a).intersection(b))


a = []
n = int(input("Enter number of elements for the first list: "))
for i in range(0, n):
    ele1 = int(input())
    a.append(ele1)

b = []
n1 = int(input("Enter number of elements for the second list: "))
for i in range(0, n1):
    ele2 = int(input())
    b.append(ele2)

print(list_intersection(a, b))