# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GE-Project\tasks\System Cycling\IssueInvestigator\src\view\ui\InvMainViewScreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IssueInvestigatorForm(object):
    def setupUi(self, IssueInvestigatorForm):
        IssueInvestigatorForm.setObjectName("IssueInvestigatorForm")
        IssueInvestigatorForm.resize(571, 676)
        self.gridLayout_3 = QtWidgets.QGridLayout(IssueInvestigatorForm)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(IssueInvestigatorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabSnapshot = QtWidgets.QWidget()
        self.tabSnapshot.setObjectName("tabSnapshot")
        self.gridLayout = QtWidgets.QGridLayout(self.tabSnapshot)
        self.gridLayout.setObjectName("gridLayout")
        self.frameOption = QtWidgets.QFrame(self.tabSnapshot)
        self.frameOption.setFrameShape(QtWidgets.QFrame.Box)
        self.frameOption.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameOption.setObjectName("frameOption")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameOption)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.labelPath = QtWidgets.QLabel(self.frameOption)
        self.labelPath.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPath.setFont(font)
        self.labelPath.setObjectName("labelPath")
        self.horizontalLayout_12.addWidget(self.labelPath)
        self.lineEditPath = QtWidgets.QLineEdit(self.frameOption)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditPath.setFont(font)
        self.lineEditPath.setObjectName("lineEditPath")
        self.horizontalLayout_12.addWidget(self.lineEditPath)
        self.toolButtonSelectionDialog = QtWidgets.QToolButton(self.frameOption)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toolButtonSelectionDialog.setFont(font)
        self.toolButtonSelectionDialog.setObjectName("toolButtonSelectionDialog")
        self.horizontalLayout_12.addWidget(self.toolButtonSelectionDialog)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelPatternInv = QtWidgets.QLabel(self.frameOption)
        self.labelPatternInv.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelPatternInv.setFont(font)
        self.labelPatternInv.setObjectName("labelPatternInv")
        self.horizontalLayout_13.addWidget(self.labelPatternInv)
        self.lineEditPatternInv = QtWidgets.QLineEdit(self.frameOption)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditPatternInv.setFont(font)
        self.lineEditPatternInv.setObjectName("lineEditPatternInv")
        self.horizontalLayout_13.addWidget(self.lineEditPatternInv)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.frame = QtWidgets.QFrame(self.frameOption)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelIP = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelIP.setFont(font)
        self.labelIP.setObjectName("labelIP")
        self.horizontalLayout_9.addWidget(self.labelIP)
        self.lineEditIP = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditIP.setFont(font)
        self.lineEditIP.setObjectName("lineEditIP")
        self.horizontalLayout_9.addWidget(self.lineEditIP)
        self.labelPort = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName("labelPort")
        self.horizontalLayout_9.addWidget(self.labelPort)
        self.lineEditPort = QtWidgets.QLineEdit(self.frame)
        self.lineEditPort.setMaximumSize(QtCore.QSize(45, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditPort.setFont(font)
        self.lineEditPort.setObjectName("lineEditPort")
        self.horizontalLayout_9.addWidget(self.lineEditPort)
        self.labelUser = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelUser.setFont(font)
        self.labelUser.setObjectName("labelUser")
        self.horizontalLayout_9.addWidget(self.labelUser)
        self.lineEditUser = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditUser.setFont(font)
        self.lineEditUser.setObjectName("lineEditUser")
        self.horizontalLayout_9.addWidget(self.lineEditUser)
        self.labelPassword = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.horizontalLayout_9.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setClearButtonEnabled(False)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_9.addWidget(self.lineEditPassword)
        self.verticalLayout_3.addWidget(self.frame)
        self.gridLayout.addWidget(self.frameOption, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonAnalyze = QtWidgets.QPushButton(self.tabSnapshot)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAnalyze.setFont(font)
        self.pushButtonAnalyze.setObjectName("pushButtonAnalyze")
        self.verticalLayout.addWidget(self.pushButtonAnalyze)
        self.pushButtonSettings = QtWidgets.QPushButton(self.tabSnapshot)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSettings.setFont(font)
        self.pushButtonSettings.setObjectName("pushButtonSettings")
        self.verticalLayout.addWidget(self.pushButtonSettings)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tabSnapshot)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelMatchedSearchResults = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelMatchedSearchResults.setFont(font)
        self.labelMatchedSearchResults.setObjectName("labelMatchedSearchResults")
        self.verticalLayout_2.addWidget(self.labelMatchedSearchResults)
        self.comboBoxIssueList = QtWidgets.QComboBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxIssueList.setFont(font)
        self.comboBoxIssueList.setObjectName("comboBoxIssueList")
        self.verticalLayout_2.addWidget(self.comboBoxIssueList)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.labelHeadingInv = QtWidgets.QLabel(self.frame_2)
        self.labelHeadingInv.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelHeadingInv.setFont(font)
        self.labelHeadingInv.setObjectName("labelHeadingInv")
        self.horizontalLayout_7.addWidget(self.labelHeadingInv)
        self.lineEditHeadingInv = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditHeadingInv.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditHeadingInv.setFont(font)
        self.lineEditHeadingInv.setObjectName("lineEditHeadingInv")
        self.horizontalLayout_7.addWidget(self.lineEditHeadingInv)
        self.labelOccIdInv = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelOccIdInv.setFont(font)
        self.labelOccIdInv.setObjectName("labelOccIdInv")
        self.horizontalLayout_7.addWidget(self.labelOccIdInv)
        self.lineEditOccurrenceInv = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditOccurrenceInv.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOccurrenceInv.sizePolicy().hasHeightForWidth())
        self.lineEditOccurrenceInv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditOccurrenceInv.setFont(font)
        self.lineEditOccurrenceInv.setObjectName("lineEditOccurrenceInv")
        self.horizontalLayout_7.addWidget(self.lineEditOccurrenceInv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelDescInv = QtWidgets.QLabel(self.frame_2)
        self.labelDescInv.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelDescInv.setFont(font)
        self.labelDescInv.setObjectName("labelDescInv")
        self.horizontalLayout_8.addWidget(self.labelDescInv)
        self.plainTextEditDescriptionInv = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEditDescriptionInv.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditDescriptionInv.setFont(font)
        self.plainTextEditDescriptionInv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditDescriptionInv.setObjectName("plainTextEditDescriptionInv")
        self.horizontalLayout_8.addWidget(self.plainTextEditDescriptionInv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelLookupInv = QtWidgets.QLabel(self.frame_2)
        self.labelLookupInv.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelLookupInv.setFont(font)
        self.labelLookupInv.setObjectName("labelLookupInv")
        self.horizontalLayout_5.addWidget(self.labelLookupInv)
        self.plainTextEditLookupInv = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEditLookupInv.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditLookupInv.setFont(font)
        self.plainTextEditLookupInv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditLookupInv.setObjectName("plainTextEditLookupInv")
        self.horizontalLayout_5.addWidget(self.plainTextEditLookupInv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelResolutionInv = QtWidgets.QLabel(self.frame_2)
        self.labelResolutionInv.setMinimumSize(QtCore.QSize(75, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelResolutionInv.setFont(font)
        self.labelResolutionInv.setObjectName("labelResolutionInv")
        self.horizontalLayout_6.addWidget(self.labelResolutionInv)
        self.plainTextEditResolutionInv = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEditResolutionInv.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditResolutionInv.setFont(font)
        self.plainTextEditResolutionInv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditResolutionInv.setObjectName("plainTextEditResolutionInv")
        self.horizontalLayout_6.addWidget(self.plainTextEditResolutionInv)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.radioButtonLocal = QtWidgets.QRadioButton(self.tabSnapshot)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonLocal.setFont(font)
        self.radioButtonLocal.setObjectName("radioButtonLocal")
        self.horizontalLayout_10.addWidget(self.radioButtonLocal)
        self.radioButtonShared = QtWidgets.QRadioButton(self.tabSnapshot)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonShared.setFont(font)
        self.radioButtonShared.setObjectName("radioButtonShared")
        self.horizontalLayout_10.addWidget(self.radioButtonShared)
        self.radioButtonRemote = QtWidgets.QRadioButton(self.tabSnapshot)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonRemote.setFont(font)
        self.radioButtonRemote.setObjectName("radioButtonRemote")
        self.horizontalLayout_10.addWidget(self.radioButtonRemote)
        self.radioButtonOccurrenceID = QtWidgets.QRadioButton(self.tabSnapshot)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButtonOccurrenceID.setFont(font)
        self.radioButtonOccurrenceID.setObjectName("radioButtonOccurrenceID")
        self.horizontalLayout_10.addWidget(self.radioButtonOccurrenceID)
        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tabSnapshot, "")
        self.tabAddIssue = QtWidgets.QWidget()
        self.tabAddIssue.setObjectName("tabAddIssue")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabAddIssue)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelHeading = QtWidgets.QLabel(self.tabAddIssue)
        self.labelHeading.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelHeading.setFont(font)
        self.labelHeading.setObjectName("labelHeading")
        self.horizontalLayout.addWidget(self.labelHeading)
        self.lineEditHeading = QtWidgets.QLineEdit(self.tabAddIssue)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditHeading.setFont(font)
        self.lineEditHeading.setObjectName("lineEditHeading")
        self.horizontalLayout.addWidget(self.lineEditHeading)
        self.labelOccurrenceID = QtWidgets.QLabel(self.tabAddIssue)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelOccurrenceID.setFont(font)
        self.labelOccurrenceID.setObjectName("labelOccurrenceID")
        self.horizontalLayout.addWidget(self.labelOccurrenceID)
        self.lineEditOccurenceID = QtWidgets.QLineEdit(self.tabAddIssue)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditOccurenceID.sizePolicy().hasHeightForWidth())
        self.lineEditOccurenceID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditOccurenceID.setFont(font)
        self.lineEditOccurenceID.setObjectName("lineEditOccurenceID")
        self.horizontalLayout.addWidget(self.lineEditOccurenceID)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.labelPattern = QtWidgets.QLabel(self.tabAddIssue)
        self.labelPattern.setMinimumSize(QtCore.QSize(100, 0))
        self.labelPattern.setMaximumSize(QtCore.QSize(75, 16777215))
        self.labelPattern.setObjectName("labelPattern")
        self.horizontalLayout_14.addWidget(self.labelPattern)
        self.lineEditPattern = QtWidgets.QLineEdit(self.tabAddIssue)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditPattern.setFont(font)
        self.lineEditPattern.setObjectName("lineEditPattern")
        self.horizontalLayout_14.addWidget(self.lineEditPattern)
        self.label = QtWidgets.QLabel(self.tabAddIssue)
        self.label.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        self.comboBoxSubSystem = QtWidgets.QComboBox(self.tabAddIssue)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBoxSubSystem.setFont(font)
        self.comboBoxSubSystem.setObjectName("comboBoxSubSystem")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.comboBoxSubSystem.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBoxSubSystem)
        self.gridLayout_2.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelDescription = QtWidgets.QLabel(self.tabAddIssue)
        self.labelDescription.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelDescription.setFont(font)
        self.labelDescription.setObjectName("labelDescription")
        self.horizontalLayout_2.addWidget(self.labelDescription)
        self.plainTextEditDescription = QtWidgets.QPlainTextEdit(self.tabAddIssue)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditDescription.setFont(font)
        self.plainTextEditDescription.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditDescription.setTabChangesFocus(True)
        self.plainTextEditDescription.setDocumentTitle("")
        self.plainTextEditDescription.setPlaceholderText("")
        self.plainTextEditDescription.setObjectName("plainTextEditDescription")
        self.horizontalLayout_2.addWidget(self.plainTextEditDescription)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelLookup = QtWidgets.QLabel(self.tabAddIssue)
        self.labelLookup.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelLookup.setFont(font)
        self.labelLookup.setObjectName("labelLookup")
        self.horizontalLayout_3.addWidget(self.labelLookup)
        self.plainTextEditLookup = QtWidgets.QPlainTextEdit(self.tabAddIssue)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditLookup.setFont(font)
        self.plainTextEditLookup.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditLookup.setTabChangesFocus(True)
        self.plainTextEditLookup.setDocumentTitle("")
        self.plainTextEditLookup.setPlaceholderText("")
        self.plainTextEditLookup.setObjectName("plainTextEditLookup")
        self.horizontalLayout_3.addWidget(self.plainTextEditLookup)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelResolution = QtWidgets.QLabel(self.tabAddIssue)
        self.labelResolution.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelResolution.setFont(font)
        self.labelResolution.setObjectName("labelResolution")
        self.horizontalLayout_4.addWidget(self.labelResolution)
        self.plainTextEditResolution = QtWidgets.QPlainTextEdit(self.tabAddIssue)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEditResolution.setFont(font)
        self.plainTextEditResolution.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditResolution.setTabChangesFocus(True)
        self.plainTextEditResolution.setDocumentTitle("")
        self.plainTextEditResolution.setBackgroundVisible(False)
        self.plainTextEditResolution.setPlaceholderText("")
        self.plainTextEditResolution.setObjectName("plainTextEditResolution")
        self.horizontalLayout_4.addWidget(self.plainTextEditResolution)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.pushButtonSave = QtWidgets.QPushButton(self.tabAddIssue)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_11.addWidget(self.pushButtonSave)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.pushButtonReset = QtWidgets.QPushButton(self.tabAddIssue)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonReset.setFont(font)
        self.pushButtonReset.setObjectName("pushButtonReset")
        self.horizontalLayout_11.addWidget(self.pushButtonReset)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tabAddIssue, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.labelStatus = QtWidgets.QLabel(IssueInvestigatorForm)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelStatus.setFont(font)
        self.labelStatus.setWordWrap(True)
        self.labelStatus.setObjectName("labelStatus")
        self.gridLayout_3.addWidget(self.labelStatus, 1, 0, 1, 1)

        self.retranslateUi(IssueInvestigatorForm)
        self.tabWidget.setCurrentIndex(0)
        self.radioButtonRemote.toggled['bool'].connect(self.frame.setVisible)
        self.radioButtonLocal.clicked.connect(self.frame.hide)
        self.radioButtonShared.clicked.connect(self.frame.hide)
        self.radioButtonOccurrenceID.clicked.connect(self.frame.hide)
        self.radioButtonLocal.toggled['bool'].connect(self.toolButtonSelectionDialog.setVisible)
        self.radioButtonShared.toggled['bool'].connect(self.toolButtonSelectionDialog.setVisible)
        self.radioButtonRemote.clicked.connect(self.toolButtonSelectionDialog.hide)
        self.radioButtonOccurrenceID.clicked.connect(self.toolButtonSelectionDialog.hide)
        QtCore.QMetaObject.connectSlotsByName(IssueInvestigatorForm)
        IssueInvestigatorForm.setTabOrder(self.tabWidget, self.radioButtonLocal)
        IssueInvestigatorForm.setTabOrder(self.radioButtonLocal, self.radioButtonShared)
        IssueInvestigatorForm.setTabOrder(self.radioButtonShared, self.radioButtonRemote)
        IssueInvestigatorForm.setTabOrder(self.radioButtonRemote, self.radioButtonOccurrenceID)
        IssueInvestigatorForm.setTabOrder(self.radioButtonOccurrenceID, self.lineEditPath)
        IssueInvestigatorForm.setTabOrder(self.lineEditPath, self.toolButtonSelectionDialog)
        IssueInvestigatorForm.setTabOrder(self.toolButtonSelectionDialog, self.lineEditPatternInv)
        IssueInvestigatorForm.setTabOrder(self.lineEditPatternInv, self.lineEditIP)
        IssueInvestigatorForm.setTabOrder(self.lineEditIP, self.lineEditPort)
        IssueInvestigatorForm.setTabOrder(self.lineEditPort, self.lineEditUser)
        IssueInvestigatorForm.setTabOrder(self.lineEditUser, self.lineEditPassword)
        IssueInvestigatorForm.setTabOrder(self.lineEditPassword, self.pushButtonAnalyze)
        IssueInvestigatorForm.setTabOrder(self.pushButtonAnalyze, self.pushButtonSettings)
        IssueInvestigatorForm.setTabOrder(self.pushButtonSettings, self.comboBoxIssueList)
        IssueInvestigatorForm.setTabOrder(self.comboBoxIssueList, self.lineEditHeadingInv)
        IssueInvestigatorForm.setTabOrder(self.lineEditHeadingInv, self.lineEditOccurrenceInv)
        IssueInvestigatorForm.setTabOrder(self.lineEditOccurrenceInv, self.plainTextEditDescriptionInv)
        IssueInvestigatorForm.setTabOrder(self.plainTextEditDescriptionInv, self.plainTextEditLookupInv)
        IssueInvestigatorForm.setTabOrder(self.plainTextEditLookupInv, self.plainTextEditResolutionInv)
        IssueInvestigatorForm.setTabOrder(self.plainTextEditResolutionInv, self.lineEditHeading)
        IssueInvestigatorForm.setTabOrder(self.lineEditHeading, self.lineEditOccurenceID)
        IssueInvestigatorForm.setTabOrder(self.lineEditOccurenceID, self.lineEditPattern)
        IssueInvestigatorForm.setTabOrder(self.lineEditPattern, self.comboBoxSubSystem)
        IssueInvestigatorForm.setTabOrder(self.comboBoxSubSystem, self.plainTextEditDescription)
        IssueInvestigatorForm.setTabOrder(self.plainTextEditDescription, self.plainTextEditLookup)
        IssueInvestigatorForm.setTabOrder(self.plainTextEditLookup, self.plainTextEditResolution)
        IssueInvestigatorForm.setTabOrder(self.plainTextEditResolution, self.pushButtonSave)
        IssueInvestigatorForm.setTabOrder(self.pushButtonSave, self.pushButtonReset)

    def retranslateUi(self, IssueInvestigatorForm):
        _translate = QtCore.QCoreApplication.translate
        IssueInvestigatorForm.setWindowTitle(_translate("IssueInvestigatorForm", "Form"))
        self.labelPath.setText(_translate("IssueInvestigatorForm", "Path/Occ"))
        self.toolButtonSelectionDialog.setText(_translate("IssueInvestigatorForm", "..."))
        self.labelPatternInv.setText(_translate("IssueInvestigatorForm", "Pattern"))
        self.labelIP.setText(_translate("IssueInvestigatorForm", "IP"))
        self.labelPort.setText(_translate("IssueInvestigatorForm", "PORT"))
        self.labelUser.setText(_translate("IssueInvestigatorForm", "User"))
        self.labelPassword.setText(_translate("IssueInvestigatorForm", "Password"))
        self.pushButtonAnalyze.setText(_translate("IssueInvestigatorForm", "Analyze"))
        self.pushButtonSettings.setText(_translate("IssueInvestigatorForm", "Settings"))
        self.labelMatchedSearchResults.setText(_translate("IssueInvestigatorForm", "Matched Search Results:"))
        self.labelHeadingInv.setText(_translate("IssueInvestigatorForm", "Headline"))
        self.labelOccIdInv.setText(_translate("IssueInvestigatorForm", "Occurrence ID"))
        self.labelDescInv.setText(_translate("IssueInvestigatorForm", "Description"))
        self.labelLookupInv.setText(_translate("IssueInvestigatorForm", "Lookup"))
        self.labelResolutionInv.setText(_translate("IssueInvestigatorForm", "Resolution"))
        self.radioButtonLocal.setText(_translate("IssueInvestigatorForm", "Local Snapshot"))
        self.radioButtonShared.setText(_translate("IssueInvestigatorForm", "Shared Snapshot"))
        self.radioButtonRemote.setText(_translate("IssueInvestigatorForm", "Remote Snapshot"))
        self.radioButtonOccurrenceID.setText(_translate("IssueInvestigatorForm", "Occurance ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSnapshot), _translate("IssueInvestigatorForm", "Investigation"))
        self.labelHeading.setText(_translate("IssueInvestigatorForm", "Headline[*]"))
        self.labelOccurrenceID.setText(_translate("IssueInvestigatorForm", "Occurrence ID (If Any)"))
        self.labelPattern.setText(_translate("IssueInvestigatorForm", "Pattern[*]"))
        self.label.setText(_translate("IssueInvestigatorForm", "SubSystem"))
        self.comboBoxSubSystem.setItemText(0, _translate("IssueInvestigatorForm", "Unknown"))
        self.comboBoxSubSystem.setItemText(1, _translate("IssueInvestigatorForm", "Others"))
        self.comboBoxSubSystem.setItemText(2, _translate("IssueInvestigatorForm", "AcqSvc"))
        self.comboBoxSubSystem.setItemText(3, _translate("IssueInvestigatorForm", "SwPlt"))
        self.comboBoxSubSystem.setItemText(4, _translate("IssueInvestigatorForm", "SwApp"))
        self.comboBoxSubSystem.setItemText(5, _translate("IssueInvestigatorForm", "POS"))
        self.comboBoxSubSystem.setItemText(6, _translate("IssueInvestigatorForm", "Djinn"))
        self.comboBoxSubSystem.setItemText(7, _translate("IssueInvestigatorForm", "Detector"))
        self.labelDescription.setText(_translate("IssueInvestigatorForm", "Description[*]"))
        self.labelLookup.setText(_translate("IssueInvestigatorForm", "Lookup"))
        self.labelResolution.setText(_translate("IssueInvestigatorForm", "Resolution"))
        self.pushButtonSave.setText(_translate("IssueInvestigatorForm", "Save"))
        self.pushButtonReset.setText(_translate("IssueInvestigatorForm", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAddIssue), _translate("IssueInvestigatorForm", "Add Issue/Solution"))
        self.labelStatus.setText(_translate("IssueInvestigatorForm", "<Display status>..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IssueInvestigatorForm = QtWidgets.QWidget()
    ui = Ui_IssueInvestigatorForm()
    ui.setupUi(IssueInvestigatorForm)
    IssueInvestigatorForm.show()
    sys.exit(app.exec_())

