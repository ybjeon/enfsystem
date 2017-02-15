import os
import sys
from BeautifulSoup import BeautifulSoup
from datetime import datetime, date, time

PAGENUM = 200
#PAGENUM = 1
recTime = 5400
#name_list = list()

def saver(outFile, data_list):
	f = open(outFile, 'w')
	f.write(str(data_list))
	f.close()

def downloader(url, path, name, mRecTime):
	print "ffmpeg -i " + url + " -vn -ar 44100 -ac 2 -ab 16k -t " + str(mRecTime) + " -f wav " + path + "/" + name.replace('\n', '') + ".wav &"
	#os.system("ffmpeg -i " + url + " -vn -ar 44100 -ac 2 -ab 16k -t " + str(mRecTime) + " -f wav " + path + "/" + name.replace('\n', '') + ".wav &")
	#print ("ffmpeg -i " + url + " -vn -ar 44100 -ac 2 -ab 16k -t " + str(mRecTime) + " -f wav " + path + "/" + name.replace('\n', '') + ".wav &")




def refiner():
	vid_list = []
	f_us = open('./enf_wget/usa/us_list')

	for pageNum in range(0, PAGENUM):
		us_list = f_us.readline()

		dTime = datetime.now().time()
		dDate = datetime.now().date()

		f = open("./enf_wget/usa/" + us_list[:len(us_list)-1])
		pagCnt = f.read()
		coordi = pagCnt

		pagCnt = pagCnt[pagCnt.find('android_livepath'):pagCnt.find('cdn_status')]

		map_lat = coordi[coordi.find('map_lat')+10:coordi.find('map_lat')+27]
		map_long = coordi[coordi.find('map_long')+11:coordi.find('map_long')+29]

#		print map_lat, map_long

		#os.system('mkdir ')

		downloader(str('http://video3.earthcam.com/') + str(pagCnt[pagCnt.find('fecnetwork'):pagCnt.find('flv')+3]).replace('\\', '') + str('/playlist.m3u8'), './usa', us_list + str(dDate) + "_" + str(dTime).replace(':', '')[:6] +"_"+ str(map_lat).replace('.', '-i ^')+str(map_long).replace('.', '^'), recTime)


def main():
	refiner()


if __name__ == '__main__':
	main()
	sys.exit(0)




