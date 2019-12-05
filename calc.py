import parse as p

f = open("N1Filter.txt", "r")



L = p.parsefile(f)

print(str(len(L)))

def calculate(parsedPackets, nodeIP):
    reqSent = 0
    reqRec = 0
    repSent = 0
    repRec = 0

    reqBytesSent = 0
    reqBytesRec = 0

    reqDataSent = 0
    reqDataRec = 0

    RTT = 0
    reqHopCount = 0

    throughPut = 0
    goodPut = 0



    seqDict = dict()

    for packet in parsedPackets:


        seqNum = packet['SeqNum']


        ## Request Packet Path
        if packet['Type'] == 8:
            


            


            ## sent by node
            if packet['SrcIP'] == nodeIP:
                reqSent += 1
                reqBytesSent += packet['TotalLen'] + 14
                reqDataSent += packet['TotalLen'] - 28

                ## Add time to sequence dictionary for later calculation
                if seqNum in seqDict:
                    seqDict[seqNum][0] = float(packet['Time'])
                else:
                    seqDict[seqNum] = [float(packet['Time']), 0]

            ## received by node
            else:
                reqRec += 1
                reqBytesRec += packet['TotalLen'] + 14
                reqDataRec += packet['TotalLen'] - 28


        ## Reply Packet Path
        else:

            
            ## sent by node
            if packet['SrcIP'] == nodeIP:
                repSent += 1
            ## received by node
            else:
            ## increment running total of Req Hop Count
                reqHopCount += 129 - packet['TTL']
                #print(packet['SrcMac'])
                repRec += 1

                ## Add time to sequence dictionary for later calculation
                if seqNum in seqDict:
                    seqDict[seqNum][1] = float(packet['Time'])
                else:
                    seqDict[seqNum] = [0, float(packet['Time'])]

    # end for loop

    reqHopCount = round(reqHopCount / repRec, 2)


    for p in seqDict:
        d = seqDict.get(p)
        ## sum time difference from request to reply
        RTT += (d[1] - d[0])

    
    throughPut = reqBytesSent

    throughPut = round( (reqBytesSent / 1000) / RTT, 1)
    goodPut = round( (reqDataSent / 1000) / RTT, 1)

    
    ## Calculate average RTT and convert to MS
    RTT = round( (RTT / reqSent) * 1000, 2)



    print("Echo Request Sent: " + str(reqSent))
    print("Echo Requests Received: " +  str(reqRec))
    print("Echo Replies Sent: "  + str(repSent))
    print("Echo Replies Received: " + str(repRec))

    print("Echo Request Bytes Sent: " + str(reqBytesSent))
    print("Echo Request Bytes Received: " + str(reqBytesRec))

    print("Echo Request Data Sent: " + str(reqDataSent))
    print("Echo Request Data Received: " + str(reqDataRec))

    print()

    print("Average RTT (ms): " + str(RTT))
    print("Echo Request Throughput (kB/sec): " + str(throughPut))
    print("Echo Request Goodput (kB/sec): " + str(goodPut))

    print()
    print("Average Echo Request Hop Count: " + str(reqHopCount))
    
calculate(L, "192.168.100.1")