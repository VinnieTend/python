movies =['the holy grail',1975,'terry jones & terry gilliam',91,['graham chapman',['michael palin','john cleese','terry gilliam','eric idle','terry jones']]]


def print_lol(the_list):
		for lol_lists in the_list:
				if isinstance(lol_lists,list):
						print_lol(lol_lists)
				else:
						print(lol_lists)
print_lol(movies);
