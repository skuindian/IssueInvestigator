import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QSplashScreen, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, Qt, pyqtSignal

from InvMainViewScreen import Ui_IssueInvestigatorForm
from InvSplashScreen import Ui_SplashScreen

# Reference - multiple inheritance approach
# http://pyqt.sourceforge.net/Docs/PyQt5/designer.html

#------------------------------------------------------------------------------
# InvSplashView Class
#------------------------------------------------------------------------------
class InvSplashView(QDialog, Ui_SplashScreen):
	def __init__(self):
		print("Inside InvSplashView, __init__")
		super(InvSplashView, self).__init__()

		#Setup user interface from designer
		self.setupUi(self)

	def start(self):
		print("Inside InvSplashView, start")
		self.setWindowOpacity(0.5)
		self.show()

	def stop(self):
		print("Inside InvSplashView, stop")
		self.hide()


#------------------------------------------------------------------------------
# InvMainView Class
#------------------------------------------------------------------------------
class InvMainView(QWidget, Ui_IssueInvestigatorForm):
	#Define class member
	_mCopyPath_ = r"output/"

	#Declaring signals
	emitSnapshotAnalysisDone = pyqtSignal()
	emitUpdateStatus = pyqtSignal(str)
	emitSplashStatus = pyqtSignal(str, int)

	def __init__(self, invMainManager):
		print("Inside InvMainView, __init__")
		super(InvMainView, self).__init__()

		#Update object with controller instence
		self._mInvMainManager_ = invMainManager

		#Setup user interface from designer
		self.setupUi(self)
		self.setWindowTitle("Issue Investigation")

		#Initialize controls before launching UI
		self.radioButtonRemote.setChecked(True)
		
		#Initialize objects
		self._mSplashObj_ = InvSplashView()

		#Connect the buttons
		self.pushButtonAnalyze.clicked.connect(self.analyzeSnapshot)
		self.pushButtonSave.clicked.connect(self.saveRecord)

		#Connect user defined signal with user defined slots or existing slots
		self.emitSnapshotAnalysisDone.connect(self.snapshotAnalysisDone)
		self.emitUpdateStatus.connect(self.updateApplicationStatus)
		self.emitSplashStatus.connect(self.updateSplashScreenStatus)

	def start(self):
		print("Inside InvMainView, start")
		self.showMaximized()

	#Defining functions to handle user action
	#http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html#PyQt5.QtCore.pyqtSlot
	def analyzeSnapshot(self):
		print("Inside InvMainView, analyzeSnapshot")

		#Display the wait screen
		self.labelStatus.setText("Parsing Snapshot...")
		self._mSplashObj_.setParent(self)
		self._mSplashObj_.resize(self.width(), self.height())
		self._mSplashObj_.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
		self._mSplashObj_.start()
		self.requestToAnalyze()

	def requestToAnalyze(self):
		self.emitSplashStatus.emit("Analyzing Logs...Please wait...", 0)
		if self.radioButtonLocal.isChecked() or self.radioButtonShared.isChecked():
			if self.lineEditPath.text() == '':
				self.emitSnapshotAnalysisDone.emit()
				self.emitUpdateStatus.emit("Empty Snapshot Path...")
				return
			self.emitSplashStatus.emit("Analyzing Logs...Please wait...Initiating Analysis of the snapshot", 5)
			self._mInvMainManager_.analyzeSnapshot(self.lineEditPath.text(), '', '', '', self._mCopyPath_)
		elif self.radioButtonRemote.isChecked():
			if self.lineEditPath.text() == '' or self.lineEditIP.text() == '' or self.lineEditUser.text() == '' or self.lineEditPassword.text() == '':
				self.emitSnapshotAnalysisDone.emit()
				self.emitUpdateStatus.emit("Empty Path or IP or User or Password...")
				return
			else:
				self.emitSplashStatus.emit("Analyzing Logs...Please wait...Initiating Analysis of the snapshot", 5)
				self._mInvMainManager_.analyzeSnapshot(self.lineEditPath.text(), self.lineEditIP.text(), self.lineEditUser.text(), self.lineEditPassword.text(), self._mCopyPath_)
		elif self.radioButtonOccurrenceID.isChecked():
			self.emitSnapshotAnalysisDone.emit()
			self.emitUpdateStatus.emit("Sorry, this feature is not yet implemented")

	def snapshotAnalysisDone(self):
		self._mSplashObj_.stop()

	def updateSplashScreenStatus(self, message, value):
		self._mSplashObj_.labelSplash.setText(message)
		self._mSplashObj_.progressBar.setValue(value)

	def updateApplicationStatus(self, message):
		self.labelStatus.setText(message)
		#Messagebox is not working, check why?
		#if not message == '':
		#	msgBox = QMessageBox() 
		#	msgBox.setText(message);
		#	msgBox.exec_();
		#self.labelStatus.setText('')

	def saveRecord(self):
		self.emitUpdateStatus.emit("")
		if not self.lineEditHeading.text() == '' and \
		not self.lineEditPattern.text() == '' and \
		not self.comboBoxSubSystem.currentText() == '' and \
		not self.plainTextEditDescription.toPlainText() == '':	
			self._mInvMainManager_.addRecord(self.lineEditHeading.text(), self.lineEditOccurenceID.text(), 
									self.lineEditPattern.text(), self.comboBoxSubSystem.currentText(),
									self.plainTextEditDescription.toPlainText(), self.plainTextEditLookup.toPlainText(),
									self.plainTextEditResolution.toPlainText())
		else:		
			self.emitUpdateStatus.emit("Please provide the required input")

if __name__ == "__main__":
	print("Inside __main__")
	app = QApplication(sys.argv)

	window = InvMainView()
	window.start()

	sys.exit(app.exec_())