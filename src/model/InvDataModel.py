import os
import sqlite3
import datetime
import pandas as pd

class InvDataModel:	
	_mDatabasePath_ = 'db\AdminPristina.db'
	_mDatabaseExpFilePath_ = 'db\\'
	_mDatabaseExpFileName_ = 'AdminPristinaDBExp.xlsx'

	def __init__(self):
		print("Inside InvDataModel, __init__")

	def exists(self):
		print("Inside InvDataModel, dbExists")

		#Check DB exists
		if not os.path.isfile(self._mDatabasePath_):
			print('DB is not exists')
			return False;
		
		self._dbCon_ = sqlite3.connect(self._mDatabasePath_)
		
		#Check table exists (note only calling this query is sufficient
		#Incase if table is not exists there will be an exception
		cursor = self._dbCon_.execute('''SELECT * from OccurrenceDB''')
		self._dbCon_.close()
		return True

	def add(self, uniqueId, currDateTime, headline, occurrenceID, pattern, subSystem, description, lookup, resolution):
		print("Inside InvDataModel, add")
		try:
			print('uniqueId' + uniqueId + 'currDateTime:' + currDateTime + 'headline:' + headline + 'occurenceID:' + 
			occurrenceID + 'pattern:' + pattern + 'subSystem:' + subSystem + 'description:' + description + 'lookup:' + 
			lookup +  'resolution:' + resolution)
			print('Opening database...')
			
			self._dbCon_ = sqlite3.connect(self._mDatabasePath_)
			print('Inserting record into database...')
			addQuery = "INSERT INTO OccurrenceDB(ID, DateTime, Headline, OccurrenceID, Pattern, SubSystem, Description, Lookup, Resolution) VALUES("
			addQuery = str(addQuery) + "'" + str(uniqueId) + str("','") + str(currDateTime) + str("','") + str(headline) + str("','") + str(occurrenceID) + \
			str("','") + str(pattern) + str("','") + str(subSystem) + str("','") + str(description) + str("','") + str(lookup) + str("','") + \
			str(resolution) + str("')")

			#Execute query & commit record
			self._dbCon_.execute(addQuery)
			self._dbCon_.commit()
			print('Record added successfully...')
			self._dbCon_.close()
			return True
		except Exception as exp:
			print('Unable to add record to the DB, Error is:')
			print(exp)
			return False
		
	def export(self, location, fileName):
		#https://xlsxwriter.readthedocs.io/working_with_pandas.html
		print('Opening database...')
		try:
			self._dbCon_ = sqlite3.connect(self._mDatabasePath_)
			dbData = self._dbCon_.execute('''SELECT Headline, OccurrenceID, Pattern, SubSystem, Description, Lookup, Resolution
			from OccurrenceDB''')

			#Write all the database data into the list
			invData = []
			for data in dbData:
				invData.append(data)

			#Create data frame
			df = pd.DataFrame(data= invData, columns = ['Headline', 'OccurrenceID', 'Pattern', 'SubSystem', 'Description', 'Lookup', 'Resolution'])
			
			#Get file handler
			writer = pd.ExcelWriter(self._mDatabaseExpFilePath_ + self._mDatabaseExpFileName_, engine='xlsxwriter')
			
			#Write dataframe to excel file, making header format false for the custom header
			df.to_excel(writer, sheet_name='Senographe Pristina Data Base', header = False, index = False)

			#Get back the current book and reformat the header
			currentBook = writer.book
			worksheet = writer.sheets['Senographe Pristina Data Base']

			#Add a header format.
			header_format = currentBook.add_format({
				'bold': True,
				'text_wrap': True,
				'valign': 'top',
				'fg_color': '#D7E4BC',
				'border': 2})

			#Write the column headers with the defined format.
			for col_num, value in enumerate(df.columns.values):
				worksheet.write(0, col_num, value, header_format)
			
			#Add a header format.
			row_format = currentBook.add_format({
			'text_wrap': True,
			'valign': 'top',
			'fg_color': '#01E4BC',
			'border': 1})
						
			#Write the row data with the defined format.
			for row_count, value in enumerate(df.values):
				for col_num, item in enumerate(value):
					worksheet.write(row_count + 1, col_num, item, row_format)

			#Set columns width based on their size pattern
			worksheet.set_column(0, 0, 15)
			worksheet.set_column(2, 2, 15)
			worksheet.set_column(4, 4, 30)
			worksheet.set_column(5, 5, 30)
			worksheet.set_column(6, 6, 75)

			#Save file
			writer.save()

		except Exception as exp:
			print (exp)
		
if __name__ == "__main__":
	print ("Inserting data into table")

	try:
		dataModel = InvDataModel()	

		if not dataModel.exists():
			print('DB/Tabel is not exists, exiting')
			exit(1)

		#currDateTime = datetime.datetime.now()
		#uniqueId = '305028701-' + str(int(currDateTime.timestamp()))
		#dataModel.add(uniqueId, currDateTime, 'Default Defect', 'O123456', 'ABORT', 'AcqSvc', 'F11 Abort', 
		#		'Check log files', 'Issue is FIX')

		dataModel.export(dataModel._mDatabaseExpFilePath_, dataModel._mDatabaseExpFileName_)

	except Exception as err:
		print ("Error while inserting data into the tabel, error is:")
		print(err)

	print ("Exiting from application")