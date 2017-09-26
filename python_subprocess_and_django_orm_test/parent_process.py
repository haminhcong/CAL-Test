import subprocess
import time

print "Start execute sub process"
subprocess.Popen(["../venv/bin/python", "child_process.py"])
print "Continue process main process"

while True:
    print "Execute main process code"
    time.sleep(1)
