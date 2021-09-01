import platform
import subprocess

def pinger(host):
    cmd = ["ping", "-n", "1", host]
    subprocess.call(cmd)

hostname = input("Enter hostname:")
reps = input("Times to ping: ")
reps = int(reps)
for i in range(reps):
    pinger(hostname)