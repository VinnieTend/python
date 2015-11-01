def sanitize(time_string):
		if '-' in time_string:
				splitter = '-'
		elif ':' in time_string:
				splitter = ':'
		else:
				return(time_string)
		(mins,secs) = time_string.split(splitter)
		return(mins+'.'+secs)



class Athlete:
		def __init__(self,a_name,a_dob=None,a_times=[]):
				self.name=a_name
				self.dob=a_dob
				self.times = a_times

		def top3(self):
				return(sorted(set([sanitize(t) for t in self.times]))[0:3])
		def add_time(self,time_value):
				self.times.append(time_value)
		def add_times(self,time_values):
				self.times.extend(time_values)

class AthleteList(list):
		def __init__(self,a_name,a_dob=Name,a_times=[]):
				list.__init__([])
				self.name=a_name
				self.dob=a_dob
				self.extend(a_times)
		def top3(self):
				return(sorted(set([sanitize(t) for t in self]))[0:3])



def open_file(file):
		try:
				with open(file) as people_file:
						data=people_file.readline()
						temp1=data.strip().split(',')
						temp2=Athlete(temp1.pop(0),temp1.pop(0),temp1)
						return(temp2)
		except IOError as ioerr:
				print('File error:'+ str(ioerr))
				return(None)

james = open_file('james2.txt')
julie = open_file('julie2.txt')
mikey = open_file('james2.txt')
sarah = open_file('sarah2.txt')
print(james.name+ "'s fastest times are:"+str(james.top3()))
print(julie.name+ "'s fastest times are:"+str(julie.top3()))
print(mikey.name+ "'s fastest times are:"+str(mikey.top3()))
print(sarah.name+ "'s fastest times are:"+str(sarah.top3()))

vera = Athlete('Vera Vi')
vera.add_time('1.31')
vera.add_times(['2.22','1-21','2:22'])

print(vera.top3())




