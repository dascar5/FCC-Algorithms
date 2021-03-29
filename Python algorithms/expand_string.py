#Write a function that expands a string with a given prefix, sufix, and n - number of times prefix and sufix multiply

def expand_string(a, pre, suf, num):
    return pre * num + a + suf * num


a = input("Insert string: ")
pre = input("Insert prefix: ")
suf = input("Insert sufix: ")
num = int(input("Insert number of pref and suf multiplications: "))

print(expand_string(a, pre, suf, num))

# Insert string: Expanded!
# Insert prefix: Really
# Insert sufix: Nice.
# Insert number of pref and suf multiplications: 2
# Really Really Expanded!Nice. Nice. 