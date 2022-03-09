import socket
import subprocess

ip_address= socket.gethostbyname(socket.gethostname())
print(ip_address)

subprocess.run("ifconfig")
