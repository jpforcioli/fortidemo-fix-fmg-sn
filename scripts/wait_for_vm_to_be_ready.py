# coding: utf-8
"""
This program will check for the status of specific FortiPoC VM.
It will exit when all status will be "Running"
"""

import requests
import logging
import time
import sys
import json

# Set prg_begin_time
prg_begin_time = time.time()

# Disable SSL warnings
from requests.packages import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# FortiPoC
ip = "35.246.144.3"
login = "admin"
password = "fabricadmin"
port = 443
url_prefix = f"https://{ip}:{port}/api"
pause = 5

# List of VMs to check
vms = [
    "FAZ",
    "FMG",
    "HUB1",
    "HUB2",
    "Spoke1",
    "Spoke2",
]

# Configure logging
logfile = f'{time.strftime("%Y%m%d-%H%M%S")}.log'
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(
    filename=logfile, encoding="utf-8", level=logging.INFO, format=format
)
logger = logging.getLogger(sys.argv[0])

# Create the Session
s = requests.Session()
s.verify = False

# Login to FortiPoC
url = f"{url_prefix}/v0/login"
body = {
    "username": login,
    "password": password,
}
logger.info("Login to FortiPoC")
r = s.post(url, json=body)
r.raise_for_status()

# Update session with FortiPoC header
rj = r.json()
csrf_token_http_header = rj.get("csrf-token-http-header")
csrf_token = rj.get("csrf-token")
new_header = '{"' + csrf_token_http_header + '": "' + csrf_token + '"}'
logger.info(f"Insert {new_header} in HTTPS session header")
s.headers.update(json.loads(new_header))

# Wait till all devices aren't running
devices = ",".join(vms)
url = f"{url_prefix}/v0.2/poc/current/devices/list?filter={devices}"
l_vms = len(vms)
not_all_running = True

while not_all_running:
    logger.info(f"Retrieve FortiPoC status for devices {devices}")
    r = s.get(url)
    r.raise_for_status()
    fpoc_devices = r.json()["devices"]
    i = 0
    for pk in fpoc_devices:
        logging.info(json.dumps(fpoc_devices[pk]))
        name = fpoc_devices[pk].get("name")
        state = fpoc_devices[pk].get("state")
        logger.info(f"Device {name}, Status: {state}")
        if state == "Running":
            i = i + 1
    if i == l_vms:
        not_all_running = False
        logger.info(f"All VMs are running!")
    else:
        # Pausing
        logger.info(f"Pause for {pause} seconds")
        time.sleep(pause)

# Logout
url = f"{url_prefix}/v0/logout"
s.get(url)
logger.info("Logout from FortiPoC")

# Set prg_end_time
prg_end_time = time.time()

# Calculate program duration
duration = prg_end_time - prg_begin_time
logger.info(f"Program ran for {duration} seconds")