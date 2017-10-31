X = "qwerty"

def func():
    print X

func()
#kod wyswietla "qwerty" poniewaz taka jest wartosc zmiennej X

X = "qwerty"

def func():
    X = "abc"

func()
print X
#kod wyswietla "qwerty" poniewaz X = abc
#odnosi sie do lokalnej wewnetrnej zmiennej X

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print X
#kod wyswietla "abc" poniewaz zmieniam wartosc globalnej zmiennej
