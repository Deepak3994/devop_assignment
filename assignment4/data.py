import random

#Creating an empty list 
subj1=[]
subj2=[]
subj3=[]
subj4=[]
subj5=[]

#Generating random numbers for each subjects
for i in range(18):
	subj1.append(random.randint(25,50))
	subj2.append(random.randint(15,50))
	subj3.append(random.randint(25,45))
	subj4.append(random.randint(25,40))
	subj5.append(random.randint(10,50))

#opening a file
output_file = open("data.csv","w")
count = 1
for i in range(18):
	message = str(count)+","+str(subj1[i]) + "," +str(subj2[i]) + "," +str(subj3[i]) + "," +str(subj4[i]) + "," +str(subj5[i]) + ",0" +"\n"
	output_file.write(message)
	count += 1 