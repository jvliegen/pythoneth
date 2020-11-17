#!/usr/bin/python3

class UDPFrame:

  def __init__(self):
    self.sourceport = 235
    self.destinationport = 190
    self.length = 10 + 8
    self.checksum = 0
    self.payload = range(1,11)

  def hexdump(self):
    dump = self.intToHexString(self.sourceport, 4)
    dump = dump + self.intToHexString(self.destinationport, 4)
    dump = dump + self.intToHexString(self.length, 4)
    dump = dump + self.intToHexString(self.checksum, 4)
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

if __name__ == '__main__':
  u = UDPFrame()

  print(u.hexdump())
  print(len(u.hexdump())/2)