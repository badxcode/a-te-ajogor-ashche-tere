
name = '''
String with
multiple line
'''
print(name)

name = "Bangladesh"
print(name[-10])

name = "Bangladesh"
name2 = name[0:6]

print("'",name2,"'", "is mother-language of", name)
print(f" '{name2}' is mother-language of '{name}' ")
print(f' {name} sdkjf {name} dfsd {name} ')



name = "Ana De Armas"
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.find("a"))
print(name.rfind("a"))
rpl_name = name.replace("s", "f")
print(rpl_name)
print("Ana" in name)


name = input("Enter name: ")
if 30 > len(name) > 5:
    print(name)

else:
    name = input("enter name: ")
print(name)

name = "Hello"
print(name.replace("l","k"))
