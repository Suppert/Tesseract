"""
   _____                                 _   
  |_   _|                               | |  
    | | ___  ___ ___  ___ _ __ __ _  ___| |_ 
    | |/ _ \/ __/ __|/ _ \ '__/ _` |/ __| __|
    | |  __/\__ \__ \  __/ | | (_| | (__| |_ 
    \_/\___||___/___/\___|_|  \__,_|\___|\__|                                                                                   
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
"""
from resources import config
import sys

try:
  from pyraklib.server import PyRakLibServer
  from pyraklib.server import ServerHandler
  found = True
except ImportError:
  found = False
  pass

if not found:
  sys.exit("Unable to load all modules")

config = config.handle_config()
server = PyRakLibServer(config['port'])
print("Tesseract is licensed under the GNU license")
print("starting server on *:" + str(config['port']))
