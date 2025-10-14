class Car:
    def __init__(self, brand, model, horse_power):
        self.brand = brand
        self.model = model
        self.horse_power = horse_power

class Truck:
    def __init__(self, brand, model, weight):
        self.brand = brand
        self.model = model
        self.weight = weight

cars = []
trucks = []

while True:
    line = input()
    if line == 'end':
        break
    parts = line.split('/')
    if parts[0] == 'Car':
        cars.append(Car(parts[1], parts[2], parts[3]))
    elif parts[0] == 'Truck':
        trucks.append(Truck(parts[1], parts[2], parts[3]))

cars.sort(key=lambda c: c.brand)
trucks.sort(key=lambda t: t.brand)

if cars:
    print('Cars:')
    for car in cars:
        print(f"{car.brand}: {car.model} - {car.horse_power}hp")

if trucks:
    print('Trucks:')
    for truck in trucks:
        print(f"{truck.brand}: {truck.model} - {truck.weight}kg")
