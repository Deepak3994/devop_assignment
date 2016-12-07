class Stud_Marks:
	def __init__(self):
		self.in_file = open("data.csv","r")
		self.out_file = open("total.csv","w")
		self.out_file2 = open("sub_tot.csv","w")
		self.subject1 = []
		self.subject2 = []
		self.subject3 = []
		self.subject4 = []
		self.subject5 = []
		
#Function to calculate the total of each student in each subject
	def cal_total(self):
		count = 1
		for record in self.in_file:
			total = 0
			marks_split = record.split(",")
			subj1 = marks_split[1]
			self.subject1.append(subj1) 
			subj2 = marks_split[2]	
			self.subject2.append(subj2)
			subj3 = marks_split[3]
			self.subject3.append(subj3)
			subj4 = marks_split[4]
			self.subject4.append(subj4)
			subj5 = marks_split[5]
			#print(subj5)
			self.subject5.append(subj5)
			total = int(subj1)+int(subj2)+int(subj3)+int(subj4)+int(subj5)
			avg = (float(total))/5.0 
			#print(avg)
			message = str(count)+","+str(total)+","+str(avg)+",0"+"\n"
			self.out_file.write(message)
			count += 1

#Function to calculate the total of every student in all subjects
	def cal_tot_subj(self):
		sub1_tot = 0
		sub2_tot = 0
		sub3_tot = 0
		sub4_tot = 0
		sub5_tot = 0
		for i in range(len(self.subject1)):
			sub1_tot = sub1_tot + int(self.subject1[i])
			sub2_tot = sub2_tot + int(self.subject2[i])
			sub3_tot = sub3_tot + int(self.subject3[i])
			sub4_tot = sub4_tot + int(self.subject4[i])
			sub5_tot = sub5_tot + int(self.subject5[i])
		avg1 = float(sub1_tot)/18.0
		avg2 = float(sub2_tot)/18.0
		avg3 = float(sub3_tot)/18.0
		avg4 = float(sub4_tot)/18.0
		avg5 = float(sub5_tot)/18.0 
		message1 = "subject1," + str(sub1_tot) + "," +str(avg1)+",0"+"\n"
		message2 = "subject2," + str(sub2_tot) + "," +str(avg2)+",0"+"\n"
		message3 = "subject3," + str(sub3_tot) + "," +str(avg3)+",0"+"\n"
		message4 = "subject4," + str(sub4_tot) + "," +str(avg4)+",0"+"\n"
		message5 = "subject5," + str(sub5_tot) + "," +str(avg5)+",0"+"\n"
		self.out_file2.write(message1)
		self.out_file2.write(message2)
		self.out_file2.write(message3)
		self.out_file2.write(message4)
		self.out_file2.write(message5)

students = Stud_Marks()
students.cal_total()
students.cal_tot_subj()