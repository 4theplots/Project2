def parsefile(f):
    packets = []
    x = f.readline().strip()

    while(x != ""):
        packet = dict()
        
        
        f.readline()
        x = f.readline().strip()
        line = ' '.join(x.split()).split(' ')


        packetNum = line[0]
        packetTime = line[1]


        x = f.readline().strip()
        line = ' '.join(x[6:].split()).split(' ')

        destMac = line[0] + ":" + line[1] + ":" + line[2] + ":" + line[3] + ":" + line[4] + ":" + line[5]
        srcMac = line[6] + ":" + line[7] + ":" + line[8] + ":" + line[9] + ":" + line[10] + ":" + line[11]

        headerLength = int(line[14][1]) * 4


    ## Hex line 2
        x = f.readline().strip()
        line = ' '.join(x[6:53].split()).split(' ')

        # Set Packet Length value and convert from hex to decimal
        totalLength = int(line[0] + line[1], 16)

        # Set Time to Live value and convert from hex to decimal
        timeToLive = int(line[6], 16)

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

        # concatenate destination IP hex fields
        # and convert the hex value to string
        destinationIP += str(int(line[0], 16)) + '.' + str(int(line[1],16))

        icmpType = int(line[2],16)

        seqNum = int(line[8] + line[9], 16)

        
        # set packet values and add to list of packets
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

        # move file reader to next packet or EOF
        x = f.readline().strip()
        while x != "@":
            if x == "":
                break
            x = f.readline().strip()

    
    return packets