import socket
import sys

user = 'Cactus'
password = 'carnot'
    
def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    lines = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            lines.append(rline)
            rline = sfile.readline()
    finally:
        sock.close()
    return lines

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\nSUBSCRIBE\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    finally:
        sock.close()

def pull_stocks():
    # Ticker, Net Worth, Div. Ratio, Volatility
    secs = run(user,password,'SECURITIES')[0].split()[1:]
    secs = [secs[i:i+4] for i in range(0,len(secs),4)]
    secs = map(lambda x: (x[0], float(x[1]), float(x[2]), float(x[3])), secs)
    print secs
