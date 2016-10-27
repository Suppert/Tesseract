# textformat.py
Class TextFormat():
  GREEN = "\x1b[1;32;40m"
  RED = "\x1b[1;31;40m"
  
  @staticmethod
  def toANSI(string):
    if type(string) == string:
      #todo
