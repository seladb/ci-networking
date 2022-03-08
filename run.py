import sys
import subprocess
import socket
import netifaces as ni

def main():
  
  ni.ifaddresses("en0")
  ip = ni.ifaddresses("en0")[ni.AF_INET][0]["addr"]
  print("IP ADDRESS OF EN0:")
  print(ip)  # should print "192.168.100.37"

  # ip_address= socket.gethostbyname(socket.gethostname())
  # print(ip_address)
  subprocess.run("ifconfig")
  return

  ip_address= socket.gethostbyname(socket.gethostname())
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
