# DATUMO task
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime
import os
import sys
from typing import List, Union, Any

os.system("")


class Style():
    """
    class with definition of colors - used for coloring the text while printing it
    """
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
    """
    Sorts 2 numbers in pair
    :param pair:of two numbers
    :return: sorted pair of two numbers in ascending order
    """
    a = pair[0]
    b = pair[1]
    if pair[0] > pair[1]:
        sortedPair = [b, a]
    else:
        sortedPair = [a, b]

    return sortedPair


def read_numbers_from_file(file_path):
    """
    Reads input data form file_path

    input file delimiter should be:
    ";" OR  ","

    If file is not found it thorws an exception and exits

    :param file_path: string with file path to read input form
    :return: numbers: numbers form file as list


    """
    try:
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read()
            if content.__contains__(";"):
                numbers = [int(num.strip()) for num in content.split(';')]
            elif content.__contains__(","):
                numbers = [int(num.strip()) for num in content.split(',')]
            else:
                print(f"Error: The file '{file_path}' contains different separator than \";\" or \",\" or it is empty "
                      f"file or contains float numbers or string - check content")
                sys.exit("Terminating the program")

        return numbers

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

        sys.exit("Terminating the program")

    except ValueError:
        print("Error: The file argument contains rubbish - fix It")
        sys.exit("Terminating the program")


def write_numbers_to_file(file_path, output):
    """Write list to files
    if path contains directory that do not exists it creates it.
    Keyword arguments:
    file_path -- string with file path to write output to it
    output -- list/array to write to file
    """

    print(f"Starting writing to file {file_path}.")
    # Extract the directory from the file path
    directory = os.path.dirname(file_path)

    # Check if the directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")

    try:
        with open(file_path, 'w') as file:
            for item in output:
                file.write(f"{item}\n")
        print(f"List successfully written to {file_path}")
        success = True
        return success
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit("Terminating the program")


def find_pairsOn(input_array, target_sum):
    """
    Optimized version of finding all pairs in the array that sum to target_sum.

    :param input_array: array/list with integer numbers
    :param target_sum: value of target sum of two elements

    :returns:
    results - array with results - contains pairs of numbers. Each pair sums to target_sum
    leftovers - array with numbers - that are not summing to target_sum
    """
    seen = set()  # To store elements we've seen so far
    results = []  # To store pairs that sum to target_sum
    leftovers = []  # To store numbers that don't form any pair

    for num in input_array:
        complement = target_sum - num
        if complement in seen:
            # We found a pair
            pair = sorted([num, complement])
            results.append(pair)
            seen.remove(complement)  # Remove complement to avoid pairing again
        else:
            seen.add(num)  # Add current number for future pair checking

    leftovers = list(seen)  # Remaining elements in `seen` are leftovers
    return results, leftovers



def find_pairs(input_array, target_sum):
    """
    Find all pairs in the array that sum to the target_sum.

    :param input_array: array/list with integer numbers
    :param target_sum: value of target sum of two elements

    :returns:
    results - array with results - contains pairs of numbers. Each pair is sum's to target_sum
    leftovers - array with numbers - that are not summing to target_sum
    """

    array = input_array.copy()
    i = 0
    run = True
    leftovers = []
    results = []
    while run:
        array_size = len(array)
        if i >= array_size:
            break

        element = array[i]
        for k in range(1, array_size):
            if element + array[k] == target_sum:
                print(Style.MAGENTA + f"FOUND sum of 2 elements equal to {target_sum} = {array[i]} + {array[k]} " + Style.RESET)
                pair = sort_pair([element, array[k]])
                results.append(pair)
                array.pop(k)
                array.pop(i)
                break

        if i + 1 >= len(array):
            run = False
        else:
            i += 1
    leftovers = array
    return results, leftovers


def get_time_stamp():
    """
    Return the timestamp in proper format
    :return: timestamp -as formatted string %Y.%m.%d__%H-%M-%S-%f

    """
    time_stamp = datetime.now()
    time_stamp_str = time_stamp.strftime('%Y.%m.%d__%H-%M-%S-%f')[:-3]  # Format as a readable string
    return time_stamp_str
