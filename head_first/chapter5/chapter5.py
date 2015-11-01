def sanitize(time_string):
		if '-' in time_string:
				splitter = '-'
		elif ':' in time_string:
				splitter = ':'
		else:
				return(time_string)
		(mins,secs) = time_string.split(splitter)
		return(mins+'.'+secs)

def open_file(file):
		try:
				with open(file) as people_file:
						data=people_file.readline()
				return(data.strip().split(','))
		except IOError as ioerr:
				print('File error:'+ str(ioerr))
				return(None)


james = open_file('james.txt')
julie = open_file('julie.txt')
mikey = open_file('mikey.txt')
sarah= open_file('sarah.txt')

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

print(sorted(set(sanitize(t) for t in james))[0:3])
print(sorted(set(sanitize(t) for t in julie))[0:3])
print(sorted(set(sanitize(t) for t in mikey))[0:3])
print(sorted(set(sanitize(t) for t in sarah))[0:3])
