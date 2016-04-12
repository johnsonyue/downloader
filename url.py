import urllib
import HTMLParser

class CaidaParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self);
		self.img_cnt=0;
		self.alt="";
		self.file=[];
		self.dir=[];

	def get_attr_value(self, target, attrs):
		for e in attrs:
			key = e[0];
			value = e[1];
			if (key == target):
				return value;

	def handle_starttag(self, tag, attrs):
		if (tag == "img"):
			if (self.img_cnt >=2):
				alt_value = self.get_attr_value("alt", attrs);
				self.alt=alt_value;
			self.img_cnt = self.img_cnt + 1;
		
		if (tag == "a" and self.alt == "[DIR]"):
			href_value = self.get_attr_value("href", attrs);
			self.dir.append(href_value);
		elif (tag == "a" and self.alt != ""):
			href_value = self.get_attr_value("href", attrs);
			self.file.append(href_value);

def recursive_download_dir(depth, path):
	f = urllib.urlopen(path);
	text = f.read();

	parser = CaidaParser();
	parser.feed(text);

	for e in parser.file:
		i = 0;
		while i < depth:
			print "--",
			i = i+1;
		print e;

	for e in parser.dir:
		i = 0;
		while i < depth:
			print "--",
			i = i+1;
		print e;
		recursive_download_dir(depth+1, path+e)

seed = "http://data.caida.org/datasets/topology/ark/"
recursive_download_dir(0, seed);
