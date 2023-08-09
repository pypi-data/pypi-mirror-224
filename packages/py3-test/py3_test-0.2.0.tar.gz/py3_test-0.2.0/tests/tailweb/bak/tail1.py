import os
import time


def tail(filename, sleep=0.5):
    # Print last 20 lines
    with open(filename) as f:
        lines = f.readlines()
        print("".join(lines[-20:]).strip())

    # Watch the file for changes
    stat = os.stat(filename)
    size = stat.st_size
    mtime = stat.st_mtime
    while True:
        time.sleep(0.5)
        stat = os.stat(filename)
        if mtime < stat.st_mtime:
            mtime = stat.st_mtime
            with open(filename, "rb") as f:
                f.seek(size)
                lines = f.readlines()
                print("".join(lines).strip())
            size = stat.st_size


print(tail("ip.txt"))
