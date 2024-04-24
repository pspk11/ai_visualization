import csv
def min_max_scaling(input_file,output_file,new_min=0,new_max=1):
    with open(input_file,'r') as file:
        reader =csv.reader(file)
        data=[float(row[0]) for row in reader]
    current_min=min(data)
    current_max=max(data)
    scaled_data=[(x-current_min)/(current_max-current_min)*(new_max-new_min)+new_min for x in data]
    with open(output_file,'w',newline="") as file:
        writer = csv.writer(file)
        for value in scaled_data:
            writer.writerow([value])
if __name__=="__main__":
    input_file="data.csv"
    output_file="scaled_data1.csv"
    min_max_scaling(input_file,output_file)
