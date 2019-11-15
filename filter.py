f = open("Node1.txt", "r")
w = open("N1Filter.txt", "w")

x = f.readline().strip()

# while not end of file
while x != "":

    # check to see if file format is as expected
    chk = x[0] + x[1] + x[2]
    if(chk == "No."):
        y = f.readline().strip()
        
        #split data and limit whitespace to 1 character for easier parsing
        dataCols = ' '.join(y.split()).split(' ')


        #print(dataCols)
        #print(dataCols[4])



        # Check if Packet is ICMP and an Echo Request/Reply and:
            # ignore Destination Host Unreachable ICMP Packets then:
                # Write out packet information entries separated by
                # '@' line 
        if(dataCols[4] == 'ICMP' and dataCols[6] != "Destination"):
            #print(dataCols)
            w.write("@\n")
            w.write(x + "\n")
            w.write(y + "\n")
            #print(x)
            #print(y)
            f.readline().strip()
            out = f.readline().strip()
            #print("out = " + out)

            # write out lines of packet data
            while out != "":
                #print(out)
                w.write(out + "\n")
                out = f.readline().strip()

            # move to next packet data entry
            x = f.readline().strip()
        # end if

        # Packet being ignored, move to next packet in source file

        else:
            x = f.readline().strip()
            x = f.readline().strip()
           # print(x)
            while(x != ""):
                x = f.readline().strip()
                #print(x)
            x = f.readline().strip()


    
    


# chk = x[0] + x[1] + x[2]
# if(chk == "No."):
#     x = f.readline().strip()
#     dataCols = ' '.join(x.split()).split(' ')
#     print(dataCols[4])