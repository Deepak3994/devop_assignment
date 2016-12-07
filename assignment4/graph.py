import pandas as pd
import matplotlib.pyplot as plt

#To plot the overall performance of student
sub_total = pd.read_csv('sub_tot.csv')
sub_total =  sub_total[['total','average']]
sub_total.plot(kind='bar', title='Overall performance of students in each subject', rot=0, color=(['r','b']),
                  figsize=(11, 8), edgecolor='w', linewidth=2, width=0.7)
plt.ylabel('<--------- Name of the subjects --------->', fontsize=14, color='m')
plt.xlabel('<--------- Marks obtained --------->', fontsize=14, color='m')
plt.show()

#To plot the performance of students in each subjects
total = pd.read_csv('total.csv')
total = total[['Sub-total','average']]
total.plot(kind='bar', title='Performance of students in each subject', rot=0, color=(['r','b']),
                  figsize=(11, 8), edgecolor='w', linewidth=2, width=0.7)
plt.ylabel('<--------- Marks --------->', fontsize=14, color='m')
plt.xlabel('<--------- Roll numbers --------->', fontsize=14, color='m')
plt.show()
