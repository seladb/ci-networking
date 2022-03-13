import os
import subprocess
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
        mac_address = ni.ifaddresses(ni_interface)[-1000][0]["addr"]
        if not mac_address:
          continue
        ip_address = ni.ifaddresses(ni_interface)[ni.AF_INET][0]["addr"]
        if ip_address.startswith("169.254"):
          continue
        return interface, ip_address
      except:
        pass
  return None, None


def main():
  tcpreplay_interface, ip_address = find_interface()
  print(f"Interface is {tcpreplay_interface} and IP address is {ip_address}")

  try:
    tcpreplay_cmd = f"tcpreplay.exe -i \"{tcpreplay_interface}\" --mbps=10 -l 0 ..\\1.pcap"
    tcpreplay_proc = subprocess.Popen(tcpreplay_cmd, shell=True, cwd="tcpreplay-win")

    completed_process = subprocess.run(
      os.path.join("Bin", "Packet++Test"),
      cwd=os.path.join("PcapPlusPlus", "Tests", "Packet++Test"),
      shell=True,
    )
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

    completed_process = subprocess.run(
      [os.path.join("Bin", "Pcap++Test"), "-i", ip_address, "-x", "TestRemoteCapture"],
      cwd=os.path.join("PcapPlusPlus", "Tests", "Pcap++Test"),
      shell=True,
    )
    if completed_process.returncode != 0:
      exit(completed_process.returncode)

  finally:
    tcpreplay_proc.kill()

if __name__ == "__main__":
  main()
