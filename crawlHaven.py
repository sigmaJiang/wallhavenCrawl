import urllib2
from urllib2 import HTTPError, URLError
import math
import sys
import time
import random

print "The start time: "+time.ctime()
x = input("Start value:")
y = input("Stop value:")
k = y-x
for i in range(x, y+1):
	#save path 
	path = '/home/sigmaj/Documents/python/'
	url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'+str(i)+'.jpg'
	req = urllib2.Request(url)
	req.add_header("User-agent", "Mozilla 5.10")
	name = str(path)+'wallhaven-'+str(i)+'.jpg'
	url2 = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-'+str(i)+'.png'
	req2 = urllib2.Request(url2)
	req2.add_header("User-agent", "Mozilla 5.10")
	name2 = str(path)+'wallhaven-'+str(i)+'.png'
	try:
		conn = urllib2.urlopen(req)
		f = open(name, 'wb')
		f.write(conn.read())
		f.close()
		if k < 100:
			sys.stdout.write("Computing: [%s%s] %.2f%%\r" % ('#' * (i-x) , '-' * (y-i), (i-x)*100/k))
			sys.stdout.flush()
			time.sleep(0.1)
		else:
			sys.stdout.write("Computing: [%s%s] %.2f%% \r" % ('#' * ((i-x)/(k/50)) , '-' * ((y-i)/(k/50)), (i-x)*100.0/k))
			sys.stdout.flush()
			time.sleep(0.1)
		time.sleep(random.uniform(0,2))
	except HTTPError ,e:
		print i,e.code
		try:
			conn2 = urllib2.urlopen(req2)
			f2 = open(name2, 'wb')
			f2.write(conn2.read())
			f2.close()
		except HTTPError, e:
			print 'download','PIC'+str(i),'fail',e.code
		except URLError, e:
			print "url error",e.code
		i = i+1
	except URLError, e:
		print "The server\'s something is wrong!"
		print e.code
		print e.read()
		break
print "\nThe finished time: "+time.ctime()
print 'pic saved'
