#Check how many words ends with input character in an input string, count and print them

def num_of_wordsEndsWith(St,ch):
    return ar, counter

St= input('Insert string: ')
ch= input ('Insert character: ')
ar= []
counter=0

for i in St.split():
    if i.endswith(ch):
        ar.append(i)
        counter+=1

print(num_of_wordsEndsWith(St,ch))

#Insert string: Good good great great
#Insert character: d
#(['Good', 'good'], 2)