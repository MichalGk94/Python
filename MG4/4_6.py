def sum_seq(sequence):
    wynik = 0
    for i in range(len(sequence)):
        if isinstance(sequence[i], tuple):
            wynik += sum_seq(sequence[i])
        else:
            wynik += sequence[i]
    return wynik

sequence = (1, 2, 3, (7, 5), 0, (2, (4, 3)), 8)
print sum_seq(sequence)
