import socket
from funcions import *
try:
    azure_host = conexion('localhost', 8000)
except:
    azure_host = conexion('localhost', 8080)

while True:
    conexion, addr = azure_host.accept()
    print(f"Conexion establecida con: {addr}")

    conexion.send("Hola te saludo desde el server!".encode())
    respuesta = conexion.recv(1024)
    print(respuesta)
    conexion.close()

