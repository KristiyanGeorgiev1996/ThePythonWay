class Car:
    def __init__(self, model, fuel_amount, fuel_consumption_per_km):
        self.model = model
        self.fuel_amount = fuel_amount
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.traveled_distance = 0

    def drive(self, amount_of_km):
        needed_fuel = amount_of_km * self.fuel_consumption_per_km
        if needed_fuel <= self.fuel_amount:
            self.fuel_amount -= needed_fuel
            self.traveled_distance += amount_of_km
        else:
            print("Insufficient fuel for the drive")

n = int(input())
cars = {}

for _ in range(n):
    model, fuel_amount, fuel_consumption = input().split()
    fuel_amount = float(fuel_amount)
    fuel_consumption = float(fuel_consumption)
    if model not in cars:
        cars[model] = Car(model, fuel_amount, fuel_consumption)

while True:
    command = input()
    if command == "End":
        break
    _, model, km = command.split()
    km = float(km)
    if model in cars:
        cars[model].drive(km)

for car in cars.values():
    print(f"{car.model} {car.fuel_amount:.2f} {car.traveled_distance}")
