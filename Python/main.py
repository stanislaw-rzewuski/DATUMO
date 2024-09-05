from module import *

file_path = ".\\TestData\\input1.txt"
file_path = ".\\TestData\\input2.txt"
InputArray = read_numbers_from_file(file_path)

# InputArray = [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0]
array = InputArray.copy()
results = []
i = 0
run = 1

while run == 1:
    arraySize = len(array)
    element = array[i]

    for k in range(1, len(array)):

        print(f"i={i}, k={k} inspected element = {element} and {array[k]}")
        if element + array[k] == 12:
            print(style.MAGENTA + "FOUND sum of 2 elements equal to 12")
            print(f"i={i}, k={k}, pair=[{element},{array[k]}]" + style.RESET)
            pair = [element, array[k]]
            pair = sort_pair(pair)
            results.append(pair)
            array.pop(k)
            array.pop(i)
            arraySize = len(array)
            break

    #
    print(f"k loop increasing i+1 i={i}, k={k} , arraySize={arraySize}")
    if i + 1 >= arraySize:
        print(f"HAND breaking")
        print(array)
        run = 0;
        break
    i = i + 1;
# end of while

# let's print the results at the end
print(style.GREEN + "\nOUTPUT: lets print the results")
print(f" Input array= {InputArray}")
print(f" Results array= {results}")
print(f" Left overs array = {array}" + style.RESET)
