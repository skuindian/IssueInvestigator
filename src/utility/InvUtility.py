import os
import sys
import shutil
import zipfile
from colorama import Fore, Style
import requests

#Globel variables
GB_TO_BYTES = 1024 * 1024 * 1024
MIN_SPACE_NEEDED_IN_GB = 3

#------------------------------------------------------------------------------
# SnapshotUtil Class
#------------------------------------------------------------------------------
class SnapshotUtil:
	def __init__(self):
		pass

	def getSnapshotLocation(self, snapshotLocation, copyPath):
		print("Fetching complete snapshot into the system...snapshotLocation:" + snapshotLocation + ',copyPath:' + copyPath)
		snapshot_target_path = ''
		try:
			#Create destination file name
			snapshotFileName = snapshotLocation.split("\\")[-1]

			#Create directory if not exists
			if not os.path.isdir(copyPath):
				#Creating directory
				print("Creating new directiry...")
				os.mkdir(copyPath)
			else:
				print("Destination folder exists...")
			copyPathWithFile = copyPath + snapshotFileName;

			#Check if snapshot zip is present into the system
			if not os.path.isfile(copyPathWithFile):
				#Download file into the current file system
				shutil.copyfile(snapshotLocation, copyPathWithFile)
			else:
				print("Snapshot is already present into the system...")

			#untar file
			print("Untaring snapshot into the corrosponding directory...")
			snapshot_zip = zipfile.ZipFile(copyPathWithFile, 'r')
			snapshot_target_path = copyPath + snapshotFileName.split('.zip')[0] + '/';
			snapshot_zip.extractall(snapshot_target_path)
			snapshot_zip.close()

		except (FileNotFoundError, IOError, PermissionError) as err:
			print("Unable to copy file, error is:")
			print(err)
			return ''

		return snapshot_target_path

	def getRemoteSnapshot(self, snapshotLocation, ipAddress, username, password, copyPath):
		print("Fetching remote snapshot..." + snapshotLocation)

		#Get file name
		snapshotFilePath = snapshotLocation.split("/")[-1]

		#Check if snapshot zip is present into the system
		if os.path.isfile(copyPath + snapshotFilePath):
			print("Snapshot is already present into the system...")
			return snapshotFilePath

		print ('OS Name', os.name)
		cmd = ''
		#find proper command for windows and linux
		if sys.platform.startswith('win'):
			#PuTTY Secure Copy (PSCP) and PuTTY SFTP (PSFTP)
			#https://www.ssh.com/ssh/putty/putty-manuals/0.68/Chapter5.html
			#https://www2.cisl.ucar.edu/resources/storage-and-file-systems/pscp-and-psftp
			cmd = "pscp -pw " + password + " -r " + username + "@" + ipAddress + ":" + snapshotLocation + " " + copyPath
		elif sys.platform.startswith('linux'):
			#TODO - test in linux?
			cmd = "scp -pw '" + password + "' -r " + username + "@" + ipAddress + ":" + snapshotLocation + " " + copyPath

		try:
			#Create directory if not exists
			if not os.path.isdir(copyPath):
				#Creating directory
				print("Creating new directiry...")
				os.mkdir(copyPath)

			print("Copying remote snapshot to location: "+ copyPath + " from remote location " + snapshotLocation)
			#Get file name and append the path
			snapshotFilePath = snapshotLocation.split("/")[-1]
			os.system(cmd)
		except Exception as err:
			print("Unable to get snapshot from the remote location...error is:")
			print(err)
			return ''

		return snapshotFilePath

#------------------------------------------------------------------------------
# SpaceUtil Class
#------------------------------------------------------------------------------
class SpaceUtil:
	def __init__(self):
		pass

	def isSystemHasSufficientSpace(self, path):
		total, used, free = shutil.disk_usage(path)
		print("Space in system, total:" + str(total/GB_TO_BYTES) + ", Used:" + str(used/GB_TO_BYTES) + ", Free:" + str(free/GB_TO_BYTES))
		if ((free/GB_TO_BYTES) < MIN_SPACE_NEEDED_IN_GB):
			return False
		else:
			return True

#------------------------------------------------------------------------------
#Calling main routine
#------------------------------------------------------------------------------
if __name__ == '__main__':
	print("Starting Application...")	
	userOccInput = input("Do you have occurrence ID (Yes/No):")
	print(userOccInput)

	userOccId = ''
	#Example
	#\\inblrhctinas03.eng.med.ge.com\MammoLogs\2018.09\24\P207\P207_20180921_160546_CYCLING_LOG.zip
	#/mnt/storage/nextgen/snapshots/PoP/SPR_FailedSigmaPaddleFirmwareUpload/Pristina_20180823_060810_Sigma_Paddle_work_fine.zip
	snapshotLocation = ''
	copyPath = r"output/"
	extractionPath = ''
	snapshotType = ''
	#remote option
	#ipAddress = '3.249.12.181'
	#username = 'nextgen'
	#password = 'nextgen'
	ipAddress = '3.204.30.136'
	username = 'root'
	password = '#superxr'

	if userOccInput.lower() == str("yes"):
		userOccId = input("Enter the occurrence ID:")

		#TODO - Use RiTa Restfull API to get the snapshot information
		occData = InvOccModel() ;
		snapshotLocation = occData.getOccurrenceSnapshot(userOccId)
	else:
		snapshotType = input("Is snapshot local/remote?")

		if snapshotType == 'local':
			snapshotLocation = input("Enter the snapshot location:")
		elif snapshotType == 'remote':
			#Ask user for the ipaddress/username/password
			snapshotLocation = input("Enter the snapshot location:")
		else:
			print(Fore.RED, "ERROR::Invalid option provided, exiting.")
			exit(1)

	print("Snapshot Location is:", snapshotLocation)

	if snapshotLocation == '':
		print(Fore.RED, 'ERROR::No snapshot information provided, exiting')
		exit
	else:
		spaceUtil = SpaceUtil()
		snapshotUtil = SnapshotUtil()
		#First check system has sufficent space
		if spaceUtil.isSystemHasSufficientSpace('.'):

			if snapshotType == 'remote':
				snapshotLocation = snapshotUtil.getRemoteSnapshot(snapshotLocation, ipAddress, username, password, copyPath)

			#Copy snapshot and untar and get the final location
			extractionPath = snapshotUtil.getSnapshotLocation(snapshotLocation, copyPath)
			if extractionPath != '':
				print(Fore.GREEN, "SUCCESS::Snapshot extracted at:", os.path.abspath(extractionPath))
			else:
				print(Fore.RED, "ERROR::Unable to get and extract snapshot.")
		else:
			print(Fore.RED, "ERROR::System does not have sufficient space to get zip and extract...")

		#Reset all color
		print(Style.RESET_ALL)