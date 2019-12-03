f = open("N1Filter.txt", "r")

def parsefile(f):
    packets = []
    x = f.readline().strip()

    while(x != ""):
        packet = dict()
        
        
        f.readline()
        x = f.readline().strip()
        line = ' '.join(x.split()).split(' ')
        #print(line)

        packetNum = line[0]
        packetTime = line[1]

        #print("Packet #: " + packetNum)
        #print("Packet Time: " + packetTime)

        x = f.readline().strip()
        line = ' '.join(x[6:].split()).split(' ')
        #print (line)

        destMac = line[0] + ":" + line[1] + ":" + line[2] + ":" + line[3] + ":" + line[4] + ":" + line[5]
        srcMac = line[6] + ":" + line[7] + ":" + line[8] + ":" + line[9] + ":" + line[10] + ":" + line[11]

        #destMac = int(destMac, 16)
        #srcMac = int(srcMac, 16)

        #print('Dest Mac: ' + str(destMac))
        #print('Src Mac: ' + str(srcMac))

        protocolType = line[12] + line[13]

        #print('Type: ' + protocolType)

        headerLength = int(line[14][1]) * 4

        #print('Header Length: ' + str(headerLength))

    ## Hex line 2
        x = f.readline().strip()
        line = ' '.join(x[6:53].split()).split(' ')
        #print (line)

        totalLength = int(line[0] + line[1], 16)

        #print("Total Length: " + str(totalLength))

        timeToLive = int(line[6], 16)

        #print("Time to Live: " + str(timeToLive))

        sourceIP = ''

        ## BUILD IP ADDRESS WITH DOTS
        for i in range(10,14):
            sourceIP += str(int(line[i], 16))
            if(i == 13):
                break
            else:
                sourceIP += "."
        
        destinationIP = str(int(line[14],16)) + '.' + str(int(line[15], 16)) + "."

        ## HEX LINE 3
        x = f.readline().strip()
        line = ' '.join(x[6:53].split()).split(' ')
        #print (line)

        destinationIP += str(int(line[0], 16)) + '.' + str(int(line[1],16))


        #print("Source IP: " + str(sourceIP))
        #print("Destination IP: " + str(destinationIP))

        icmpType = int(line[2],16)

        #print("ICMP Type: " + str(icmpType))

        seqNum = int(line[8] + line[9], 16)

        #print("Seq. #: " + str(seqNum))

        packet['Num'] = packetNum
        packet['Time'] = packetTime
        packet['DestMac'] = destMac
        packet['SrcMac'] = srcMac
        packet['HeadLen'] =  headerLength
        packet['TotalLen'] = totalLength
        packet['TTL'] = timeToLive
        packet['DestIP'] = destinationIP
        packet['SrcIP'] = sourceIP
        packet['Type'] = icmpType
        packet['SeqNum'] = seqNum


        packets.append(packet)

        x = f.readline().strip()
        while x != "@":
            if x == "":
                break
            x = f.readline().strip()

    
    return packets

print(parsefile(f)[0])