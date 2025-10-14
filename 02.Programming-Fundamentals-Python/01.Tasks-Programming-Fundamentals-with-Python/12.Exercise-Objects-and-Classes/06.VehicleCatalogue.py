class Vehicle:
    def __init__(self, type_, model, color, horsepower):
        self.type = type_
        self.model = model
        self.color = color
        self.horsepower = horsepower

def calculate_average_horsepower(vehicles):
    if not vehicles:
        return 0
    total_hp = sum(v.horsepower for v in vehicles)
    return total_hp / len(vehicles)

vehicles = []

while True:
    line = input()
    if line == "End":
        break
    type_, model, color, hp = line.split()
    vehicles.append(Vehicle(type_, model, color, int(hp)))

requested_models = []
while True:
    line = input()
    if line == "Close the Catalogue":
        break
    requested_models.append(line)

requested_vehicles = [v for v in vehicles if v.model in requested_models]

cars = sorted([v for v in requested_vehicles if v.type == 'car'], key=lambda v: v.horsepower)
trucks = sorted([v for v in requested_vehicles if v.type == 'truck'], key=lambda v: v.horsepower)

for car in cars:
    print(f"Type: Car")
    print(f"Model: {car.model}")
    print(f"Color: {car.color}")
    print(f"Horsepower: {car.horsepower}")

for truck in trucks:
    print(f"Type: Truck")
    print(f"Model: {truck.model}")
    print(f"Color: {truck.color}")
    print(f"Horsepower: {truck.horsepower}")

all_cars = [v for v in vehicles if v.type == 'car']
all_trucks = [v for v in vehicles if v.type == 'truck']

avg_car_hp = calculate_average_horsepower(all_cars)
avg_truck_hp = calculate_average_horsepower(all_trucks)

print(f"Cars have average horsepower of: {avg_car_hp:.2f}.")
print(f"Trucks have average horsepower of: {avg_truck_hp:.2f}.")
