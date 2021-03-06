import athletemodel 
import yate

athletes = athletemodel.get_namesID_from_store(data_files)


print(yate.start_response())
print(yate.include_header("NUAC's List of Athletes"))
print(yate.para("Select an athlete from the list to work with:"))
print(yate.start_form("generate_timing_data.py"))

for each_athlete in athletes:
		print(yate.radio_button("which_athlete",each_athlete[0],each_athlete[1]))
print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))
