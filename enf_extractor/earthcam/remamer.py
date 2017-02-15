import os
import sys

print('mv ' + sys.argv[1] + " d_" + str(sys.argv[1]).split('d_')[len(str(sys.argv[1]).split('d_'))-1])
os.system('mv ' + sys.argv[1] + " d_" + str(sys.argv[1]).split('d_')[len(str(sys.argv[1]).split('d_'))-1])

#print str(sys.argv[1]).split('d_')[len(str(sys.argv[1]).split('d_'))-1]
