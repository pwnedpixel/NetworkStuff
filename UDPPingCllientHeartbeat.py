from socket import *
import time
from time import gmtime, strftime
import datetime

serverName = '127.0.0.1'
serverPort = 12000

totalTime = 0
successCnt = 0
min = 1
max = 0

for index in range(0, 10):
    # create socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # set the soket timeout
    clientSocket.settimeout((1))
    # takes a reading of the time before sending the UDP message
    timebefore = time.time()
    currentTime = strftime("%Y-%m-%d %H:%M:%S")
    # sends UDP message with current time and date as a message
    clientSocket.sendto(currentTime.encode(), (serverName, serverPort))

    # Tries to wait and receive a reply back. will throw exception if the
    #   1 second timeout period is reached.
    try:
        message, server = clientSocket.recvfrom((1024))
        # reads time after receiving reply
        timeafter = time.time()
        # calculates RTT time
        totalTime += (timeafter - timebefore)

        # determine if min or max
        if totalTime < min:
            min = totalTime
        if totalTime > max:
            max = totalTime

        successCnt += 1
        print("PING:" + " " + str(index) + " " + currentTime)
    except timeout:
        print("*** Request Timed Out ***")
    # was sometimes getting times of zero without a delay between runs.
    time.sleep(0.1)

print("RTT: Min:" + str(round(min * 1000, 2)) + "ms  Avg:" + str(
    round(1000 * totalTime / successCnt, 2)) + "ms  Max:" + str(round(max * 1000, 2)) + "ms  Packet Loss:" +
      str(10 - successCnt) + "0.00%")
