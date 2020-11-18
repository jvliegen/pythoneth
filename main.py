#!/usr/bin/python3

from EthernetFrame import EthernetFrame

def hexdumpToAXI4Stream(hd):
  stream = ""
  for i in range(0, len(hd)-2, 2):
    stream = stream + hd[i:i+2] + " 1 0\n"
  stream = stream + hd[-2:] + " 1 1\n"
  return stream

f = EthernetFrame()

ifg = "00 0 0\n"
frame = hexdumpToAXI4Stream(f.hexdump())

fh = open("gen/axistream.dat", "w")
fh.write(frame)
fh.write(ifg)
fh.write(frame)
fh.write(ifg)
fh.write(frame)
fh.close()
