"""
THIS IS COPIED FROM THE SPIFFY SERVER SOFTWARRE
LINK: https://github.com/spiffy/spiffy
"""

import json
import os.path

def generate_config():
	target = open('settings.json', 'w')
	config = {
		  "port": 19132,
		  "name": "A Minecraft: PE Server"
		}
	parsed = config
	json.dump(parsed,target, indent = 4, sort_keys = True)

def load_config():
	with open('settings.json', 'r') as handle:
		parsed = json.load(handle)
		return parsed

def handle_config():
	if os.path.isfile('settings.json'):
		return load_config()
	else:
		generate_config()
		return load_config()
