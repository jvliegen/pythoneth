#!/usr/bin/python3

from UDPFrame import UDPFrame

class IPv4Frame:

  C_VERSION = 4
  C_IHL = 5
  C_DSCP_ECN = 255
  C_ID = 65535
  C_FLAGS_OFFSET = 1024
  C_TTL = 64

  def __init__(self):
    self.totallength = 0
    self.protocol = 17
    self.checksum = 0
    self.sa = [192, 168, 1, 1]
    self.da = [192, 168, 1, 201]
    self.payload = UDPFrame()

  def hexdump(self):
    dump = self.intToHexString(self.C_VERSION*16+self.C_IHL)
    dump = dump + self.intToHexString(self.C_DSCP_ECN)
    dump = dump + self.intToHexString(self.totallength,4) 
    dump = dump + self.intToHexString(self.C_ID,4)
    dump = dump + self.intToHexString(self.C_FLAGS_OFFSET,4)
    dump = dump + self.intToHexString(self.C_TTL)
    dump = dump + self.intToHexString(self.protocol)
    dump = dump + self.intToHexString(self.checksum,4)
    dump = dump + self.listToHexString(self.sa)
    dump = dump + self.listToHexString(self.da)

    dump = dump + self.payload.hexdump()
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


if __name__ == '__main__':
  i = IPv4Frame()

  print(i.hexdump())
  print(len(i.hexdump())/2)