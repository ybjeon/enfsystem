import os
import time
import subprocess


lsDic = {}
changed = list()

while True:
	for f in os.listdir('.'):
		if os.path.isfile(f):
			lsDic[f] = os.path.getsize(f)

	print "time "
	time.sleep(60)
	for f in os.listdir('.'):
		#if os.path.isfile(f) or f.find('.wav'):
		if f.find('.wav') != -1:
			try:
				if cmp(os.path.getsize(f), lsDic[f]) == 0:
					print f
					subprocess.check_output('python har_QIFFT.py ' + f, shell=True)
			except KeyError:
				print "New one is detected"
			except subprocess.CalledProcessError:
				os.system('rm ' + f)
				print "Error.."
			except OSError:
				os.system('rm ' + f)
				print "OS Error"
				
			#lsDic[f] = os.path.getsize(f)


		
