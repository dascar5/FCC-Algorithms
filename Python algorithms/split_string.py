#Split an input string based on an input number of characters (space counts as a character too)

def split_string(St,n):
    return x

St = input('Insert string: ')
n = int(input('Insert int: '))
x = [St[i:i+n] for i in range(0, len(St), n)]

print (split_string(St,n))

#Insert string: Good morning, mother
#Insert int: 2
#['Go', 'od', ' m', 'or', 'ni', 'ng', ', ', 'mo', 'th', 'er']