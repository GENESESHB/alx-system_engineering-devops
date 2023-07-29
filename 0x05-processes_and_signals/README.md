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


# declaration with script

``
declaration with script f i have ran some file in ather terminal
the descript for do this its
``

```bash
#!/usr/bin/env bash
#a Bash script that displays "To infinity and beyond" indefinitely and "I am invincible!!!" in case of SIGINT

on_sigterm()
{
	echo "I am invincible!!!"
}
trap "on_sigterm" SIGTERM

while true
do
	echo "To infinity and beyond"
	sleep 2
done
```

``
if you wanna a killed -stoped- the despliy of string
``

``
tap this command in your terminal
``
``
kill -9 "$(pgrep -f name-of_file)"
``

#  Process and PID file

``
let me tell you ebout my code
this is
``

```bash
function love() {
    rm /var/run/myscript.pid
    exit
}

trap "echo I hate the kill command;love" SIGTERM
trap "echo Y U no love me?!;love" SIGINT

echo $$ >> /var/run/myscript.pid
while [ true ]; do
    echo To infinity and beyond;
done
```

``
in this file i rain hem win i tap ctrl+c will stop with last string -Y U no lave me?!-
and if rain hem if i tap i ather terminal this command -sudo pkill -f 100-process_and_pid_file-
will stop with last string -i hate the kill command-
``

