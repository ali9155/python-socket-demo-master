import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 20000))

client.send("I am CLIENT\n")

from_server = client.recv(4096)

client.close()

print (from_server)
