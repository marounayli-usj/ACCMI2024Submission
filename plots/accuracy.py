import numpy as np
import pandas as pd

data= []
index=-1


with open("scores.txt" , "r") as f:
    for r in f.readlines():
        r=r.strip()
        if r.startswith("#"):
            data.append([])
            index+=1
        else:
            x,y = r.split(" ")
            data[index].append(float(y))


def detect_outliers_iqr(array):
   
    Q1 = np.percentile(array, 25)
    Q3 = np.percentile(array, 75)


    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    
    outliers = (array < lower_bound) | (array > upper_bound)
    extreme_outliers = (array < Q1 - 3 * IQR) | (array > Q3 + 3 * IQR)

    return outliers, extreme_outliers





df = pd.DataFrame()

for i, arr in enumerate(data):
    arr = np.array(arr)
    sorted_array = np.sort(arr)

    outliers, extreme_outliers = detect_outliers_iqr(sorted_array)

    extreme_values = sorted_array[extreme_outliers]

    mean = np.mean(arr)
    median = np.median(arr)
    mean_distance = np.abs(extreme_values - mean)
    median_distance = np.abs(extreme_values - median)
    distance_last_second_last = sorted_array[-1] - sorted_array[-2]
    distance_last_second_last_ratio = (sorted_array[-1] - sorted_array[-2]) / (sorted_array[2])

    # Create a dictionary where each statistic corresponds to a key-value pair
    stats = {
        'Array ID': [i+1],
        'Mean': [mean],
        'Median': [median],
        'Distance between Mean and Median': [np.abs(mean - median)],
        'Distance between Highest and Second Highest Value': [distance_last_second_last],
        'Max 1 Max 2 Ratio' : [distance_last_second_last_ratio]
    }

    # Create a DataFrame from the dictionary and append it to the existing DataFrame
    temp_df = pd.DataFrame(stats)
    df = pd.concat([df, temp_df], ignore_index=True)

print(df)



df.to_excel('output.xlsx', index=False)
