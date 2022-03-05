import subprocess
import socket

ip_address= socket.gethostbyname(socket.gethostname())

try:
  tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", "eth0", "--mbps=10", "-l", "0", "1.pcap"])

  completed_process = subprocess.run(["Bin/Packet++Test"], cwd="PcapPlusPlus/Tests/Packet++Test")
  if completed_process.returncode != 0:
    exit(completed_process.returncode)

  completed_process = subprocess.run(["Bin/Pcap++Test", "-i", ip_address], cwd="PcapPlusPlus/Tests/Pcap++Test")
  if completed_process.returncode != 0:
    exit(completed_process.returncode)

finally:
  tcpreplay_proc.kill()

