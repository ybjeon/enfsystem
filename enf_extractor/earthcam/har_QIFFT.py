import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt 
from scipy.fftpack import fft
from scipy.interpolate import interp1d
from multiprocessing import Process, Queue
from scipy.signal import resample
import scipy.io as sio
import sys
import os
import subprocess


def harmonics(x, ffted_y, mmWinSize, mmOrder):

	harm_y = list()
	for i in range(len(ffted_y)):
		y = ffted_y[i][(mmWinSize/2)*0:(mmWinSize/2)*0.12+1] 
		for j in range(1, mmOrder):
			idx = (mmWinSize/2)*0.06*j 
			y = y + ffted_y[i][idx:idx+len(y)] 
		harm_y.append(y)

	return harm_y


def zerolistmaker(n):
	listofzeros = [0] * n
	return listofzeros

def QIFFT(mData, mFs, mWinSize, ovlapSize, result, mOrder):
	#global cnt
	N = len(mData)
	T = 1/float(mFs)

	wData = list()
	for wd in mData:
		wData.append(wd)

	#first time operation
	winIdx = mWinSize-ovlapSize
	yf = [np.abs(fft(mData[winIdx:(winIdx+mWinSize-1)]))]


	while winIdx+2*mWinSize < len(mData):
		winIdx = winIdx+mWinSize-ovlapSize
		yf = np.append(yf, [np.abs(fft(mData[winIdx:(winIdx+mWinSize-1)]))], axis=0)

	xf = np.linspace(0.0, 1.0/(2.0*T), mWinSize/2)

	harm_yy = harmonics(np.linspace(0.0, 1.0/(2.0*T), len(yf[0])), yf, mWinSize, mOrder)

	enfBin = list()
	for i in range(len(harm_yy)):
		xf_120 = xf[(mWinSize/2)*0.058:(mWinSize/2)*0.062]

		#yf_120 = 2.0/mWinSize * harm_yy[i][(mWinSize/2)*0:(mWinSize/2)*0.065]
		harm_yy[i][(mWinSize/2)*0.058:(mWinSize/2)*0.059] = zerolistmaker(harm_yy[i][(mWinSize/2)*0.058:(mWinSize/2)*0.059])
		harm_yy[i][(mWinSize/2)*0.061:(mWinSize/2)*0.062] = zerolistmaker(harm_yy[i][(mWinSize/2)*0.061:(mWinSize/2)*0.062])
		yf_120 = 2.0/mWinSize * harm_yy[i][(mWinSize/2)*0.058:(mWinSize/2)*0.062]
		
		f_120 = interp1d(xf_120, yf_120, kind='cubic')


		xf_interp = np.linspace(1.0/(2.0*T)*0.0595, 1.0/(2.0*T)*0.0605, mWinSize/2)

		yf_interp = f_120(xf_interp)

		enfBin.append(xf_interp[np.argmax(yf_interp)]+30.05)

			
	result.put(enfBin)
	return 

def downsampler(name):
	result = subprocess.check_output('sox ' + name + ' -r 1000 d_' + name, shell=True)
	return

if __name__ == '__main__':
	convert_16_bit = float(2**15)
	fs, data = scipy.io.wavfile.read(sys.argv[1])
	#fs, data = scipy.io.wavfile.read('2016-03-12_09_1kHz.wav')
	#fs, data = scipy.io.wavfile.read('d_overlap_004011_921265_33.077-97.0702.wav')
	#fs, data = scipy.io.wavfile.read('ust.wav')

	if fs != 1000:
		downsampler(sys.argv[1])
		print "try downsample!"
		os.system('rm ' + sys.argv[1])
		exit(0)

	N = len(data)
	T = 1/float(fs)
	winSize = 2**13
			

	data = data / (convert_16_bit + 1.0)


	dMono = list()
	try:
		if len(data[0]) == 2:
			for i in range(len(data)):
				dMono.append((data[i][0] + data[i][1])/2)
	except TypeError:
		dMono = data
		print "no error"		


	"""
	x = np.linspace(0.0, T, N)
	y = dMono
	#print (data[:len(data)][0] + data[:len(data)][1])/2
	plt.figure(1)
	plt.plot(x[1:500], y[1:500])
	plt.grid()
	plt.show()
	"""

	numOfMul = 25
	res = list()
	pr = list()
	dataLen = len(dMono)


	for i in range(numOfMul):
		res.append(Queue())

	for i in range(numOfMul):
		pr.append(Process(target=QIFFT, args=(dMono[dataLen*i/numOfMul:dataLen*(i+1)/numOfMul], fs, winSize, winSize/2, res[i], 8)))
		print str(i)+"/"+str(numOfMul) + " ~ " + str(i+1)+"/"+str(numOfMul)

	for i in range(numOfMul):
		pr[i].start()
	print "start"

	for i in range(numOfMul):
		pr[i].join()
	print "join"

	for i in range(numOfMul):
		res[i].put('STOP')
	print "stop"

	enfSum = list()
	for i in range(numOfMul):
		#print res[i].get()
		enfSum.extend(res[i].get())

	x_enf = np.linspace(0.0, 1.0/(2.0*T), len(enfSum))
	#x_enf = np.linspace(0.0, 2.0/(2.0*T), len(enfSum))
	#plt.plot(x_enf, enfSum)
	#plt.axis([0, 1, 59, 61])


	print enfSum
	#sio.savemat('enf.mat', {'enf': enfSum})
	sio.savemat(sys.argv[1], {'enf': enfSum})
	os.system('rm ' + sys.argv[1])
	os.system('mv ' + sys.argv[1]+str('.mat') + ' ' + str(sys.argv[1])[:len(sys.argv[1])-4]+str('.mat'))

	#plt.grid()
	#plt.show()

