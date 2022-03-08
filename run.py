import sys
import subprocess
import socket

def main():
  ip_address= socket.gethostbyname(socket.gethostname())
  print(ip_address)
  subprocess.run("ifconfig")
  return

  try:
    tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", "eth0", "--mbps=10", "-l", "0", "1.pcap"])

    completed_process = subprocess.run(["Bin/Packet++Test"] + sys.argv[1:], cwd="PcapPlusPlus/Tests/Packet++Test")
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

    completed_process = subprocess.run(["Bin/Pcap++Test", "-i", ip_address] + sys.argv[1:], cwd="PcapPlusPlus/Tests/Pcap++Test")
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

  finally:
    tcpreplay_proc.kill()

if __name__ == "__main__":
    main()
