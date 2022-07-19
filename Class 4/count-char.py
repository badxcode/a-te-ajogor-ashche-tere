f = open("sherlock-holmes.txt", "r")
s = f.read()
dic = {}
for i in s:
    dic[i] = dic.get(i, 0) + 1

for key, val in dic.items():
    print("{} = {}".format(key, val))
f.close()