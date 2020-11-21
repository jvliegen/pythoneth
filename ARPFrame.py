#!/usr/bin/python3

class ARPFrame:


  C_HTYPE = 4
  C_PTYPE = 2048
  C_HLEN = 6
  C_PLEN = 4

  def __init__(self, operation=1):
    self.oper = 1 # 1: request, 2: reply
    self.sha = [2, 0, 0, 1, 21, 35]
    self.spa = [192, 168, 23, 1]
    self.tha = [0, 10, 53, 3, 88, 215]
    self.tpa = [192, 168, 23, 235]

  def hexdump(self):
    dump = self.intToHexString(self.C_HTYPE, 4)
    dump = dump + self.intToHexString(self.C_PTYPE, 4)
    dump = dump + self.intToHexString(self.C_HLEN, 2)
    dump = dump + self.intToHexString(self.C_PLEN, 2)
    dump = dump + self.intToHexString(self.oper, 4)
    dump = dump + self.listToHexString(self.sha)
    dump = dump + self.listToHexString(self.spa)
    dump = dump + self.listToHexString(self.tha)
    dump = dump + self.listToHexString(self.tpa)
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
    return 28

if __name__ == '__main__':
  u = UDPFrame(20)

  print(u.hexdump())
  print(len(u.hexdump())/2)