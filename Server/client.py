import socket
from funcions import *

local_host = socket.socket()
local_host.connect(('20.109.17.17', 8080))


respuesta = local_host.recv(1024)
mensaje = input(">>> ")
local_host.send(mensaje.encode())
print(respuesta)
