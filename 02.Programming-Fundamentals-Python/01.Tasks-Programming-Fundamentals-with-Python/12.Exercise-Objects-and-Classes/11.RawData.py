class Engine:
    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

class Cargo:
    def __init__(self, weight, type_):
        self.weight = weight
        self.type = type_

class Car:
    def __init__(self, model, engine_speed, engine_power, cargo_weight, cargo_type):
        self.model = model
        self.engine = Engine(engine_speed, engine_power)
        self.cargo = Cargo(cargo_weight, cargo_type)

n = int(input())
cars = []

for _ in range(n):
    parts = input().split()
    model = parts[0]
    engine_speed = int(parts[1])
    engine_power = int(parts[2])
    cargo_weight = int(parts[3])
    cargo_type = parts[4]
    cars.append(Car(model, engine_speed, engine_power, cargo_weight, cargo_type))

command = input()
if command == "fragile":
    for car in cars:
        if car.cargo.type == "fragile" and car.cargo.weight < 1000:
            print(car.model)
elif command == "flamable":
    for car in cars:
        if car.cargo.type == "flamable" and car.engine.power > 250:
            print(car.model)
