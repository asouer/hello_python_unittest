def mileage(vehicle):
    miles = input('Enter new miles for %s: ' % vehicle)
    if floating(miles):
        if positive(miles):
            return float(miles)
    print("Please enter a positive number.")
    return mileage(vehicle)


def positive(input_value):
    if isinstance(input_value, float) or isinstance(input_value, int):
        if input_value >= 0:
            return True
    if integer(input_value):
        if int(input_value) >= 0:
            return True
    if floating(input_value):
        if float(input_value) >= 0:
            return True
    return False


def integer(input_value):
    if isinstance(input_value, int):
        return True
    else:
        try:
            int(input_value)
            return True
        except ValueError:
            return False


def floating(input_value):
    if isinstance(input_value, float):
        return True
    else:
        try:
            float(input_value)
            return True
        except ValueError:
            return False
