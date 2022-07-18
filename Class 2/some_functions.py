def name():
    print("My name is: zah1dz")

def sum(a, b):
    print("Sum is: {}".format(a+b))

def vowel(words):
    count = 0
    for ch in words.lower():
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            count += 1
    return count


