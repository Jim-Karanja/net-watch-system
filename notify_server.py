import sys
import requests

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1456213980308832297/viB8jOhZQsVNm5wvKn993X4KPwR6J48uN3Zjy5M51wC3oaDUZoP-8MnGFk9hTwssqXTy"
FRIENDLY_FILE = "/home/jim/net-watch/friendly_devices.txt"

def check_for_intruders(found_ips):
    with open(FRIENDLY_FILE, 'r') as f:
        friendly_ips = [line.strip() for line in f.readlines()]

    intruders = [ip for ip in found_ips if ip not in friendly_ips]

    for intruder in intruders:
        msg = f"⚠️ **UNKNOWN DEVICE DETECTED:** `{intruder}`"
        requests.post(DISCORD_WEBHOOK, json={"content": msg})
        print(f"Alerted Discord about: {intruder}")

if __name__ == "__main__":
    # This reads IPs sent from the laptop over SSH
    ips = sys.argv[1:]
    if ips:
        check_for_intruders(ips)
