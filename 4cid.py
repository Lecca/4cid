import argparse, os, re
try:
	import urllib.request as urllib
except ImportError:
	import urllib

def urlget(board, thread):
	return("https://boards.4chan.org/"+board+"/thread/"+thread)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("board")
	parser.add_argument("thread")
	args = parser.parse_args()
	wdir = os.path.dirname(os.path.abspath(__file__))
	ddir = os.path.join(wdir,'downloads',args.board,args.thread)
	if not os.path.exists(ddir):
		os.makedirs(ddir)
	url = urlget(args.board, args.thread)
	sturl = str(urllib.urlopen(url).read())
	for _ in re.findall('//i.4cdn.org/\w+/\d*\.\w{3,4}?',sturl):
		try:
			imgdir = os.path.join(ddir, _[15:])
			imglink = 'http:'+_
			urllib.urlretrieve(imglink, imgdir)
			print('Downloaded '+imglink)
		except Exception as e:
			print(e)

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print(e)
