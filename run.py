import subprocess

tcpdump_proc = subprocess.Popen("tcpdump")
subprocess.run(["tcpreplay", "-i", "eth0", "--mbps=10", "1.pcap"])
tcpdump_proc.kill()
outs, errs = tcpdump_proc.communicate()

print("ERRORS:")
print(errs)

print("STDOUT:")
print(outs)
