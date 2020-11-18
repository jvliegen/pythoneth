#!/usr/bin/python3

class TCPFrame:

  def __init__(self, PLsize=10):
    self.sourceport = 235
    self.destinationport = 190
    self.sequencenumber = 0xFEDC
    self.acknumber = 0xBA98
    self.flags = 0x7654
    self.windowsize = 0x3210
    self.checksum = 0
    self.urgentpointer = 0
    self.payload = range(1,1+PLsize)

  def hexdump(self):
    dump = self.intToHexString(self.sourceport, 4)
    dump = dump + self.intToHexString(self.destinationport, 4)
    dump = dump + self.intToHexString(self.sequencenumber, 8)
    dump = dump + self.intToHexString(self.acknumber, 8)
    dump = dump + self.intToHexString(self.flags, 4)
    dump = dump + self.intToHexString(self.windowsize, 4)
    dump = dump + self.intToHexString(self.checksum, 4)
    dump = dump + self.intToHexString(self.urgentpointer, 4)
    dump = dump + self.listToHexString(self.payload)
    return dump

  def intToHexString(self, a, minLength=2):
    hexstring = ""
    while a > 0:
      remainder = a % 256
      hexstring =  "%02X" % remainder + hexstring
      a = int((a - remainder)/256)
    while(len(hexstring) < minLength):
      hexstring = "00" + hexstring
    return hexstring

  def listToHexString(self, a):
    hexstring = ""
    for i in range(len(a)):
      hexstring = hexstring + "%02X" % a[i]
    return hexstring

  def getSize(self):
    return 20 + len(self.payload)

if __name__ == '__main__':
  t = TCPFrame()

  print(t.hexdump())
  print(len(t.hexdump())/2)