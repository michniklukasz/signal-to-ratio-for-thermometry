import data.single_data as sd
import numpy as np


def extracted_xy_dataset(files_list):
    # just if needed in future
    data_objects = []
    # data width spectra xy
    processed_dataset = []

    for file in files_list:
        # for creating and array with data from taken files, this class takes filename and temperature from files_list
        data_instance = sd.SingleData(file[1], file[0])
        # save every object to data_objects to have for future
        data_objects.append(data_instance)
        # import data from input directory and process data
        # returns processed data
        processed_data_instance = data_instance.stack()
        processed_dataset.append(processed_data_instance)
    return processed_dataset


def signaltonoise(ydata, axis=0, ddof=0):
    ydata = np.asanyarray(ydata)
    m = ydata.mean(axis)
    sd = ydata.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)


def output_array(data, temps):
    out_arr = []
    for i in range(0, len(temps)):
        temp = temps[i][0]
        snr = float(signaltonoise(data[i][1]))
        out_arr.append([temp, snr])
    return out_arr


