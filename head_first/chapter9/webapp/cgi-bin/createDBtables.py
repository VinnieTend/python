import sqlite3

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()
cursor.execute("""create table athletes (
				id InTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
				name text not null,
				dob DATE not NULL)""")
cursor.execute("""CREATE Table timing_data(
				athlete_id integer not null,
				value text not null,
				foreign key (athlete_id) REFERENCES athletes)""")

connection.commit()
connection.close()
