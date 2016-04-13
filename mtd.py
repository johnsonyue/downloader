from multiprocessing import Pool
import urllib
import os

def download(url):
	#text = urllib.open(url).read();
	print "download", url,"done";

if __name__=='__main__':
	a = "www.baidu.com"
	b = "www.bing.com"
	c = "www.sohu.com"

	list = [a, b, c];

	print "parent pid:",os.getpid();
	p = Pool(4);
	for i in range(3):
		print "start task", i;
		p.apply_async(download,args=(i,));

	print "waiting..";
	p.close();
	p.join();

print "done.";
