import filter as filt
import parse
import calc

ips = ["192.168.100.1","192.168.100.2","192.168.200.1","192.168.200.2"]
calcs = []

if __name__ == "__main__":
        filt.filter(4)

        for i in range(1, 5):
            filename = "N" + str(i) + "Filter.txt"
            f = open(filename, "rb")
            L = parse.parsefile(f)
            calcs.append(calc.calculate(L,ips[i-1]))
        
        f = open("output.csv", "wb+")

        for i in range(0, 4):
            f.write("Node " + str(i+1) + "\n\n")
            f.write("Echo Requests Sent, Echo Requests Received, Echo Replies Sent, Echo Replies Received\n")
            f.write(calcs[i][0] + "," + calcs[i][1] + "," + calcs[i][2]+ "," + calcs[i][3] + "\n")
            f.write("Echo Request Bytes Sent (bytes), Echo Request Data Sent (bytes)\n")
            f.write(calcs[i][4] + "," + calcs[i][5] + "\n")
            f.write("Echo Request Bytes Received (bytes), Echo Request Data Received (bytes)\n")
            f.write(calcs[i][6] + "," + calcs[i][7] + "\n\n")
            f.write("Average RTT (milliseconds)," + calcs[i][8] + "\n")
            f.write("Echo Request Throughput (kB/sec)," + calcs[i][9] + "\n")
            f.write("Echo Request GoodPut (kB/sec),"+ calcs[i][10] + "\n")
            f.write("Average Reply Delay (microseconds)," + calcs[i][11] + "\n")
            f.write("Average Echo Request Hop Count," + calcs[i][12] + "\n\n")

            