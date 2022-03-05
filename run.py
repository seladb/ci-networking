import subprocess
import socket

ip_address= socket.gethostbyname(socket.gethostname())

tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", "eth0", "--mbps=10", "-l", "0", "1.pcap"])

subprocess.run(["Bin/Packet++Test"], cwd="PcapPlusPlus/Tests/Packet++Test")

subprocess.run(["Bin/Pcap++Test", "-i", ip_address], cwd="PcapPlusPlus/Tests/Pcap++Test")

tcpreplay_proc.kill()
