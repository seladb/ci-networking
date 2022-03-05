import subprocess
# import time
import socket

ip_address= socket.gethostbyname(socket.gethostname())

tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", "eth0", "--mbps=10", "-l", "0", "1.pcap"])
# tcpdump_proc = subprocess.Popen("tcpdump")

subprocess.run(["Bin/Pcap++Test", "-i", ip_address], cwd="PcapPlusPlus/Tests/Pcap++Test")

# time.sleep(10)

# tcpdump_proc.kill()
tcpreplay_proc.kill()
