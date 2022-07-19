f = open("sherlock-holmes.txt", "r")
s = f.read()
list1 = s.split()
countSher = 0
for sherlock in list1:
    if ("Sherlock" in sherlock) or ("sherlock" in sherlock): 
        countSher += 1

print(countSher)

f.close()