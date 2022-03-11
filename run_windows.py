import subprocess
import netifaces as ni

def main():
  completed_process = subprocess.run(["tcpreplay.exe", "--listnics"], shell=True, capture_output=True, cwd="tcpreplay-win")
  raw_nics_output = completed_process.stdout.decode("utf-8")
  tcpreplay_interface = raw_nics_output.split("\n")[2].split("\t")[1]
  print("Interface is: %s" % tcpreplay_interface)

  tcpreplay_cmd = f"tcpreplay.exe -i \"{tcpreplay_interface}\" --mbps=10 ..\\1.pcap"
  subprocess.run(tcpreplay_cmd, shell=True, cwd="tcpreplay-win")

  ni_interface = tcpreplay_interface.lstrip("\\Device\\NPF_")
  ip_address = ni.ifaddresses(ni_interface)[ni.AF_INET][0]["addr"]
  print("IP address is: %s" % ip_address)

  # try:
  #   tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", args.interface, "--mbps=10", "-l", "0", "1.pcap"], cwd=args.tcpreplay_dir)

  #   use_sudo = ["sudo"] if args.use_sudo else []
  #   completed_process = subprocess.run(use_sudo + ["Bin/Packet++Test"] + args.test_args.split(), cwd="PcapPlusPlus/Tests/Packet++Test")
  #   if completed_process.returncode != 0:
  #     exit(completed_process.returncode)

  #   completed_process = subprocess.run(use_sudo + ["Bin/Pcap++Test", "-i", ip_address] + args.test_args.split(), cwd="PcapPlusPlus/Tests/Pcap++Test")
  #   if completed_process.returncode != 0:
  #     exit(completed_process.returncode)

  # finally:
  #   tcpreplay_proc.kill()

if __name__ == "__main__":
  main()
