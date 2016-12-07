import GitExtract

class Gitops:
	def __init__(self):
		self.mdbms = GitExtract.GitExtract("modern.txt")
		self.viz = GitExtract.GitExtract("data-viz.txt")
		self.uml = GitExtract.GitExtract("uml.txt")
		
	
	def get_average_length(self):
		mdbms_length = str(self.mdbms.get_avg_length())
		viz_length = str(self.viz.get_avg_length())
		uml_length = str(self.uml.get_avg_length())
		message1 = "mdbms" + "," + mdbms_length
		message2 = "data-viz" + "," + viz_length
		message3 = "uml" + "," + uml_length
		outfile = open("length.txt","w")
		outfile.write(message1)
		outfile.write('\n')
		outfile.write(message2)
		outfile.write('\n')
		outfile.write(message3)
		return

	def get_word_count(self):
		mdbms_count = str(self.mdbms.get_avg_word_count())
		viz_count = str(self.viz.get_avg_word_count())
		uml_count = str(self.uml.get_avg_word_count())
		message1 = "mdbms" + "," + mdbms_count
		message2 = "data-viz" + "," + viz_count
		message3 = "uml" + "," + uml_count
		outfile = open("wc.txt","w")
		outfile.write(message1)
		outfile.write('\n')
		outfile.write(message2)
		outfile.write('\n')
		outfile.write(message3)
		return

	def get_freq_count(self):
		self.mdbms.freq_count("mdbms_freq.txt")
		self.viz.freq_count("viz_freq.txt")
		self.uml.freq_count("uml_freq.txt")
		return

	def get_days_count(self):
		self.mdbms.get_day_count("mdbms_day.txt")
		self.viz.get_day_count("viz_day.txt")
		self.uml.get_day_count("uml_day.txt")

git = Gitops()
git.get_average_length()
git.get_word_count()
git.get_freq_count()
git.get_days_count()