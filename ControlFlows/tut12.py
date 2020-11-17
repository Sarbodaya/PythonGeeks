# Looping Extensions
cars = ['Aston', 'Audi', 'Mclaren']
accessories = ["GPS kit", "Car Repair Tool Kit"]

prices = {1: "570000$", 2: "68000$", 3: "450000", 4: "8900$", 5: "4500$"}

for index, c in enumerate(cars, start=1):
    print(f"Car: {c} Price: {prices[index]}")

for index, a in enumerate(accessories, start=4):
    print(f"Accessory: {a} Price: {prices[index]}")
