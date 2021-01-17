import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bin((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conexion establecida desde {address}")
	clientsocket.send(bytes("Hola, bienvenido al server", 'utf-8'))
	clientsocket.close()