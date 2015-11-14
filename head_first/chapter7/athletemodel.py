import pickle
#from athletelist import AthleteList

# 规范时间格式
def sanitize(time_string):
		if '-' in time_string:
				splitter='-'
		elif ':' in time_string:
				splitter = ':'
		else:
				return(time_string)
		(mins,secs)=time_string.split(splitter)
		return(mins+'.'+secs)

# 继承list的类属性，添加了name,dob,top3的方法
class AthleteList(list):
		def __init__(self,a_name,a_dob=None,a_times=[]):
				list.__init__([])
				self.name=a_name
				self.dob=a_dob
				self.extend(a_times)
		def top3(self):
				return(sorted(set([sanitize(t)]))[0:3])

# 读入文件，然后通过AthleteList 返回每个人的信息
def get_coach_data(filename):
		try:
				with open(filename) as f:
						data = f.readline()
				templ=data.strip().split(',')
				return(AthleteList(templ.pop(0),templ.pop(0),templ))
		except IOError as ioerr:
				print('File error: ' + str(ioerr))
				return(None)

# 将读取get_coach_data中获得的信息，存入到字典中，并保存到pickle文件中
def put_to_store(files_list):
		all_athletes={}
		for each_file in files_list:
				ath = get_coach_data(each_file)
				all_athletes[ath.name]=ath
		try:
				with open('athletes.pickle','wb') as athf:
						pickle.dump(all_athletes,athf)
		except IOError as ioerr:
						print('File error(put_and_store):'+str(ioerr))
		return(all_athletes)

# 读取文件
def get_from_store():
		all_athletes={}
		try:
				with open('athletes.pickle','rb') as athf:
						all_athletes = pickle.load(athf)
		except IOError as ioerr:
						print('File error(get_from_store):'+str(ioerr))
		return(all_athletes)


the_files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data = put_to_store(the_files)

for each_athlete in data:
		print(data[each_athlete].name + ' ' +data[each_athlete].dob)

data1 = get_from_store()
for each_athlete in data1:
		print(data1[each_athlete].name + ' ' +data1[each_athlete].dob)
