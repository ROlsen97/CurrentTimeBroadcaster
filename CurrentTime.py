import time
from socket import *
from datetime import datetime

servername = '255.255.255.255'
BROADCAST_TO_PORT = 7000
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    data = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    #s.sendto(data.encode('utf-8'), ('<broadcast>', BROADCAST_TO_PORT))
    s.sendto(data.encode(), (servername, BROADCAST_TO_PORT))
    print(data)
    time.sleep(5)
#"2023-05-02T10:36:09.917Z"