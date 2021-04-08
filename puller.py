import os
import csv
import json
import gdown

with open('index.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)

# url = 'https://drive.google.com/uc?id=1qj2ZPXHOC8e9d28l119kdSuyJQ2hVY1H'
# output = 'replace-3-train.json'
# gdown.download(url, output, quiet=False)
