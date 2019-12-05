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
    replyDelay = 0.0



    seqDict = dict()
    delayDict = dict()

    calcs = []

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
                if seqNum in delayDict:
                    delayDict[seqNum][0] = float(packet['Time'])
                else:
                    delayDict[seqNum] = [float(packet['Time']), 0]
                reqRec += 1
                reqBytesRec += packet['TotalLen'] + 14
                reqDataRec += packet['TotalLen'] - 28


        ## Reply Packet Path
        else:

            
            ## sent by node
            if packet['SrcIP'] == nodeIP:
                repSent += 1
                if seqNum in delayDict:
                    delayDict[seqNum][1] = float(packet['Time'])
                else:
                    delayDict[seqNum] = [0, float(packet['Time'])]
            ## received by node
            else:
            ## increment running total of Req Hop Count
                reqHopCount += (129 - packet['TTL'])
                #print(packet['SrcMac'])
                repRec += 1

                ## Add time to sequence dictionary for later calculation
                if seqNum in seqDict:
                    seqDict[seqNum][1] = float(packet['Time'])
                else:
                    seqDict[seqNum] = [0, float(packet['Time'])]

    # end for loop

    avgHopCount = round(float(reqHopCount) / float(repRec), 2)



    for p in seqDict:
        d = seqDict.get(p)
        ## sum time difference from request to reply
        RTT += (d[1] - d[0])

    for p in delayDict:
        d = delayDict.get(p)
        replyDelay += (d[1] - d[0])



    replyDelay = round((replyDelay / repSent) * 1000000,2)
    throughPut = reqBytesSent

    throughPut = round( (reqBytesSent / 1000) / RTT, 1)
    goodPut = round( (reqDataSent / 1000) / RTT, 1)

    
    ## Calculate average RTT and convert to MS
    RTT = round( (RTT / reqSent) * 1000, 2)

    calcs.append(str(reqSent))
    calcs.append(str(reqRec))
    calcs.append(str(repSent))
    calcs.append(str(repRec))

    calcs.append(str(reqBytesSent))
    calcs.append(str(reqDataSent))
    

    calcs.append(str(reqBytesRec))
    calcs.append(str(reqDataRec))


    calcs.append(str(RTT))
    calcs.append(str(throughPut))
    calcs.append(str(goodPut))
    calcs.append(str(replyDelay))

    calcs.append(str(avgHopCount))

    return calcs
