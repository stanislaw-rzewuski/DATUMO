import re

from helpers_module import *

# Main program execution

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_csv_file>")
    else:
        file_path = sys.argv[1]

    time_stamp = get_time_stamp()

    output_file_name = re.search(r"\\([^\\]+)\....$", file_path).group(1)
    output_file_name = f"{time_stamp}_{output_file_name}"
    output_path = f".\\TestsOutput\\{output_file_name}.out"

    InputArray = read_numbers_from_file(file_path)

    results, leftovers = find_pairs(InputArray, 12)

    # let's print the results at the end
    print(Style.GREEN + "\nOUTPUT: lets print the results")
    print(f" Input array= {InputArray}")
    write_numbers_to_file(output_path, InputArray)
    print(f" Results array= {results}")
    print(f" Left overs array = {leftovers}" + Style.RESET)

    is_file_write_OK = write_numbers_to_file(output_path, results) # results file format is not covered by requirements
    if is_file_write_OK == False:
        print(Style.RED + f" Something went wrong with file writting" + Style.RESET)
