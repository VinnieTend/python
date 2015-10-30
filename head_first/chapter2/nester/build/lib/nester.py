import sys

def print_lol(the_list,indent=False,level=0,fh=sys.stdout):
		for each_list in the_list:
				if isinstance(each_list,list):
						print_lol(each_list,indent,level+1,fh)
				else:
						if indent:
								for num in range(level):
										print("\t",end='',file=fh)
						print(each_list,file=fh)
