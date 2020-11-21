#!/usr/bin/python3

from EthernetFrame import EthernetFrame

def hexdumpToAXI4Stream_8bit(hd):
  stream = ""
  for i in range(0, len(hd)-2, 2):
    stream = stream + hd[i:i+2] + " 1 0\n"
  stream = stream + hd[-2:] + " 1 1\n"
  return stream

def hexdumpToAXI4Stream_32bit(hd):
  stream = ""
  for i in range(0, len(hd)-8, 8):
    word = hd[i:i+8]
    word.rjust(8, '0')
    stream = stream + word + " 1 0\n"

  word = hd[-8:]
  word.rjust(8, '0')
  stream = stream + word + " 1 1\n"
  return stream

# Generate frames
f_arp = EthernetFrame(1111)
f_udp = EthernetFrame(17)
f_tcp = EthernetFrame(6)


# Prepare hexdumps of frames + InterFrameGap
frame_arp = hexdumpToAXI4Stream_32bit(f_arp.hexdump())
frame_udp = hexdumpToAXI4Stream_32bit(f_udp.hexdump())
frame_tcp = hexdumpToAXI4Stream_32bit(f_tcp.hexdump())
ifg = "00000000 0 0\n"

# Prepare hexdumps of frames + InterFrameGap
frame_arp = hexdumpToAXI4Stream_8bit(f_arp.hexdump())
frame_udp = hexdumpToAXI4Stream_8bit(f_udp.hexdump())
frame_tcp = hexdumpToAXI4Stream_8bit(f_tcp.hexdump())
ifg = "00 0 0\n"*12


# Write scenario to simulation model input file
fh = open("gen/axistream.dat", "w")
fh.write(frame_arp)
fh.write(ifg)
fh.write(frame_arp)
# fh.write(ifg)
# fh.write(frame_udp)
# fh.write(ifg)
# fh.write(frame_udp)
# fh.write(ifg)
# fh.write(frame_tcp)
# fh.write(ifg)
# fh.write(frame_tcp)
# fh.write(ifg)
# fh.write(frame_tcp)
# fh.write(ifg)
fh.close()
