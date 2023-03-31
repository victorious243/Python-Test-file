

def table_of_5():
    i = 0
    while i < 12:
        i = i + 1
        calcule = i * 1
        print(f"{i} * 5 = {calcule}")


ecole = []


def main():
    count = 0
    for i in range(5):
        count = count + 1
        classic = str(input(f"Enter a name of school {count} here >> "))
        ecole.append(classic)
    print(ecole)
    # table_of_5()
    # for i in range(13):
    #     # print(i)
    #     calcul = i * 5
    #     print(f"{i} * 5 = {calcul}")
    return 0


if __name__ == '__main__':
    main()
