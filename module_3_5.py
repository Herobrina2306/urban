def get_multiplied_digits(namber):
    str_namber = str(namber)
    first = int(str_namber[0])
    if len(str_namber) > 1:
        first = first * get_multiplied_digits(int(str_namber[1:]))
        return first
    else:
        return first


result = get_multiplied_digits(40203)
print(result)