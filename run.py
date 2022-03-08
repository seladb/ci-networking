from ast import arg
import sys
import subprocess
import socket
import netifaces as ni

def main():
  iface = sys.argv[1]
  ip_address = ni.ifaddresses(iface)[ni.AF_INET][0]["addr"]
  print("IP address is: %s" % ip_address)

  # ip_address= socket.gethostbyname(socket.gethostname())
  try:
    tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", iface, "--mbps=10", "-l", "0", "1.pcap"])

    completed_process = subprocess.run(["sudo", "Bin/Packet++Test"] + sys.argv[1:], cwd="PcapPlusPlus/Tests/Packet++Test")
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

    completed_process = subprocess.run(["sudo", "Bin/Pcap++Test", "-i", ip_address] + sys.argv[2:], cwd="PcapPlusPlus/Tests/Pcap++Test")
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

  finally:
    tcpreplay_proc.kill()

if __name__ == "__main__":
    main()
