import imp
import os
import subprocess
import netifaces as ni

def main():
  completed_process = subprocess.run(["tcpreplay.exe", "--listnics"], shell=True, capture_output=True, cwd="tcpreplay-win")
  raw_nics_output = completed_process.stdout.decode("utf-8")
  tcpreplay_interface = raw_nics_output.split("\n")[2].split("\t")[1]
  print("Interface is: %s" % tcpreplay_interface)

  ni_interface = tcpreplay_interface.lstrip("\\Device\\NPF_")
  ip_address = ni.ifaddresses(ni_interface)[ni.AF_INET][0]["addr"]
  print("IP address is: %s" % ip_address)

  try:
    tcpreplay_cmd = f"tcpreplay.exe -i \"{tcpreplay_interface}\" --mbps=10 -l 0 ..\\1.pcap"
    tcpreplay_proc = subprocess.Popen(tcpreplay_cmd, shell=True, cwd="tcpreplay-win")

    rpcapd_proc = subprocess.Popen(
      ["rpcapd", "-b", "127.0.0.1", "-p", "12321"],
      cwd=os.path.join("PcapPlusPlus", "Tests", "Pcap++Test", "rpcapd"),
      shell=True,
    )
    import time
    time.sleep(3)
    if rpcapd_proc.poll() is not None:
      print("rpcapd is not running!!!")
      exit(1)

    import socket
    s = socket.socket()
    address = "127.0.0.1"
    port = 12321
    s.connect((address, port))
    print("CONNECTED!!!!!!")

    # completed_process = subprocess.run(
    #   os.path.join("Bin", "Packet++Test"),
    #   cwd=os.path.join("PcapPlusPlus", "Tests", "Packet++Test"),
    #   shell=True,
    # )
    # if completed_process.returncode != 0:
    #   exit(completed_process.returncode)

    completed_process = subprocess.run(
      [os.path.join("Bin", "Pcap++Test"), "-i", ip_address, "-t", "TestRemoteCapture"],
      cwd=os.path.join("PcapPlusPlus", "Tests", "Pcap++Test"),
      shell=True,
    )
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

  finally:
    tcpreplay_proc.kill()
    rpcapd_proc.kill()

if __name__ == "__main__":
  main()
