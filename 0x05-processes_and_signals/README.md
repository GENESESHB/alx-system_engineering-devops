# 0x05-processes_and_signals

# What is my PID
``
for git your PID
``

```bash
echo $$
```

# List your processes

``
#this script display list of currently running processes
#must show all processes, for all users,
#display a user-oriented format
#show process hiererchy
``

```bash
ps -a -x -u -f
```

# Show your Bash PID

``
#this script extends previous exercise commad and displays line containing the bash word, this allowing you to get the PID of my bash process
#you cannot use pgrep
``

```bash
./1-list_your_processes | grep "bash"
```

# mode easy

``
if you wanna show your processes PID you can tap this commande
but it s not get the discription
``

```bash
pgrep -l bash
```

# display script

```bash
#!/usr/bin/env bash
#this script displays a statement indefinitly
while true; do
    echo "To infinity and beyond"
    sleep 2
done
```
# command for stop last display script


```bash
kill "$(pgrep -f 4-to_infinity_and_beyond)"
```

``
or
``

```bash
pkill -f 4-to_infinity_and_beyond
```

