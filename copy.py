import os
import datetime
import shutil

# Defining all necessary source and destination pathes for Windows system. Src and dst folders can be changed depending on application structure
# For Linux system flow will be the same but for with slashes in the path variables(instead of backslashes for Windows)
targetFilePath = "C:\\Python27\\Target\\logo.png"
weekdayFilePath = "C:\Python27\\BusinessDays\\weekday.png"
weekendFilePath = "C:\\Python27\\Weekend\\weekend.png"

# Getting todays number of the day in a week:
dayNumber = datetime.datetime.today().isoweekday()

# Remove existing logo file:
if os.path.isfile(targetFilePath):
	os.remove(targetFilePath)
	print "Removed original logo.png file"

# Copying necessary logo.png picture depending on day in the week:
if dayNumber in range(1,6):
	shutil.copy(weekdayFilePath, targetFilePath)
	print "Successfully copied weekday logo"
elif dayNumber in range(6,8):
	shutil.copy(weekendFilePath, targetFilePath)
	print "Successfully copied weekend logo"
else:
	# This block of code normally should never be executed:
	print "Error while copying logo image! Wrong number of day in the week: '%s'" % str(dayNumber)
