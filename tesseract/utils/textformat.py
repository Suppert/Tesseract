# textformat.py
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
Class TextFormat():    
    GREEN = '\x1b[1;32;40m'
    RED = '\x1b[1;31;40m'
    AQUA = '\x1b[1;34;40m'
    PURPLE = '\x1b[1;35;40m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    @staticmethod
    def toANSI(text):
        if type(text) == string:
            text.replace("§c", TextFormat.RED)
            text.replace("§4", TextFormat.RED)
            text.replace("§3", TextFormat.AQUA)
            text.replace("§b", TextFormat.AQUA)
            text.replace("§L", TextFormat.BOLD)
            text.replace("§n", TextFormat.UNDERLINE)
            text.replace("§d", TextFormat.PURPLE)
            text.replace("§5", TextFormat.PURPLE)
            return text + TextFormat.END

