class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bag = []

    def buy_product(self, product):
        if self.money >= product.cost:
            self.bag.append(product)
            self.money -= product.cost
            return True
        return False

people_input = input().split(';')
people = {}
for person_data in people_input:
    if not person_data:
        continue
    name, money_str = person_data.split('=')
    people[name] = Person(name, float(money_str))

products_input = input().split(';')
products = {}
for product_data in products_input:
    if not product_data:
        continue
    name, cost_str = product_data.split('=')
    products[name] = Product(name, float(cost_str))

while True:
    command = input()
    if command == "END":
        break
    person_name, product_name = command.split()
    person = people.get(person_name)
    product = products.get(product_name)
    if person and product:
        if person.buy_product(product):
            print(f"{person_name} bought {product_name}")
        else:
            print(f"{person_name} can't afford {product_name}")

for person in people.values():
    if not person.bag:
        print(f"{person.name} - Nothing bought")
    else:
        bought_names = ', '.join([p.name for p in person.bag])
        print(f"{person.name} - {bought_names}")
