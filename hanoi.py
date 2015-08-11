def hanoi(n, source, dest, temp):
    if n == 1:
        dest.append(source.pop())
        hanoi_print()
    else:
        hanoi(n-1, source, temp, dest)
        dest.append(source.pop())
        hanoi_print()
        hanoi(n-1, temp, dest, source)


def hanoi_print():
    global n
    width = 3 * (2 * n + 1) + 4
    for x in range(n, 0, -1):
        line = " "
        for lst in [list1, list2, list3]:
            if len(lst) >= x:
                line += lst[x-1] + " "
            else:
                line += "|".center(2*n+1) + " "
        print(line)
    print('-' * width)
    print('\n')
    input("")

if __name__ == '__main__':
    n = int(input("How many discs? >> "))
    input("Press Enter to show the next step.")
    list1 = []
    list2 = []
    list3 = []
    for x in range(n):
        list1.append(('-'*(n-x) + '+' + '-'*(n-x)).center(2*n+1))
    hanoi_print()
    hanoi(n, list1, list3, list2)
