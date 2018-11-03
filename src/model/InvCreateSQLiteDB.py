import sqlite3
import os

if __name__ == "__main__":
	print ("Creating SQLite database")

	try:
		#location = os.path.abspath('.')
		if not os.path.isdir('db'):
			print('DB folder was not exists, creating')
			os.mkdir('db')
		dbCon = sqlite3.connect('db\AdminPristina.db')

		print("Table OccurrenceDB is dropped") 
		
		try:
			dbCon.execute('''drop TABLE OccurrenceDB''')
		except Exception as exp:
			print ('No table is present')

		print("Creating table OccurrenceDB") 
		
		dbCon.execute('''CREATE TABLE OccurrenceDB
				(ID TEXT PRIMARY KEY NOT NULL,
				DateTime TEXT NOT NULL,
				Headline TEXT NOT NULL,
				OccurrenceID TEXT,
				Pattern TEXT NOT NULL,
				SubSystem TEXT NOT NULL,
				Description TEXT NOT NULL,
				Lookup TEXT,
				Resolution TEXT);''')

		dbCon.close()

		print("Table created successfully")

	except Exception as err:
		print ("Error while creating DB, error is:")
		print(err)

	print ("Exiting from application")