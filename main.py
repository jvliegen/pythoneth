#!/usr/bin/python3

from EthernetFrame import EthernetFrame

def hexdumpToAXI4Stream_8bit(hd):
  stream = ""
  for i in range(0, len(hd)-2, 2):
    stream = stream + hd[i:i+2] + " 1 1 0\n"
  stream = stream + hd[-2:] + " 1 1 1\n"
  return stream

def hexdumpToAXI4Stream_32bit(hd):
  stream = ""
  for i in range(0, len(hd)-8, 8):
    word = hd[i:i+8]
    word.rjust(8, '0')
    stream = stream + word + " 1111 1 0\n"

  word = hd[-8:]
  word.rjust(8, '0')
  stream = stream + word + " 1110 1 1\n"
  return stream

# Generate frames
f_arp = EthernetFrame(6)
f_udp = EthernetFrame(0, 17)
f_tcp = EthernetFrame(0, 6)
f_icmp = EthernetFrame(0, 1)

data_width = 32

if data_width == 32: 
  # Prepare hexdumps of frames + InterFrameGap
  frame_arp = hexdumpToAXI4Stream_32bit(f_arp.hexdump())
  frame_udp = hexdumpToAXI4Stream_32bit(f_udp.hexdump())
  frame_tcp = hexdumpToAXI4Stream_32bit(f_tcp.hexdump())
  frame_icmp = hexdumpToAXI4Stream_32bit(f_icmp.hexdump())
  ifg = "00000000 0000 0 0\n"

  fh = open("gen/axistream_32.dat", "w")
  fhg = open("gen/axistream_golden_32.dat", "w")
else:
  # Prepare hexdumps of frames + InterFrameGap
  frame_arp = hexdumpToAXI4Stream_8bit(f_arp.hexdump())
  frame_udp = hexdumpToAXI4Stream_8bit(f_udp.hexdump())
  frame_tcp = hexdumpToAXI4Stream_8bit(f_tcp.hexdump())
  frame_icmp = hexdumpToAXI4Stream_8bit(f_icmp.hexdump())
  ifg = "00 0 0 0\n"*12
  fh = open("gen/axistream_8.dat", "w")
  fhg = open("gen/axistream_golden_8.dat", "w")


print(frame_udp)


# Write scenario to simulation model input file
fh.write(frame_arp)
fh.write(ifg)
fh.write(frame_icmp)
fh.write(ifg)
fh.write(frame_udp)
fh.write(ifg)
fh.write(frame_udp)
fh.write(ifg)
fh.write(frame_tcp)
fh.write(ifg)
fh.write(frame_tcp)
fh.write(ifg)
fh.close()

# Write scenario to simulation model input file
fhg.write(frame_arp)
fhg.write(frame_icmp)
fhg.write(frame_udp)
fhg.write(frame_udp)
fhg.write(frame_tcp)
fhg.write(frame_tcp)
fhg.close()