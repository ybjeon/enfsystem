import re
import os
import sys
import json
import time as t
from multiprocessing import Process, Queue
from BeautifulSoup import BeautifulSoup
from datetime import datetime, date, time
from livestreamer import Livestreamer, StreamError, PluginError, NoPluginError


PAGENUM = 198

def readJson(filename):
	f = open(filename, 'r')
	js = json.loads(f.read())
	f.close()
	return js


def renewer(dName, outFile, data_list):
	# writedata.py
	f = open(outFile, 'w')
	f.write("var " + dName + " = [")
	f.write(str(data_list))
	f.write("];")
	f.close()

def downloader(url, path, name, lat, lng):
	livestreamer = Livestreamer()
	
	name = str(name).replace(':', '')
	name = path + str('_') + name.replace('.', '_') 

	streams = livestreamer.streams(url)

	try:
		stream = streams["worst"]
	except KeyError:
		return 

	#print "\n\n\n"
	stream = str(stream)[11:len(str(stream))-2]
	#print stream	

	#print("ffmpeg -i " + stream + " -vn -ar 44100 -ac 2 -ab 16k -t 1800 -f wav ./" + path +"/"+ name + "_" + lat.replace('.', '^') + "_" + lng.replace('.', '^') + ".wav &")
	os.system("ffmpeg -i " + stream + " -vn -ar 44100 -ac 2 -ab 16k -t 1800 -f wav ./" + path +"/"+ name + "_" + lat.replace('.', '^') + "_" + lng.replace('.', '^') + ".wav &")

	return 




#totalCount = 0	
def list2Dict(data_list):
	consolidation = []	
#	global totalCount

	pr = list()

	loop = len(data_list)
	
	for n in range(len(data_list)):
		
		#U.S.A
		if (data_list[n][1] > 25 and data_list[n][1] < 50 and data_list[n][2] < -63 and data_list[n][2] > -125):

			consolidation.append(
				"{ 'title':'" + str(data_list[n][0]) 
				+ "' , 'lat':'" + str(data_list[n][1]) 
				+ "' , 'lng':'" + str(data_list[n][2])
				+ "' , 'description':'" + str(data_list[n][0]) 
				+ "' , 'imgUrl':'" + str(data_list[n][3]) 
				#+ "' , 'vidTitle':'" + str(data_list[n][4]) 
				+ "' , 'vidUrl':'www.ustream.tv" + str(data_list[n][5]) 
				+ "'}, "
				+ "\n"		
			)

	#print consolidation

	return ''.join(consolidation)


def downloadStarter(data_list):
	pr = list()

	loop = len(data_list)

	for n in range(loop):
		
		#U.S.A
		if (data_list[n][1] > 25 and data_list[n][1] < 50 and data_list[n][2] < -63 and data_list[n][2] > -125):

			dDate = datetime.now().date()
			dTime = datetime.now().time()

			pr.append(Process(target=downloader, args=("www.ustream.tv" + str(data_list[n][5]), 'usa_ust', str(dDate) + "_" + str(dTime), str(data_list[n][1]), str(data_list[n][2]))))

	for n in range(loop):		
		pr[n].start()	
		t.sleep(0.05)
	for n in range(loop):
		pr[n].join()

	return 


def refiner():
	loc_list_all = []
	coordi_list_all = []
	locNcoordi_list_all = []
	thumbnail_list_all = []
	videoUrl_list_all = []

	i=0 

	for pageNum in range(1, PAGENUM):
		CONFIG_FILE = './data_folder/page'+str(pageNum)

		CONFIG = {}
		CONFIG = readJson(CONFIG_FILE)

	
		pagCnt = CONFIG['pageContent']

		videoSrc = BeautifulSoup(pagCnt)
		videoSrc = videoSrc.findAll('div', attrs={'class':'item-image'})
		videoUrl = BeautifulSoup(str(videoSrc))
		videoUrl = videoUrl.findAll('a')

		for vu in videoUrl:
			videoUrl_list_all.append([(vu['href']).encode('utf-8')])
		#print videoUrl_list_all

		thumbnail = BeautifulSoup(str(videoSrc))
		thumbnail = thumbnail.findAll('img')

		for tm in thumbnail:
			thumbnail_list_all.append([(tm['src']).encode('utf-8')] + [(tm['alt']).encode('utf-8')])

	
		soup = BeautifulSoup(pagCnt)
		crawl = soup.findAll('span', attrs={'class':'item-location'})
		
		location = BeautifulSoup(str(crawl))
		location = location.findAll('a')

		for lo in location:
			lo = BeautifulSoup(str(lo))
			loc_list_all.append([(lo.text).encode('utf-8')])
		
		coordinate = BeautifulSoup(str(crawl))
		coordinate = coordinate.findAll('a')
	
		for co in coordinate:
			splited = re.split(r"[\=\&]*", str(co['href'])[6:])
			coordi_list_all.append([float(splited[1]), float(splited[3])])
			locNcoordi_list_all.append(loc_list_all[i] + coordi_list_all[i] + thumbnail_list_all[i] + videoUrl_list_all[i])
			i=i+1



	#	print thumbnail_list_all

	renewer("markers", "coordinates.js", list2Dict(locNcoordi_list_all))
	downloadStarter(locNcoordi_list_all)

#	renewer("thumbnails", "thumbnails.js", thumbnail_list_all)
		 
	#renewer(locNcoordi_list_all)
	
def main():
	refiner()
	
	
if __name__ == '__main__': 
	main() 
	sys.exit(0)


