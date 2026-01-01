import subprocess
import os

# CONFIG
NETWORK_RANGE = "192.168.100.0/24"
SERVER_USER = "jim"
SERVER_IP = "192.168.100.241"

def scan():
    print("Scanning network...")
    # -sn is a 'Ping Scan' - fast and effective for finding active devices
    cmd = f"nmap -sn {NETWORK_RANGE}"
    result = subprocess.check_output(cmd, shell=True).decode()
    
    # Extract IPs from nmap output
    found_ips = []
    for line in result.splitlines():
        if "Nmap scan report for" in line:
            ip = line.split()[-1].strip("()")
            found_ips.append(ip)
    
    return found_ips

def send_to_server(ips):
    # This sends the found IPs to the server script via SSH
    ip_string = " ".join(ips)
    ssh_cmd = f'ssh jim@192.168.100.241 "python3 /home/jim/net-watch/notify_server.py {ip_string}"'
    os.system(ssh_cmd)

if __name__ == "__main__":
    active_ips = scan()
    send_to_server(active_ips)
    print(f"Scan complete. Sent {len(active_ips)} IPs to server.")