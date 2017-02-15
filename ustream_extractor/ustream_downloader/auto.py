import os
import time as t
from datetime import datetime, date, time

while True:
	dDate = datetime.now().date()
	dTime = datetime.now().time()

	print str("Current Time: ") + str(dTime) + str(", Recording will be conducted every 10 min >> ust down")

	#print str(dTime)
	#print 20 % 10
#	dTime = "11:10:00"
#	print str(dTime)
#	print int(str(dTime)[3:5])%10, str(dTime)[6]

	if int(str(dTime)[3:5])%20==0 and int(str(dTime)[6:8]) == 0:
		os.system("python h_parser.py")
		t.sleep(10)
