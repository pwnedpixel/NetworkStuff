
from socket import *
import sys

# Create a server socket, bind it to a port and start listening
# fill in start
#fill in ends

while 1:
    # Start receiving data from the client
    print( 'Ready to serve...')
    tcpCliSock, addr = tcpSerSocket.accept()
    print ('Received a connection from:', addr)
    message = tcpCliSock.recv(2048)
    if str( message, encoding='utf8' ) != '':
        print (message)

    # Extract the filename from the given message
        print (message.split()[1])
        file1 = str( message, encoding='utf8' )
        filename = file1.split()[1].split("/")[1]
        print (filename)
        fileExist = "false"
        filetouse = "/" + filename
        print (filetouse)
        try:
        # Check whether the file exist in the cache
            f = open(filetouse[1:], "rb")
            outputdata = f.readlines()
            fileExist = "true"

        # ProxyServer finds a cache hit and generates a response message
        
            tcpCliSock.send(bytes("HTTP/1.0 200 OK\r\n",'utf-8'))
            tcpCliSock.send(bytes("Content-Type:text/html\r\n",'utf-8'))
        # Fill in start.

        # Fill in end.
            f.close()
            print ('Read from cache')

    # Error handling for file not found in cache
        except IOError:
            if fileExist == "false":
            # Create a socket on the proxy server
                c = socket(AF_INET, SOCK_STREAM)
                hostn = filename.replace("www.", "", 1)
                print (hostn)
                try:
                # Connect to the socket to port 80
                
                # fill in start
                
                #fill in ends
            
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                    fileobj = c.makefile('rwb')
                    string1 = "GET " + "http://" + filename + " HTTP/1.0\n\n"
                    naming = bytes(string1,'utf-8')
                    c.send(naming)
                    fileobj.write(naming)
               
                # Read the response into buffer
                
                # fill in start
                
                #fill in ends
                
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                    tmpFile = open("./" + filename,"wb")
                    
                # Fill in start.

                # Fill in end.
                
                    tmpFile.close()
                except:
                        print ("Illegal request")
                else:
            # HTTP response message for file not found
                
                # Fill in start.

                # Fill in end.

    # Close the client and the server sockets
    tcpCliSock.close()
    
# Fill in start.

# Fill in end.
    
