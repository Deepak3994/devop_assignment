#Class that is used to read the git log output and divide according to the different variables
class GitExtract:
	def __init__(self,input):
		self.commit_id = []
		self.author_name = []
		self.author_mail = []
		self.day = []
		self.month = []
		self.year = []
		self.date = []
		self.time = []
		self.message = []
		self.message_length = 0
		self.word_count = 0
		self.list_words = []
		self.list_words_unique = []
		self.count = []
		self.read_file(input)

#To read a given input file
	def read_file(self,input):
		infile = open(input,"r")
		for record in infile:
			if record != '\n':
				self.string_split = record.split()
				#print(string_split)
				if self.string_split[0] == "commit":
					self.process_commit()
				elif self.string_split[0] == "Author:":
					self.process_author()
				elif self.string_split[0] == "Date:":
					self.process_date()
				else:
					self.process_message()

		#print(self.message_length,self.word_count)
#Stores all commit ids
	def process_commit(self):
		self.commit_id.append(self.string_split[1]) 
		return

#Stores all authors name
	def process_author(self):
		self.author_name.append(self.string_split[1])
		self.author_mail.append(self.string_split[2])
		return

#Stores day,month,date,time,year
	def process_date(self):
		self.day.append(self.string_split[1])
		self.month.append(self.string_split[2])
		self.date.append(self.string_split[3])
		self.time.append(self.string_split[4])
		self.year.append(self.string_split[5])
		return

#Stores the messages
	def process_message(self):
		message = ""
		for word in self.string_split:
			if message == "":
				message = message + word
				self.word_count += 1
			else:
				message = message + " " +word
				self.word_count += 1
		self.message.append(message)
		self.message_length += len(message)
		return

#Calculates the no.of occurance of word
	def freq_count(self,file):
		count = 0
		for message in self.message:
			message_split = message.split()
			for word in message_split:
				self.list_words.append(word)
		self.list_words_unique = list(set(self.list_words))
		for word in self.list_words_unique:
			for text in self.list_words:
				if word == text:
					count += 1
			self.count.append(count)
			count =0
		outfile = open(file,"w")
		for i in range(len(self.list_words_unique)):
			if self.count[i] > 1:
				message = self.list_words_unique[i]+ "," + str(self.count[i])
				outfile.write(message)
				outfile.write('\n')

	def get_avg_length(self):
		return self.message_length/len(self.message)

	def get_avg_word_count(self):
		return self.word_count/len(self.message)

#Gets the count of each day
	def get_day_count(self,file):
		count_list = []
		count = 0
		day_list = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
		for day in day_list:
			for d in self.day:
				if day == d:
					count += 1
			count_list.append(count)
			count = 0
		outfile = open(file,'w')
		for i in range(len(day_list)):
			message = day_list[i] + "," + str(count_list[i])
			outfile.write(message)
			outfile.write('\n')		