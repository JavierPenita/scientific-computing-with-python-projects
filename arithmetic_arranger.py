def arithmetic_arranger(*args):
    list_one = []
    list_two = []
    list_less = []
    for arg in args:
        for i in arg:
            i = i.split()
            list_one.append("  " + i[0] + "  ")
            list_two.append("+")
            list_two.append(i[2] + "   ")
            list_less.append("-----" + "  ")
    print(' '.join(list_one))
    print(' '.join(list_two))
    print(' '.join(list_less))
            

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43","123 + 149", "101 + 20"])