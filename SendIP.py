import socket
import os
from datetime import datetime
import telegram_send


def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


if __name__ == "__main__":
    ip = getIP()
    telegram_send.send(messages=["My IP is: " + ip])