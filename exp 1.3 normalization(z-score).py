import csv
import statistics
def z_score_normalization(input_file,output_file):
    with open(input_file,'r') as file:
        reader =csv.reader(file)
        data=[float(row[0]) for row in reader]
    mean_value=statistics.mean(data)
    standard_dev=statistics.stdev(data)
    z_scored_data=[(x-mean_value)/standard_dev for x in data]
    with open(output_file,'w',newline="") as file:
        writer = csv.writer(file)
        for value in z_scored_data:
            writer.writerow([value])
if __name__ == "__main__":
    input_file="data.csv"
    output_file = "z_scord_data1.csv"
    z_score_normalization(input_file,output_file)
