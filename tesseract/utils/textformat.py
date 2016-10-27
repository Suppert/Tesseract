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
  def toANSI(string):
    if type(string) == string:
      #todo
