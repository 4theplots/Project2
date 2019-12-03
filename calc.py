import parse as p

f = open("N1Filter.txt", "r")



L = p.parsefile(f)

print(str(len(L)))

def calculate(parsedPackets, nodeMac):
    reqSent = 0
    reqRec = 0
    repSent = 0
    repRec = 0

    reqBytesSent = 0
    reqBytesRec = 0

    reqDataSent = 0
    reqBytesRec = 0



    sequenceDict = dict()
    for packet in parsedPackets:
        ## Request Packet Path
        if packet['Type'] == 8:
            ## sent by node
            if packet['SrcMac'] == nodeMac:
                reqSent += 1
                reqBytesSent += packet['TotalLen'] + 14
            ## received by node
            else:
                reqRec += 1
                reqBytesRec += packet['TotalLen'] + 14


        ## Reply Packet Path
        else:
            ## sent by node
            if packet['SrcMac'] == nodeMac:
                repSent += 1
            ## received by node
            else:
                #print(packet['SrcMac'])
                repRec += 1

    print("Echo Request Sent: " + str(reqSent))
    print("Echo Requests Received: " +  str(reqRec))
    print("Echo Replies Sent: "  + str(repSent))
    print("Echo Replies Received: " + str(repRec))

    print("Echo Request Bytes Sent: " + str(reqBytesSent))
    print("Echo Request Bytes Received: " + str(reqBytesRec))
calculate(L, "ec:b1:d7:43:89:be")