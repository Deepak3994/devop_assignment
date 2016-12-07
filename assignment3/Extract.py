class Extract:
	def __init__(self):
		self.input_file = open("history.txt","r")
		self.output_file = open("bda1.csv","w")
		self.split_record = []
		self.date = []
		self.time = []
		self.url = []
		print("done")

	def read_file(self):
		for record in self.input_file:
			self.split_record = record.split(" ")
			self.date.append(self.split_record[0])
			timestring = str(self.split_record[1])
			self.split_record = []
			self.split_record = timestring.split("|")
			self.time.append(self.split_record[0])
			website = str(self.split_record[1])
			website_split = website.split("/")
			self.url.append(website_split[2])
		
	def write_file(self):
		for i in range(len(self.url)):
			message = str(self.date[i]) + "," + str(self.time[i]) + "," + self.url[i] + ",0"	 
			self.output_file.write(message)
			self.output_file.write("\n")

E = Extract()
E.read_file()
E.write_file()