while True:
    input_value = input()
    if input_value == "END":
        break

    try:
        int_value = int(input_value)
        print(f"{input_value} is integer type")
    except ValueError:
        try:
            float_value = float(input_value)
            print(f"{input_value} is floating point type")
        except ValueError:
            if input_value == "true" or input_value == "false":
                print(f"{input_value} is boolean type")
            elif len(input_value) == 1:
                print(f"{input_value} is character type")
            else:
                print(f"{input_value} is string type")
