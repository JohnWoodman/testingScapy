#Figure out how to forward traffic (use stackoverflow post)
#Figure out how to arpspoof (stackoverflow)
#Figure out how to manipulate traffic (consider using sniff() instead of SniffSource)


from scapy.all import *

s = SniffSource(filter = 'dst port 80')

d1 = Drain()

#d2 = TransformDrain(lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))

#d2 = TransformDrain(lambda x: hexdump(x.load)) 

si1 = QueueSink()

s > d1
#d1 > d2
#d2 > si1
d1 > si1

p = PipeEngine()
p.add(s)
p.start()

while True:
	#print(si1.recv())
	if si1.recv() is not None:
		print("Captured packet")
		time.sleep(5)
		print("Forwarding packet")
		sendp(si1.recv())

