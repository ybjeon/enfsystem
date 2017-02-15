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
	time.sleep(180)
	for f in os.listdir('.'):
		#if os.path.isfile(f) or f.find('.wav'):
		if f.find('.wav') != -1:
			try:
				if cmp(os.path.getsize(f), lsDic[f]) == 0:
					if int(subprocess.check_output('sox --i -r ' + f, shell=True)) != 1000:
						print f
						subprocess.check_output('sox ' + f + ' -r 1000 d_' + f , shell=True)
						subprocess.check_output('rm ' + f, shell=True)

			except KeyError:
				print "New one is detected"
			except subprocess.CalledProcessError:
				print "Error.."
			except OSError:
				print "OS Error"
				
			#lsDic[f] = os.path.getsize(f)


		
