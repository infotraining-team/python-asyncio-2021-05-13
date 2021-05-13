import socket as sc
import time

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.connect(("localhost", 25000))

while True:
    sock.send(b'Hello from client')
    resp = sock.recv(100000)
    print(b"got: " + resp)
    time.sleep(1)