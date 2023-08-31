import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 7692))

full_msg = "I am Geethanjali"
while True:
    msg = s.recv(9)
    if len(msg) <= 0:
        break
    else:
        full_msg += msg.decode("utf-8")

print(full_msg)