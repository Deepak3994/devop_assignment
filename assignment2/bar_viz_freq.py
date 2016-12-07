#-------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("viz_freq.txt", header=None)
name = df[0]
count = df[1]

y_pos = np.arange(len(name))

plt.bar(y_pos,count, align='center', alpha=10)
plt.xticks(y_pos,name, rotation = 'vertical')
plt.ylabel('frequency')
plt.title('visuallisation freq')
 
plt.show()

