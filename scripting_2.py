import time
import random


def function1(x, z):
    i = 0
    while i < len(x):
        i += 1
        movie = random.choice(x)
        for y in x:
            if y == movie:
                x.remove(y)
                print(f"{y} was eliminated")
        print(f"{len(x)} remaining {x}")
        time.sleep(2)
        if i == z:
            print(f"Game over {len(x)} players are the winners ")
            break



def main():
    list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L']
    players = int(input("Enter the number of players to be eliminate >> "))
    while players < 2 or players > 6:
        players = int(input("Enter the number of players to be eliminate \nWARNING ENTER NUMBER BETWEEN 2-6 >> "))
    function1(list1, players)


if __name__ == '__main__':
    main()
