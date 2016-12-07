import pandas as pd
import matplotlib.pyplot as plt
import pylab
import matplotlib
import numpy as np

df = pd.read_csv("web_count.csv", header=None)
result=df.sort_index(by=[1],ascending = [False])

result = result[result[1] > 10]
result = result[result[1] < 300]

name = result[0]
visits = result[1]

y_pos = np.arange(len(name))

plt.bar(y_pos, visits, align='center', alpha=10)
plt.xticks(y_pos,name, rotation = 'vertical')
plt.ylabel('visits')
plt.title('browse history')
plt.show()
