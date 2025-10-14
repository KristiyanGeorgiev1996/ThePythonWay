data_type = input()
value = input()

if data_type == "int":
    print(int(value) * 2)
elif data_type == "real":
    print(f"{float(value) * 1.5:.2f}")
elif data_type == "string":
    print(f"${value}$")
