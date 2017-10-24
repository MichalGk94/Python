class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "%s sec" % self.s

    def __repr__(self):
        return "Time(%s)" % self.s

time1 = Time(12)
time2 = Time(3456)
print time1, time2            # Python wywoluje str()
print [time1, time2]          # Python wywoluje repr()


#Wydruk bez komentarzy
#12 sec 3456 sec
#[Time(12), Time(3456)]

#Po zakomentowaniu metody _str_
#Time(12) Time(3456)
#[Time(12), Time(3456)]

#Po zakomentowaniu metody _repr_
#12 sec 3456 sec
#[<__main__.Time instance at 0x7f8506297758>, <__main__.Time instance at 0x7f85062977e8>]

