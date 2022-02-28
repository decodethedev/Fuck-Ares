import signal

def handler(signum, frame):
    exit(0)

signal.signal(signal.SIGINT, handler)