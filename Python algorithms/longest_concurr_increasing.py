#Write a function that has a list as input, and have it return a sublist with the longest increasing chain of positive numbers in a row

def longest_concurr_increasing(arr):
    return LCI_Arr

arr = []
n=int(input("How many array elements do you want? "))
for i in range (0,n):
    ele = int(input())
    arr.append(ele)

l = len(arr)
i = 0

max = 1

start = 0
end = 0

beststart = 0
bestend = 0

while i<l:
    if i+1 < l and arr[i+1]>arr[i]:
        end = end + 1
        if (end-start+1) > max:
            max = (end - start + 1)
            beststart = start
            bestend = end
    else:
        start = i+1
        end = i+1

    i = i + 1

LCI_Arr = (arr[beststart:bestend+1])

print(longest_concurr_increasing(arr))