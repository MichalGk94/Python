def flatten(sequence):
    l = []
    for item in sequence[:]:
        l.extend(flatten(item)) if isinstance(item, (list, tuple)) else l.append(item)
    return l


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print flatten(seq)
