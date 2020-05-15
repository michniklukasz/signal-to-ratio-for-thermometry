class SingleData:
    def __init__(self, filename, temperature):
        # uses ./ instead of ../ because, object is created in parent directory
        self.__data_file_path = r'./input/' + filename
        self.__abs_temperature_integer = temperature
        self.__abs_temperature_string = f'{temperature}K'

    __abs_temperature_integer = 999
    __abs_temperature_string = ':)'
    __data_file_path = ''
    __splitted_data = []
    __first_extracted_row = 0
    __extracted_data = []

# just splits data text separatet by ';'.
    def split_all_data(self):
        data_file_path = self.__data_file_path
        splitted_data = []
        with open(data_file_path, 'r') as file:
            for row in file:
                splitted_row = row.split(',')
                splitted_data.append(splitted_row)
        self.__splitted_data = splitted_data

# every splitted line has ['\n'], so empty line should have only one item in array -> just ['\n']
    def find_first_idx(self):
        first_extracted_row = 0
        for idx, item in enumerate(self.__splitted_data):
            while len(item) == 1:
                first_extracted_row = idx
                break
        self.__first_extracted_row = first_extracted_row

# takes only data, withoud headers in file
    def extract_data(self):
        #może dodać jakiś walidator zanim sie przypisze, zeby sprawdzic czy ok?
        splitted_data = self.__splitted_data
        first_extracted_row = self.__first_extracted_row
        ext_x = []
        ext_y = []
        for idx, item in enumerate(splitted_data):
            while idx > first_extracted_row:
                ext_x.append(float(item[0]))
                ext_y.append(float(item[1]))
                break
# return array with data and header in line 1 !
        #self.__extracted_data = [['x-axis'] + ext_x, [self.__abs_temperature] + ext_y]
        self.__extracted_data = [ext_x, ext_y]

    def stack(self):
        self.split_all_data()
        self.find_first_idx()
        self.extract_data()
        return self.__extracted_data










