import os
import csv
import json
import gdown

urls = {}
with open('index.csv', 'r') as f:
	reader = csv.reader(f)	
	for row in reader:
		urls[row[0]] = row[1].replace("file/d/", "uc?id=").replace("/view?usp=sharing", '')

def pull(*names):
	for name in names:
		if not os.path.exists(name):
			gdown.download(urls[name], name, quiet=False)
	return None
