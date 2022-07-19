f = open("sherlock-holmes.txt", "r")
s = f.read()
list1 = s.split(" ")
#print(list1)
dic = {}
countSher = 0
for i in list1:
    dic[i] = dic.get(i, 0) + 1

for key, val in dic.items():
    print("{} = {}".format(key, val))
f.close()