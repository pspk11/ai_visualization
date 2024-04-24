import csv
import statistics
import numpy as np
import pandas as pd

def remove_mean(input_file,output_file):
    with open(input_file,'r') as file:
        reader = csv.reader(file)
        data=[float(row[0]) for row in reader]
    mean_value=statistics.mean(data)
    mean_removed_data = [x - mean_value for x in data]
    with open(output_file,'w',newline="") as file:
        writer = csv.writer(file)
        for value in mean_removed_data:
            writer.writerow([value])
if __name__ == "__main__":
    input_file="data.csv"
    output_file = "mean_removed_data2.csv"
    remove_mean(input_file,output_file)
