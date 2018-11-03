#------------------------------------------------------------------------------
# InvOccModel Class
#------------------------------------------------------------------------------
class InvOccModel:
	def __init__(self):
		pass

	def getOccurrenceSnapshot(self, occurrenceID):
		print("Requested occurrence ID is:", occurrenceID)
		try:
			#Remove characters if present
			if 'o' in occurrenceID:
				occurrenceID = occurrenceID.replace('O', '')
			if 'O' in occurrenceID:
				occurrenceID = occurrenceID.replace('O', '')

			#Get information of the webpage
			occ = {'id': occurrenceID}
			#http://ritamammo.health.ge.com/rita/occurrences/index.php?live=1&type%5B%5D=&type%5B%5D=x-ray+abort+MEBEF&type%5B%5D=MEBEF+L2&type%5B%5D=MEBEF+L3&type%5B%5D=MEBF+L2&type%5B%5D=MEBF+L3&type%5B%5D=onoff&type%5B%5D=quality&type%5B%5D=other&sysrel%5B%5D=&team%5B%5D=5&status%5B%5D=open&official%5B%5D=1&official%5B%5D=2&tags=&pattern=&button=Search&csv=list
			#req = requests.get("http://ritamammo.health.ge.com/rita/occurrences/show.php?id=" + occurrenceID);
			req = requests.get("http://ritamammo.health.ge.com/rita/occurrences/show.php", params=occ);
			print("Status Code:")
			print(req.status_code)
			print(req.text)
		except Exception as err:
			print("ERROR:Unable to create connection, error is...")
			print(err)

		return ""