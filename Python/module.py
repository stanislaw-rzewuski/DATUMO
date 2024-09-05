# DATUMO task
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import sys
from typing import List, Union, Any

os.system("")


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


def sort_pair(pair):
    a = pair[0]
    b = pair[1]
    if pair[0] > pair[1]:
        sortedPair = [b, a]
    else:
        sortedPair = [a, b]

    return sortedPair


def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read()

            # Split the content by commas and convert each item to an integer
            numbers = [int(num.strip()) for num in content.split(',')]

        return numbers

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

        sys.exit("Terminating the program")

    except ValueError:
        print("Error: The file contains non-integer values.")
        sys.exit("Terminating the program")


#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # array = array.array('i', [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0])
#     InputArray = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
#     array = InputArray.copy()
#     results = []
#     i = 0
#     run =1
#
#     while run == 1:
#         arraySize = len(array)
#         element = array[i]
#
#         for k in range(1, len(array)):
#
#             print(f"i={i}, k={k} inspected element = {element} and {array[k]}")
#             if element + array[k] == 12:
#                 print(style.RED +"FOUND sum of 2 elements equal to 12")
#                 print(f"i={i}, k={k}, pair=[{element},{array[k]}]"+ style.RESET)
#                 pair = [element, array[k]]
#                 pair = sortPair(pair)
#                 results.append(pair)
#                 print(f"Array  before modification: {array}")
#                 print(f"arraySize {arraySize}")
#                 array.pop(k)
#                 array.pop(i)
#                 arraySize = len(array)
#                 print(f"Array  after  modification: {array} ")
#                 print(f"arraySize {arraySize}")
#
#                 print(f"Input  array: {InputArray} ")
#                 print(f"InputArray Size = {len(InputArray)}")
#                 break
#             else:
#                 print()
#                 # print(f"elements do not sum  to 12 i={i}, k={k}, pair=[{element},{array[k]}]")
#                 # print(f"array lenght = {len(array)}")
#         #
#         print(f"k loop increasing i+1 i={i}, k={k} , arraySize={arraySize}")
#         if i+1 >= arraySize:
#             print(f"HAND breaking")
#             print(array)
#             run = 0;
#             break
#         i = i + 1;
#     #end of while
#
#     # let's print the results at the end
#     print(style.GREEN + "\nOUTPUT: lets print the results")
#     print(f" Input array= {InputArray}")
#     print(f" Results array= {results}")
#
#     print(f" Left overs array = {array}"+style.RESET)
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
