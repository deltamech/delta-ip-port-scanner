#%%
"""
DeltaMech Port Checker
to launch:
python3 /../deltaPortcheck.py
"""
import socket
import time
# easier than error handling
ip = ['0'] # don't set this here run the program
port = 0   # don't set this here run the program
retry = 1  # tune to your liking 
delay = 2  # tune to your liking 
timeout = 3  # tune to your liking 

def isOpen(ip, port):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.settimeout(timeout)
        try:
                mySocket.connect((ip, int(port)))
                mySocket.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                mySocket.close()

def checkIp(ip, port):
        ipup = False
        for retries in range(retry):
                if isOpen(ip, port):
                        ipup = True
                        break
                else:
                        time.sleep(delay)
        return ipup

if __name__ == '__main__':
        ip = input('Enter IP address without port: ')
        p = input('Enter Ports to check, comma separated: ')

        list = p.split (",")
        ports = []

        for i in list:
	        ports.append(int(i))
        for j in range(len(ports)):
                port = ports[j-1]
                if checkIp(ip, port):
                        print(ip + ':' + str(port) + ' is up')
                else:
                        print(ip + ':' + str(port) + ' is down')

# %%
