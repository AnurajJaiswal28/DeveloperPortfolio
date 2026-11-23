#!/bin/bash

echo "================================"
echo "       SYSTEM INFORMATION"
echo "================================"

echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Date: $(date)"
echo "Operating System: $(. /etc/os-release && echo "$PRETTY_NAME")"
echo "Kernel Version: $(uname -r)"
echo "Architecture: $(uname -m)"

echo
echo "---------- CPU INFORMATION ----------"
lscpu | grep -E 'Model name|CPU\(s\)|Core\(s\) per socket|Thread\(s\) per core'

echo
echo "---------- MEMORY INFORMATION ----------"
free -h

echo
echo "---------- DISK INFORMATION ----------"
df -h /

echo
echo "---------- TOP PROCESSES ----------"
ps aux --sort=-%cpu | head -6

echo
echo "System information report completed."
