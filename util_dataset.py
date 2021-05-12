import json
import random
import pandas as pd
from collections import OrderedDict

def split(directory, sets = ['train', 'test'], ratio = 0.3, shuffle = 1, seed = random.randint(1, 1000)):
	with open(directory, 'r') as f:
		dataset = f.readlines()

	if shuffle:
		random.seed(seed)
		random.shuffle(dataset)
		
	sets.reverse()
	
	num = len(dataset)
	
	datasets = OrderedDict()
	
	for x in sets[:-1]:
		datasets[x] = dataset[round(num * (1 - ratio)):]
		dataset = dataset[0:round(num * (1 - ratio))]
		assert num == len(dataset) + len(datasets[x])
		num = len(dataset)
	datasets[sets[-1]] = dataset
	
	directories = []
	for key, value in datasets.items():
		name = directory.replace('.json', '-' + key + '.json')
		with open(name, 'w') as f:
			f.writelines(value)
		directories.append(name)
			
	return tuple(directories)[::-1]

def concatenate(*directories, destiny = 'concatenated.json', shuffle = 1, seed = random.randint(1, 1000)):
	dataset = []
	for directory in directories:
		with open(directory, 'r') as f:
			dataset += f.readlines()

	shuffle = 1
	if shuffle:
		random.shuffle(dataset)

	with open(destiny, 'w') as g:
		g.writelines(dataset)

	return len(dataset)

def json2csv(directory, shuffle = False):
	with open(directory, 'r') as f:
		dataset = f.readlines()

	if shuffle:
		random.seed(seed)
		random.shuffle(dataset)

	df_dict = OrderedDict()
	for x in dataset:
		datum = json.loads(x)
		for key, value in datum.items():
			if key not in df_dict:
				df_dict[key] = [value]
			else:
				df_dict[key].append(value)

	assert len(set([len(x) for x in df_dict.values()])) == 1

	# Set up the dataframe
	df = pd.DataFrame(df_dict)

	df.to_csv(directory.replace('.json', '.csv'), index = False)

	return directory.replace('.json', '.csv')

def toy(directory, num = 100, shuffle = 1, seed = random.randint(1, 1000)):
	with open(directory, 'r') as f:
		dataset = f.readlines()

	if shuffle:
		random.seed(seed)
		random.shuffle(dataset)

	with open(directory.replace('.json', '-toy.json'), 'w') as f:
		f.writelines(dataset[0:num])

	return directory.replace('.json', '-toy.json')
