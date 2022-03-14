import os
import subprocess
from time import time, sleep
import netifaces as ni


def find_interface():
  completed_process = subprocess.run(["tcpreplay.exe", "--listnics"], shell=True, capture_output=True, cwd="tcpreplay-win")
  raw_nics_output = completed_process.stdout.decode("utf-8")
  for row in raw_nics_output.split("\n")[2:]:
    columns = row.split("\t")
    if len(columns) > 1 and columns[1].startswith("\\Device\\NPF_"):
      interface = columns[1]
      try:
        ni_interface = interface.lstrip("\\Device\\NPF_")
        ip_address = ni.ifaddresses(ni_interface)[ni.AF_INET][0]["addr"]
        if ip_address.startswith("169.254"):
          continue
        completed_process = subprocess.run(["curl", "--interface", ip_address, "www.google.com"], capture_output=True, shell=True)
        if completed_process.returncode != 0:
          continue
        return interface, ip_address
      except:
        pass
  return None, None


def main():
  tcpreplay_interface, ip_address = find_interface()
  if not tcpreplay_interface or not ip_address:
    print("Cannot find an interface to run tests on!")
    exit(1)
  print(f"Interface is {tcpreplay_interface} and IP address is {ip_address}")

  tcpreplay_cmd = f"tcpreplay.exe -i \"{tcpreplay_interface}\" --mbps=10 -l 0 ..\\1.pcap"
  subprocess.run(tcpreplay_cmd, shell=True, cwd="tcpreplay-win")

if __name__ == "__main__":
  main()
