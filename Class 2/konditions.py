is_regular = True
has_card = True
base_price = 250

if is_regular:
    offered_price = base_price - (0.3*base_price)
elif not is_regular and has_card:
    offered_price = base_price - (0.2*base_price)
else:
    offered_price = base_price - (0.15*base_price)

print(offered_price)

length = int(input("Enter length: "))
unit = input("M(Meter)/ C(Centimerter: ")

if unit.upper() == "M":
    new_length = length * 100
else:
    new_length = length / 100
print(new_length)
