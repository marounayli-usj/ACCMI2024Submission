import matplotlib.pyplot as plt
import numpy as np
import os
import heapq as hq
import matplotlib
folder_path = 'plots/'

# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted {filename}")

data = [] 
dat = []

with open('scores.txt', 'r') as file:
    for line in file:
        if line.startswith("#"):
            data.append(dat)
            dat=[]
        else:
            dat.append(float(line.split(" ")[1]))
    data.append(hq.nlargest(50,dat))

fig, axes = plt.subplots(nrows=2, ncols=5)

data=data[1:]
for i, ax in enumerate(axes.flat):
    if i < 10:
        x= np.linspace(0,len(data[i]),len(data[i]))

        if len(x) ==0:
            continue
        ax.set_yscale('linear')
        ax.boxplot(data[i])
        ax.set_title(f'Dataset {i+1}')
    else:
        ax.axis('off')


# Automatically adjust subplot layout to make them fit in the figure
fig.tight_layout()

# Display the plot
plt.show()
# for i in range(len(data)):
#     x= np.linspace(0,len(data[i]),len(data[i]))
#     if len(x) ==0:
#         continue
#     colors = np.random.rand(len(data[i]))
#     # p =  plt.scatter(x,data[i], cmap='viridis', alpha=0.8)
#     # p.set_xlabel('Element number', fontsize=12, fontname='Arial')
#     # p.set_ylabel('Similarity Score', fontsize=12, fontname='Arial')
#     # p.set_title('A Beautiful Scatter Plot', fontsize=16, fontname='Times New Roman')
#     fig, ax = plt.subplots()
#     mean = np.mean(x)
#     std_dev = np.std(x)
#     # plt.annotate("Sample size : " + str(len(data[i])), (200,200))
#     # y_values = 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std_dev)**2)

#     plot = plt.subplot()
#     plot.set_yscale('linear')
#     plot.bar(x,data[i], color='red')
    

#     # scatter = ax.boxplot( y_values)
#     # plt.plot(x, y_values, color='red', linewidth=2)


#     # Add labels and title with custom font
#     ax.set_xlabel('Element number', fontsize=12)
#     ax.set_ylabel('Similarity Score', fontsize=12)

#     # Show the plot

# plt.savefig("plots/plotdata.pgf")
# plt.savefig("plots/plotdata.png")

# plt.clf()
