#!/usr/bin/python3

from EthernetFrame import EthernetFrame

def hexdumpToAXI4Stream(hd):
  stream = ""
  for i in range(0, len(hd)-2, 2):
    stream = stream + hd[i:i+2] + " 1 0\n"
  stream = stream + hd[-2:] + " 1 1\n"
  return stream

# Generate frames
f_udp = EthernetFrame(17)
f_tcp = EthernetFrame(6)


# Prepare hexdumps of frames + InterFrameGap
frame_udp = hexdumpToAXI4Stream(f_udp.hexdump())
frame_tcp = hexdumpToAXI4Stream(f_udp.hexdump())
ifg = "00 0 0\n"

# Write scenario to simulation model input file
fh = open("gen/axistream.dat", "w")
fh.write(frame_udp)
fh.write(ifg)
fh.write(frame_udp)
fh.write(ifg)
fh.write(frame_udp)
fh.write(ifg)
fh.write(frame_tcp)
fh.write(ifg)
fh.write(frame_tcp)
fh.write(ifg)
fh.write(frame_tcp)
fh.write(ifg)
fh.close()
