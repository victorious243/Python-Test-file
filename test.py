# def find_common_chars(lst):
#     if not lst:
#         return set()
#     first_item = lst[0]
#     common_chars = set()
#     for char in first_item:
#         if all(char in item for item in lst):
#             common_chars.add(char)
#     return common_chars
#
#
# # Example usage:
# lst = ["apple", "banana", "cherry"]
# common_chars = find_common_chars(lst)
# if common_chars:
#     print(f"The common characters are: {', '.join(common_chars)}")
# else:
#     print("No common characters found.")

# for i in x:
#     if i > 0:
#         y = x.count(i)
#     print("\nCharacter o appears in all items")
#     for i in x:
#         y = i.count('o')
#         if i.count('o'):
#             print(f"{i} contains {y} o")

#
# def function2(x):
#     print("\nCommon character check: \nCharacter b appears in all items")
#     for i in x[0]:
#         found = True
#         for a in x:
#             if i in a:
#                 y = i.count(i)
#                 list3.append(y)
#                 y = + 1
#                 print(y)
#                 print(list3)
#
#
#                 if y > 5:
#                     val = i.count(i)
#                     print(val)
# print(i)
# if character[a] > 2:
#     print("yes")
# if character > 2
# print(character)

# import random
# import time
#
#
# def function1(x, z):
#     i = 0
#     while i < len(x):
#         i += 1
#         movie = random.choice(x)
#         for y in x:
#             if y == movie:
#                 x.remove(y)
#                 print(f"{y} was eliminated\n")
#         print(f"{len(x)} remaining \n{x}")
#         if i == z:
#             print(f"Game over {len(x)} players are the winners ")
#             break
#         time.sleep(2)
#
#
# def main():
#     list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L']
#     players = int(input("Enter the number of players to be eliminate >> "))
#     while players < 2 or players > 6:
#         players = int(input("Enter the number of players to be eliminate \nWARNING ENTER NUMBER BETWEEN 2-6 >> "))
#     function1(list1, players)
#
#
# if __name__ == '__main__':
#     main()
# pick a random choice from a list of strings.
# movie = random.choice(movies_list)
# print(movie)
# # Output 'The Shawshank Redemption'
#
# for i in range(2):
#     while movie == random.choice(movies_list):
#         print(movie)

# Output
# 'Citizen Kane'
# 'The Shawshank Redemption'
# for i in movies_list:
#     print(i)
#     time.sleep(2)

# def print_list(name):
#     delete = int(input("Enter an element by index >> "))
#     while delete < 0 or delete > 4:
#         delete = int(input("WARNING!! \nEnter an element by index 0-4 >> "))
#     for i in name:
#         name.pop(delete)
#         print(f"{i}")
#
#         # print(i)
#
#
# def main():
#     counties = ["Kerry", "Cork", "Waterford", "Limerick", "Tip"]
#     print_list(counties)
#
#
# if __name__ == '__main__':
#     main()
#
# def get_totsl_even_num(numbers):
#     running_total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             running_total += num
#     return running_total
#
#
# def main():
#     ages = [10, 22, 13, 14, 19]
#     total = get_totsl_even_num(ages)
#     print(f"The total is {total}")
#
#
# if __name__ == '__main__':
#     main()

def adding(x):
    number = int(input("How many numbers do you want to add to the list? "))
    for i in range(number):
        num = int(input("Please enter number >> "))
        while 0 <= num >= 10:
            num = int(input("Please enter number >> \nWARNING!! INSERT 0-10 >"))
        x.append(num)


def main():
    list1 = []
    adding(list1)
    print(f"You created the following list : {list1}")


if __name__ == '__main__':
    main()