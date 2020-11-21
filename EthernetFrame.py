#!/usr/bin/python3

from IPv4Frame import IPv4Frame
from ARPFrame import ARPFrame

class EthernetFrame:

  C_MAC_ADDRESS_LENGTH = 6
  C_ETHERTYPE_LENGTH = 2

  def __init__(self, IPv4protocol=17):
    self.da = [0, 10, 53, 3, 88, 215]
    self.sa = [2, 0, 0, 1, 21, 35]

    if IPv4protocol == 17:
      self.eth = [8, 0]
      self.payload = IPv4Frame(IPv4protocol)
    else: 
      self.eth = [8, 6]
      self.payload = ARPFrame()

  def hexdump(self):
    dump = ""
    for i in range(self.C_MAC_ADDRESS_LENGTH):
      dump = dump + "%02X" % self.da[i]
    for i in range(self.C_MAC_ADDRESS_LENGTH):
      dump = dump + "%02X" % self.sa[i]
    for i in range(self.C_ETHERTYPE_LENGTH):
      dump = dump + "%02X" % self.eth[i]

    dump = dump + self.payload.hexdump()
    return dump


if __name__ == '__main__':
  f = EthernetFrame(111)

  print(f.hexdump())
  print(len(f.hexdump())/2)