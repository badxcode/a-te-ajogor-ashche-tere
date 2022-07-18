students = {
    "name": "Harry Potter",
    "age": 15,
    "house": "gryffindor",
    "play_quidditch": True
}
print(students["house"])
print(students.get("gender"))
students["gender"] = "male"
print(students.get("gender"))
print(students.get("subject", "Dark Arts"))
students["subject"] = "Herbology"
print(students.get("subject", "Dark"))

numbers = input("> ")
digit_mapping = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output = " "
for number in numbers:
    output += digit_mapping.get(number) + " "
print(output)



msg = input(">>")
words = msg.split("  ")
emoji = {
    ":)":"😊",
    ":(":"😞",
    "<3":"❤️",
    "Pizza": "🍕"
}
output = ""
for word in words:
    output += emoji.get(word, word) +  " "
print(output)
