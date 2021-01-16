import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="key_name")
parser.add_argument("--val", help="value")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path) is not True:
	with open(storage_path, 'w') as f:
		f.write(json.dumps(dict()))


def writter(key, val, storage_path):

	with open(storage_path, 'r') as f:
		content = f.read()
	python_dict = json.loads(content)

	if key in python_dict:
		python_dict[key].append(val)
	else:
		python_dict[key] = [val]


	with open(storage_path, 'w') as f:
		f.write(json.dumps(python_dict))

	print(', '.join(python_dict[key]))


def sender(key, storage_path):
	with open(storage_path, 'r') as f:
		content = f.read()
	python_dict = json.loads(content)
	if key in python_dict:
		print(', '.join(python_dict[key]))
	else:
		print(None)


if args.val is None:
	sender(args.key, storage_path)
else:
	writter(args.key, args.val, storage_path)
