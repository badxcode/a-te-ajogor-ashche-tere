mylist = [] # empyty list
t1 = () # empyt tuple
mylist2 = ['imran', 'shayed', 123, 23.0, 'mohor']
t = ('imran', 123, 35.99)

list1 = [123]
print(type(list1))
t3 = (123, )
print(type(t3))


list1 = [1, 4, 2, 3, 3, 8]
list2 = [4, 1, 1, 5, 6]
list3 = list1 + list2
print(list3)

#print([1, 4]*3)
list3.append(9)
print(list3)
list3.insert(2, 54)
print(list3)
list3.pop()
print(list3)

list3.reverse()
print(list3)
list3.sort()
print(list3)

list3.remove(4)
print(list3)
list3.pop(2)
print(list3)


print(list3.count(1))
print(list3.index(3))

t = (5, 3, 2, 3, 4, 1, 5)
print(t.count(5))
print(t.index(2))


list1 = ['one', 2, 'three', 4, 5, 3]
# del list1[1:4] 
print(list1)

b = list1[:]
print(b)


var = "one", 2, 1965, 'imran'
print(type(var))

t1, t2, t3, t4 = var

print(t1, t2, t3, t4)
print(type(t1))
print(type(t2))

a = 5
b = 6
#temp = a 
#a = b 
#b = temp 

print(a, b)

(a, b) = (b, a)
print(a, b)


authors = [('Jahid', 'Imran'), ('Shayed', 'Hasan'), ('Ishan', 'Ahmed')]
for firstname, lastname in authors:
    print(firstname)
    print(lastname)


fruits = ['apple', 'pear', 'jackfruit', 'mango']
for fr1, fr2 in enumerate(fruits):
    #print(type(fr))
    #print(fr[0], fr[1])
    print(fr1, fr2)













 
