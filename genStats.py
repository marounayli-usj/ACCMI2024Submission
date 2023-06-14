
import numpy as np 
import csv
data = []
dat=[]
with open('scores.txt', 'r') as file:
    for line in file:
        if line.startswith("#"):
            data.append(dat)
            dat=[]
        else:
            dat.append(float(line.split(" ")[1]))
header = ['maximum_score' , 'standard deviation' , 'median' , 'median absolute deviation']
with open("metrics.csv" , "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for vector in data:
        if len(vector) > 0:
        # Create a list of values 
            maxi = np.max(vector)

            # Calculate standard deviation
            stdev = np.std(vector) 

            # Calculate median
            median = np.median(vector) 

            # Calculate median absolute deviation
            mad = np.median(np.abs(vector - median))
            r = [maxi,stdev,median,mad]
            writer.writerow(r)
            