#-*- coding:utf-8 -*-
import os
import re
import time
import sys
import subprocess

lifeline = re.compile(r"(\d)ms")
report = ("No response", "Partial Response", "Alive")

print time.ctime()

for host in range(1, 100):
    ip = "10.13.32." + str(host)
    pingaling = subprocess.Popen(["ping", ip],shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print "Testing ", ip ,
    while 1:
        pingaling.stdout.flush()
        line = pingaling.stdout.readline()
        if not line:
            break
        igot = re.findall(lifeline, line)
        #print igot
        if igot:
            #print report[int(igot[0])]
            print ip
            break
    print "\n"
print time.ctime()
