import socket
import threading
import re
import struct
import os

HOST = "127.0.0.1"

BRANCHES = [
    ("shopsy-chennai", 9001),
    ("shopsy-bangalore", 9002),
    ("shopsy-mumbai", 9003),
]

os.makedirs("partitions", exist_ok=True)

LOG_PATTERN = re.compile(
    r"^(.*?) \| (INFO|WARNING|ERROR|DEBUG) \| ([\w\-]+) \| (.*)$"
)

LEVEL = {"DEBUG": 0, "INFO": 1, "WARNING": 2, "ERROR": 3}


def save_log(ts, level, service, msg):
    file = f"partitions/{service}_{level}.bin"

    data = struct.pack(
        "!19sBH",
        ts.encode().ljust(19, b' ')[:19],
        LEVEL[level],
        len(service)
    )

    data += service.encode()
    data += struct.pack("!H", len(msg))
    data += msg.encode()

    with open(file, "ab") as f:
        f.write(struct.pack("!I", len(data)))
        f.write(data)


def process(line):
    m = LOG_PATTERN.match(line)
    if not m:
        return
    save_log(*m.groups())


def harvest(branch, port):
    s = socket.socket()
    s.connect((HOST, port))
    print(branch, "connected")

    buffer = b""

    while True:
        chunk = s.recv(4096)
        if not chunk:
            break

        buffer += chunk

        while b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)
            try:
                process(line.decode().strip())
            except:
                pass

    s.close()


if __name__ == "__main__":

    for branch, port in BRANCHES:
        threading.Thread(
            target=harvest,
            args=(branch, port),
            daemon=True
        ).start()

    print("Shopsy Log Harvester Running...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopped")