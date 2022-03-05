import subprocess
import time

tcpreplay_proc = subprocess.Popen(["tcpreplay", "-i", "eth0", "--mbps=10", "1.pcap"])
tcpdump_proc = subprocess.Popen("tcpdump")

time.sleep(10)

tcpdump_proc.kill()
tcpreplay_proc.kill()
