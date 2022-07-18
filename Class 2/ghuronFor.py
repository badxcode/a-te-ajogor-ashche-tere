the_bois = ["Homelander", "starlight", "Kimiko", "Depp"]
for sups in the_bois:
    print(sups)


the_bois = [1,2,3,4,5,6]
for sups in the_bois:
    print(sups)





for sups in range(10,20,3) :
    print(sups)

hp_prices = [100,200,300,400,700,760,900]
total = 0

for per_price in hp_prices:
    if per_price == 700:
        continue
    total = per_price + total
print(total)