#!/bin/bash

# set the SSH password
ssh_password="temppwd"

# connect to the remote server and copy the latest CSV file to the local csv/ directory
latest_file=$(sshpass -p "$ssh_password" ssh debian@192.168.8.1 "ls -t /home/debian/ros_catkin_ws/*.csv | head -1")
sshpass -p "$ssh_password" scp "debian@192.168.8.1:$latest_file" ./csv/$latest_file

# run the Python script with the latest CSV file
# python3 main.py "./csv/$(basename $latest_file)"
