import re
from os import listdir
from os.path import isfile, join


# uses ./ instead of ../ because, object is created in parent directory
__input_files_path = './input'
__regex_temperature = r'\d{2,3}(k|K)'


def get_raw_data():
    return [f for f in listdir(__input_files_path) if isfile(join(__input_files_path, f))]


# IMPORTANT, REGEX MATCHES ONLY INTEGERS at the moment
def get_sorted_data():
    raw_data = get_raw_data()
    unsorted_files = []
    # uses re object to search matching temperature information in file name
    if len(raw_data) > 0:
        for file in raw_data:
            # searches and uppercases kelwin unit, in case of lowwercase 'k' instead of 'K' letter in file name string
            abs_temperature_with_unit = re.search(__regex_temperature, file).group(0).upper()
            # deletes unit to change type to number and use to sort
            abs_temperature_without_unit = int(abs_temperature_with_unit.replace('K', ''))
            # create list of tuples, for use a temperature as sorting value
            unsorted_files.append((abs_temperature_without_unit, file))
        sorted_files = sorted(unsorted_files, key=lambda temperature: temperature[0])
        return sorted_files
    else:
        print('no data in input folder')



# function creates and array of arrays, for each individual file
# [ temperature in kelvins as integer, 'filename.txt'],[],[],...


