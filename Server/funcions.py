import socket


# Establecer conexion
def conexion(host, puerto):
    conexion_host = socket.socket()
    conexion_host.bind((host, puerto))
    conexion_host.listen(15)
    return conexion_host

