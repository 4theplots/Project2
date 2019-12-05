def filter(count):

    for i in range(1, count + 1):
        inputFile = "Node" + str(i) + ".txt"
        outputFile = "N" + str(i) + "Filter.txt"

        f = open(inputFile, "r")
        w = open(outputFile, "w")

        x = f.readline().strip()

        # while not end of file
        while x != "":

            # check to see if file format is as expected
            chk = x[0] + x[1] + x[2]
            if(chk == "No."):
                y = f.readline().strip()
                
                #split data and limit whitespace to 1 character for easier parsing
                dataCols = ' '.join(y.split()).split(' ')



                # Check if Packet is ICMP and an Echo Request/Reply and:
                    # ignore Destination Host Unreachable ICMP Packets then:
                        # Write out packet information entries separated by
                        # '@' line 
                if(dataCols[4] == 'ICMP' and dataCols[6] != "Destination"):

                    w.write("@\n")
                    w.write(x + "\n")
                    w.write(y + "\n")

                    f.readline().strip()
                    out = f.readline().strip()

                    # write out lines of packet data
                    while out != "":
                        w.write(out + "\n")
                        out = f.readline().strip()

                    # move to next packet data entry
                    x = f.readline().strip()

                # end if

                # Packet being ignored, move to next packet in source file

                else:
                    x = f.readline().strip()
                    x = f.readline().strip()
                    while(x != ""):
                        x = f.readline().strip()
                    x = f.readline().strip()
filter(1)