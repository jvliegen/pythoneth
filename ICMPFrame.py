#!/usr/bin/python3

class ICMPFrame:

  def __init__(self):
    self.type = 8               # type: Echo request
    self.code = 0
    self.checksum = 0
    self.id = 0
    self.seqnumber = 0
    self.payload = range(1,1+48)
    self.updateChecksum()

  def hexdump(self):
    dump = self.intToHexString(self.type)
    dump = dump + self.intToHexString(self.code)
    dump = dump + self.intToHexString(self.checksum,4)
    dump = dump + self.intToHexString(self.id,4)
    dump = dump + self.intToHexString(self.seqnumber,4)
    dump = dump + self.listToHexString(self.payload)
    return dump

  def intToHexString(self, a, minLength=2):
    hexstring = ""
    while a > 0:
      remainder = a % 256
      hexstring = "%02X" % remainder + hexstring
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
    return 8+len(self.payload)

  def updateChecksum(self):
    self.checksum = 0
    hexstring = self.hexdump()[0:self.getSize()*2]
    doubleByteSum = 0
    for i in range(0,len(hexstring),4):
      doubleByteSum = doubleByteSum + int(hexstring[i:i+4], 16)

    while doubleByteSum > 65536:
      doubleByteSum = (doubleByteSum % 65536) + int((doubleByteSum - (doubleByteSum % 65536))/65536)

    self.checksum = 65535 - doubleByteSum



if __name__ == '__main__':
  i = ICMPFrame()

  print(i.hexdump())
  print(len(i.hexdump())/2)



