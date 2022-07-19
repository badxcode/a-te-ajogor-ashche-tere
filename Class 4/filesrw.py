f = open("sherlock-holmes.txt", "r")
s = f.read()
dic = {}
for i in s:
    dic[i] = dic.get(i,0) + 1

for key, value in dic.items():
    print(key, value)
f.close()