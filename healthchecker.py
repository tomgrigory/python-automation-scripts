import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(0.1)
    return usage > 75

if not check_disk_usage("/") or check_cpu_usage():
    print("Youre Computer is in Danger.")
else:
    print("Everything is Awesome!!!!!")
 
