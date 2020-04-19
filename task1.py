import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# address
server = '127.0.0.1'

# ports range, from a to b
a = 3
b = 56


def portScan(port):
    try:
        sock.connect((server, port))
        return True
    except:
        return False


for i in range(a, b + 1):
    if portScan(i):
        print('Port ', i, ' is opened')
    else:
        print('Port ', i, ' is closed')
