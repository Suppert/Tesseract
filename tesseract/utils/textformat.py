# textformat.py
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
