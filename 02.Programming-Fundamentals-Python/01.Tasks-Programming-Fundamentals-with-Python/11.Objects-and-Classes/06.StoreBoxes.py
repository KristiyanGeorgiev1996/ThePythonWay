class Box:
    def __init__(self, serial_number, item, quantity, price_box):
        self.serial_number = serial_number
        self.item = item
        self.quantity = quantity
        self.price_box = price_box
        self.total_price = quantity * price_box

boxes = []

while True:
    line = input()
    if line == 'end':
        break
    data = line.split()
    serial_number, item_name = data[0], data[1]
    item_quantity, item_price = int(data[2]), float(data[3])
    boxes.append(Box(serial_number, item_name, item_quantity, item_price))

boxes.sort(key=lambda b: b.total_price, reverse=True)

for box in boxes:
    print(box.serial_number)
    print(f"-- {box.item} - ${box.price_box:.2f}: {box.quantity}")
    print(f"-- ${box.total_price:.2f}")
