"""
shopsy_log_server_simulator.py
------------------------------
Simulates 3 high-velocity Shopsy regional servers
(Shopsy-Chennai, Shopsy-Bangalore, Shopsy-Mumbai).

Each server continuously sends live shopping log events to the
Log Harvester Daemon over TCP.

Run this file FIRST and leave it running.
"""

import socket
import threading
import random
import time
from datetime import datetime

# Simulated Shopsy regional servers
BRANCHES = [
    ("shopsy-chennai", 9001),
    ("shopsy-bangalore", 9002),
    ("shopsy-mumbai", 9003),
]

LEVELS = ["INFO", "WARNING", "ERROR", "DEBUG"]

# Shopsy log message templates
MESSAGE_TEMPLATES = {
    "INFO": [
        "Order#{oid} placed successfully",
        "Order#{oid} packed successfully",
        "Order#{oid} shipped successfully",
        "Order#{oid} delivered successfully",
        "Seller accepted Order#{oid}",
    ],

    "WARNING": [
        "Order#{oid} delivery delayed",
        "High traffic detected for Order#{oid}",
        "Low inventory for Order#{oid}",
        "Seller response delayed for Order#{oid}",
    ],

    "ERROR": [
        "Payment failed for Order#{oid}",
        "Order#{oid} cancelled by seller",
        "Order#{oid} refund failed",
        "Shipment tracking unavailable for Order#{oid}",
    ],

    "DEBUG": [
        "Database updated for Order#{oid}",
        "Cache refreshed for Order#{oid}",
        "Retrying payment verification for Order#{oid}",
    ],
}


def build_log_line(branch_name):
    """Generate one Shopsy log record."""

    level = random.choice(LEVELS)
    oid = random.randint(1000, 9999)

    message = random.choice(
        MESSAGE_TEMPLATES[level]
    ).format(oid=oid)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"{timestamp} | {level} | {branch_name} | {message}\n"


def handle_client(conn, branch_name):
    """Continuously send log records."""

    print(f"[{branch_name}] Harvester connected. Streaming logs...")

    try:
        while True:

            log_line = build_log_line(branch_name)

            conn.sendall(log_line.encode("utf-8"))

            # Simulate high-speed log generation
            time.sleep(random.uniform(0.05, 0.40))

            # Send an invalid log occasionally
            if random.random() < 0.05:
                conn.sendall(b"INVALID_LOG_DATA\n")

    except (BrokenPipeError, ConnectionResetError):
        print(f"[{branch_name}] Harvester disconnected.")

    finally:
        conn.close()


def run_branch_server(branch_name, port):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("127.0.0.1", port))

    server.listen(1)

    print(f"[{branch_name}] Listening on Port {port}...")

    while True:

        connection, address = server.accept()

        client = threading.Thread(
            target=handle_client,
            args=(connection, branch_name),
            daemon=True
        )

        client.start()


if __name__ == "__main__":

    threads = []

    for branch_name, port in BRANCHES:

        thread = threading.Thread(
            target=run_branch_server,
            args=(branch_name, port),
            daemon=True
        )

        thread.start()

        threads.append(thread)

    print("\n===========================================")
    print(" Shopsy Log Server Simulator Started")
    print(" Regional Servers Running Successfully")
    print(" Press Ctrl+C to Stop")
    print("===========================================\n")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping Shopsy Log Server Simulator...")