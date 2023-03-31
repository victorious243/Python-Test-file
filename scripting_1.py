from statistics import mode


def function1(x):
    print("Hash marks and no m check:")
    for i in x:
        if not i.startswith('m') & i.find('#'):
            print(f"{i} contains hash mark and does not start with m")


def function2(x):
    print("\nCommon character check: \nCharacter b appears in all items")
    for i in x:
        # most_common = max(set(i), key=i.count)
        most_common = mode(i)
        if i.count(most_common) > 1:
            print(f"{i} contains {i.count(most_common)} {most_common}")
        else:
            print(f"{i} contains 0 common character")


def main():
    list1 = ["boby#", "borya#n", "#malllibons#", "morbs", "mobking#", "bunst#or"]
    function1(list1)
    function2(list1)


if __name__ == '__main__':
    main()
