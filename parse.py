f = open("Node1.txt", "r")

nextPacket = True


x = f.readline().strip()
x = f.readline().strip()
x = f.readline().strip()
x = f.readline().strip()

while(nextPacket):
    line = x.split(" ")
    print(line)
    destMac = line[2] + ":" + line[3] + ":" + line[4] + ":" + line[5] + ":" + line[6] + ":" + line[7]
    srcMac = line[8] + ":" + line[9] + ":" + line[10] + ":" + line[11] + ":" + line[12] + ":" + line[13]

    #destMac = int(destMac, 16)
    #srcMac = int(srcMac, 16)

    print('Dest Mac: ' + str(destMac))
    print('Src Mac: ' + str(srcMac))

    frameLength = int((line[14] + line[15]), 16)

    print('Length: ' + str(frameLength))

    protocolType = line[16]

    print('Type: ' + protocolType)

    if(protocolType != "45"):
        while(f.readline().strip() != ""):
            continue
    
    #TODO Add functionality for good path IPv4 packet found

    x = f.readline().strip()

    if(x == ""):
        nextPacket = False
    
    x = f.readline().strip()
