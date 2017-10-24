def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    x = raw_input("Podaj liczbe: ")
    if x == "stop":
        break
    elif not is_number(x):
        print "To nie jest liczba!"
    else:
        print x, " ", float(x) ** 3
