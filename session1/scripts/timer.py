import time
import sys

delay = float(sys.argv[1])


print("before sleep")
print(f"sleeping for {delay} secs")
time.sleep(delay)
print("after sleep")