import data.preprocess_filenames as pf
import data.snr as snr
import data.plotter as plot

# app loads and preprocess input data from input directory
__imported_files = pf.get_sorted_data()
# prepared data set with xy's
__extracted_dataset = snr.extracted_xy_dataset(__imported_files)

output = snr.output_array(__extracted_dataset, __imported_files)

for i in range(0, len(output)):
    print(f'{output[i][0]}K: snr value: {output[i][1]}')

#plot.plot_xy(__extracted_dataset[0][0], __extracted_dataset[0][1])
#print(snr.signaltonoise(__extracted_dataset[0][1]))