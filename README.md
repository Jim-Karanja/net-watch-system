# Net-Watch System 🛡️

A lightweight network intrusion detection system that scans a local network and sends Discord alerts when unknown devices are detected.

## How it Works
1. **Client Side (Laptop):** A Python script uses `nmap` to scan the local network. It then uses **SSH** to securely pass the list of active IPs to the server.
2. **Server Side (Ubuntu):** A Python script receives the IPs, compares them against a `friendly_devices.txt` list, and triggers a **Discord Webhook** if an intruder is found.

## Project Structure
- `scan_network.py`: The client-side scanner (Windows/Linux).
- `notify_server.py`: The server-side logic (Ubuntu).

## Setup
1. Clone the repo.
2. Setup SSH keys between the client and server for passwordless execution.
3. Configure your Discord Webhook URL in `notify_server.py`.
4. Add your trusted device IPs to `friendly_devices.txt`.

## Prerequisites
- Python 3.x
- Nmap (installed on the client)
- SSH Server (OpenSSH on Ubuntu)
