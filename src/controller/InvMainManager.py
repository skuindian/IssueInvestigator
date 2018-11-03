import sys, os
from PyQt5.QtWidgets import QApplication
from threading import Thread
import datetime

#Import required view modules into controller module
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\\..\\view")
import InvMainView

#Import required model modules into controller module
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\\..\\model")
from InvOccModel import InvOccModel
from InvDataModel import InvDataModel

#Import required utility modules into controller module
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "\\..\\utility")
from InvUtility import SnapshotUtil, SpaceUtil

#------------------------------------------------------------------------------
# InvViewThread Class - To run request in a thread
#------------------------------------------------------------------------------
class InvThread(Thread):
	def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, *, daemon = None):
		Thread.__init__(self, group, target, name, args, kwargs)
		self._return = None

	def run(self):
		if self._target  is not None:
			self._return = self._target (*self._args, **self._kwargs)
	def join(self):
		Thread.join(self)
		return self._return

class InvMainManager:
	def __init__(self):
		print("Inside InvMainManager, __init__")

	def start(self):
		print("Inside InvMainManager, start")

		#Initialize main view class
		self._mInvMainView_ = InvMainView.InvMainView(self)
		self._mInvMainView_.start()

		#Initializing data model class
		self._mInvDataModel_ = InvDataModel()

	def analyzeSnapshot(self, snapshotPath, ipAddress, userName, userPassword, outputPath):
		#Download snapshot from remote server
		analyzeThread = InvThread(target = self.downloadAndAnalyzeSnapshot, name = 'ThreadAnalyzeSnapshot',
		args = (snapshotPath, ipAddress, userName, userPassword, outputPath))

		analyzeThread.start()
		#analyzeThread.join()

	def downloadAndAnalyzeSnapshot(self, snapshotPath, ipAddress, userName, userPassword, outputPath):
		#Defining common variable and function
		snapshotExtracted = False
		spaceUtil = SpaceUtil()
		snapshotUtil = SnapshotUtil()

		#Step-01 => Downloading & Extracting Snapshot
		if not os.path.isdir(snapshotPath):
			self._mInvMainView_.updateSplashScreenStatus("Analyzing Logs...Please wait...Checking System Space", 10)
			if spaceUtil.isSystemHasSufficientSpace('.'):
				self._mInvMainView_.updateSplashScreenStatus("Analyzing Logs...Please wait...Downloading", 20)

				if (not ipAddress == '') and (not userName == '') and (not userPassword == '') and (not outputPath == ''):
					snapshotPath = snapshotUtil.getRemoteSnapshot(snapshotPath, ipAddress, userName, userPassword, outputPath)

				self._mInvMainView_.updateSplashScreenStatus("Analyzing Logs...Please wait...Extracting", 40)
				extractionPath = snapshotUtil.getSnapshotLocation(snapshotPath, outputPath)
				if extractionPath != '':
					self._mInvMainView_.snapshotAnalysisDone()
					completeExtractionPath = os.path.realpath(extractionPath)
					self._mInvMainView_.updateApplicationStatus("Successfully extracted the snapshot at:" + completeExtractionPath)
					snapshotExtracted = True
				else:
					self._mInvMainView_.snapshotAnalysisDone()
					self._mInvMainView_.updateApplicationStatus("Unable to get and extract snapshot.")
			else:
				self._mInvMainView_.snapshotAnalysisDone()
				self._mInvMainView_.updateApplicationStatus("Not sufficient space into the system.")
		else:
			self._mInvMainView_.snapshotAnalysisDone()
			completeExtractionPath = os.path.realpath(outputPath)
			self._mInvMainView_.updateApplicationStatus("Snapshot is already extracted at:" + completeExtractionPath)
			snapshotExtracted = True

		#Step-02 => Analyzing Snapshot
		#TODO

	def addRecord(self, headline, occurenceID, pattern, subSystem, description, lookup, resolution):
		print("Inside InvMainManager, addRecord")
		try:
			print('Inputs are- headline:' + headline + 'occurenceID:' + occurenceID + 'pattern:' + 
			pattern + 'subSystem:' + subSystem + 'description:' + description + 'lookup:' + lookup +  'resolution:' + resolution)
			print('Opening database...')
			currDateTime = datetime.datetime.now()
			uniqueId = '305028701-' + str(int(currDateTime.timestamp()))

			if self._mInvDataModel_.exists():
				if self._mInvDataModel_.add(uniqueId, str(currDateTime), headline, occurenceID, pattern, subSystem, 
							 description, lookup, resolution):
					self._mInvMainView_.updateApplicationStatus("Record added successfully.")
				else:
					self._mInvMainView_.updateApplicationStatus("Unable to add record into the database")	
			else:
				self._mInvMainView_.updateApplicationStatus("Unable to add record into the database, DB not exists/currupted")				
		except Exception as exp:
			print('Unable to add record to the DB, Error is:')
			print(exp)

if __name__ == "__main__":
	print("Inside main")
	
	app = QApplication(sys.argv)

	#Running controller function
	mInvMainManager = InvMainManager()
	mInvMainManager.start()
	
	sys.exit(app.exec_())