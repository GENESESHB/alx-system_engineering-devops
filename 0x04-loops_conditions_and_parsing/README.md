# 0x04-loops_conditions_and_parsing



``
a Bash script that displays "Best School" 10 times using a for loop:
``

```bash
#!/usr/bin/env bash

# This script is displaying "Best School" 10 times

# Loop 10 times and display "Best School" on each iteration
for ((i=1; i<=10; i++))
do
    echo "Best School"
done
```

Save the script in a file, for example, "1-for_best_school", and make sure to give it execute permissions using the following command:

```bash
chmod +x 1-for_best_school
```

Then, you can run the script with the command:

```bash
./1-for_best_school
```



#  Bash script that uses a while loop to display "Best School" 10 times:

```bash
#!/usr/bin/env bash

# This script is displaying "Best School" 10 times

# Initialize a counter
count=0

# Use the while loop to display "Best School" until the counter reaches 10
while [ $count -lt 10 ]
do
    echo "Best School"
    # Increment the counter
    ((count++))
done
```

Save the script in a file, for example, "2-while_best_school", and make sure to give it execute permissions using the following command:

```bash
chmod +x 2-while_best_school
```

Then, you can run the script with the command:

```bash
./2-while_best_school
```

# a Bash script that uses the until loop to display "Best School" 10 times:

```bash

#!/usr/bin/env bash

# This script is displaying "Best School" 10 times

# Initialize a counter
count=0

# Use the until loop to display "Best School" until the counter reaches 10
until [ $count -eq 10 ]
do
    echo "Best School"
    # Increment the counter
    ((count++))
done
```

# a Bash script that uses a while loop and an if statement to display "Best School" 10 times but says "Hi" on a new line during the 9th iteration



```bash
#!/usr/bin/env bash

# This script is displaying "Best School" 10 times with "Hi" on the 9th iteration

# Initialize a counter
count=0

# Use the while loop to display "Best School" with "Hi" on the 9th iteration
while [ $count -lt 10 ]
do
    if [ $count -eq 8 ]; then
        echo "Hi"
    else
        echo "Best School"
    fi

    # Increment the counter
    ((count++))
done
```


# a Bash script that uses a while loop and an if statement to display "Best School" 10 times but says "Hi" on a new line during the 9th iteration

```bash
#!/usr/bin/env bash

# This script is displaying "Best School" 10 times with "Hi" on the 9th iteration

# Initialize a counter
count=0

# Use the while loop to display "Best School" with "Hi" on the 9th iteration
while [ $count -lt 10 ]
do
    if [ $count -eq 8 ]; then
        echo "Hi"
    else
        echo "Best School"
    fi

    # Increment the counter
    ((count++))
done
```

Save the script in a file, for example, "4-if_9_say_hi", and make sure to give it execute permissions using the following command:

```bash
chmod +x 4-if_9_say_hi
Then, you can run the script with the command:

bash
Copy code
./4-if_9_say_hi
It will display "Best School" 10 times, but on the 9th iteration, it will print "Hi" on a new line. The if statement checks if the counter is equal to 8 (corresponding to the 9th iteration) and prints "Hi" instead of "Best School".

```


# collaboration the while&if&elif&else

``
in this file we use the logiqal operations for get the output like alx want and this is a code 
``

```bash
#!/usr/bin/env bash
#This script is displaying "Best School" 10 times with "Hi" on the 9th iteration
hb=0
while [ $hb -lt 10 ]
do
    if [ $hb -eq 3 ]
    then
    echo "bad luck"
    elif [ $hb -eq 7 ]
    then
    echo "good luck"
    else
    echo "Best School"
    fi
    hb=$((hb+1))
done
```
