import time, socket, sys

time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
           
s.listen(1)
client, addr = s.accept()

teamone=[]
teamtwo=[]

for i in range(10):
    
	if(i==0 or i==3 or i==4 or i==7 or i==8):
		buffer= "Player1 enter choice"
		client.send(buffer.encode())
		buffer= client.recv(1024)
		buffer= buffer.decode()
		teamone.append(buffer)
    	
	else:
		buffer= "Player two enter choice"
		client.send(buffer.encode())
		buffer= client.recv(1024)
		buffer= buffer.decode()
		teamtwo.append(buffer)

buffer="End of draft\n"
client.send(buffer.encode())

buffer="TEAM ONE:\n" #sending team one
client.send(buffer.encode())
for i in range(5):
	buffer=teamone[i]
	client.send(buffer.encode())
	buffer="\n"
	client.send(buffer.encode())
	
buffer="TEAM TWO:\n" #sending team two
client.send(buffer.encode()) 

for i in range(5):
	buffer=(teamtwo[i])
	client.send(buffer.encode())
	buffer="\n"
	client.send(buffer.encode())
	
buffer="Thanks for playing!\n"
client.send(buffer.encode())
buffer="Your results will be conveyed shortly!"
client.send(buffer.encode())
