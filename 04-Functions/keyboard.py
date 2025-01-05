###
# Functions to read any data type from the keyboard
#
def input_string(message):
    x = input(message)
    return str(x)

def input_integer(message):
    y = input(message)
    return int(y)

def input_real(message):
    z = input(message)
    return float(z)

def input_boolean(message):
    w = input(message)
    return bool(w)