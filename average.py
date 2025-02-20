import numpy as np
import os

#averaging multiple data files

state = 'Z3'
boundary = "PBC"

base_path =''

# List of folder names
folders = [f'run{i}' for i in range(1, 11)]

# Common file name in each folder
file_name = "Intensity_PXP_16_"+state+boundary+".dat"

# Initialize an empty list to store all the third column data
all_lines_data = []

# Loop through each folder and process the files
for folder in folders:
    file_path = os.path.join(base_path, folder, file_name)
    if os.path.exists(file_path):
        # Load the third and fourth columns, specifying the tab delimiter
        data = np.genfromtxt(file_path, delimiter='\t', usecols=(2, 3))
        
        # Check if data is loaded
        if data.size > 0:
            # If this is the first file being processed, initialize the list of lists
            if not all_lines_data:
                all_lines_data = [[row[0]] for row in data]
            else:
                for i, row in enumerate(data):
                    all_lines_data[i].append(row[0])
        else:
            print(f"No data found in file: {file_path}")
    else:
        print(f"File not found: {file_path}")

# Calculate the average of the third column for each line
avg_lines = [np.mean(line_data) for line_data in all_lines_data]

# Load the fourth column data from the first file
fourth_col_data = []
if all_lines_data:  # Ensure there's data to process
    first_file_path = os.path.join(base_path, folders[0], file_name)
    if os.path.exists(first_file_path):
        # Only need to load the fourth column now
        fourth_col_data = np.genfromtxt(first_file_path, delimiter='\t', usecols=(3))

# Prepare the output data
output_data = np.column_stack((fourth_col_data, avg_lines))

# Define the output file path 
output_file_path = 'average'+boundary+'.dat'

# Write the output data to a .dat file, ensuring tab delimiter for consistency
np.savetxt(output_file_path, output_data, delimiter='\t', fmt='%f')

print(f"Process completed, data written to {output_file_path}")