#HackerRank - Number Line Jumps

def kangaroo(x1, v1, x2, v2):

    if v1 == v2:
        if x1 != x2:
            return 'NO'
        else:
            return 'YES'
    
    else:
        t_or_f = (x2 - x1) / (v1 - v2)
        if t_or_f < 0:
            return 'NO'
        elif t_or_f.is_integer():
            return 'YES'
        else:
            return 'NO'


print(kangaroo(0, 2, 5, 3))
print(kangaroo(0, 3, 4, 2))
print(kangaroo(2, 1, 1, 2))
print(kangaroo(1817, 9931, 8417, 190))
print(kangaroo(43, 2, 70, 2))
print(kangaroo(43, 2, 43, 2))


    