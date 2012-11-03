#-*- coding:utf-8 -*-
#!/bin/bash

ROOT_DIR='/home/rongruo.lsx/report/'

jobName = raw_input("Please input job dir:")
gday = raw_input("Please the day you want to redo, empty reprent all")

if jobName != '':
    job = ROOT_DIR + jobName
    for paths, dirs, files in os.walk(job, topdown=False):
        if gday == '':
            for fi in files:
                if fi.isdigit():
                    
    
