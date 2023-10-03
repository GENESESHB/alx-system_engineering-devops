#                               0x0F-load_balancer

![photo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)

# RESOURCES


# TASKS 
Certainly! Let me break down the provided Bash script for you step by step:

```bash
#!/bin/bash
```

This line is called a shebang. It tells the system that this script should be interpreted and executed by the Bash shell.

```bash
sudo apt-get update
sudo apt-get -y install nginx
```

These lines update the package repositories and then install Nginx, a popular web server software, on the Ubuntu machine. `sudo` is used to execute the commands with superuser privileges.

```bash
hostname=$(hostname)
```

This line captures the hostname of the server and assigns it to the variable `hostname`.

```bash
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    add_header X-Served-By $hostname;

    location / {
        # Your existing Nginx configuration here
        # ...
    }
}" | sudo tee /etc/nginx/sites-available/default
```

This part of the script creates an Nginx server configuration. It uses the `echo` command to print the configuration block and pipes (`|`) it into the `tee` command with `sudo` privileges. `tee` is used to write the standard input to a file (in this case, `/etc/nginx/sites-available/default`). The Nginx configuration specifies that the server should listen on port 80, and it adds a custom HTTP header `X-Served-By` with the value of the server's hostname. The `location / { ... }` block is a placeholder where you can add your existing Nginx configuration.

```bash
sudo systemctl restart nginx
```

This line restarts the Nginx service to apply the changes made to the configuration file. `systemctl` is a command used to examine and control the state of the system's services.

In summary, this script automates the installation of Nginx, configures a custom HTTP header in the Nginx server block, and restarts the Nginx service to apply the changes. The custom header allows tracking of which web server is handling HTTP requests, which is useful in load balancing scenarios.

# 1️⃣
Certainly! Let me break down the Bash script step by step to explain what each part does:

```bash
#!/bin/bash
```

This line is called a shebang. It tells the system that this file should be interpreted and executed by the Bash shell.

```bash
sudo apt-get update
sudo apt-get install -y haproxy
```

These lines update the package lists and install HAproxy on the Ubuntu system. `sudo` is used to execute commands with superuser privileges.

```bash
sudo tee /etc/haproxy/haproxy.cfg > /dev/null <<EOL
frontend web
    bind *:80
    mode http
    default_backend web_servers

backend web_servers
    mode http
    balance roundrobin
    server web-01 [STUDENT_ID]-web-01:80 check
    server web-02 [STUDENT_ID]-web-02:80 check
EOL
```

These lines create a configuration file for HAproxy at `/etc/haproxy/haproxy.cfg`. The configuration sets up HAproxy to listen on port 80 (`*:80`) and forwards requests to two backend servers, `web-01` and `web-02`, using the round-robin load balancing algorithm. Replace `[STUDENT_ID]` with your actual student ID.

```bash
sudo sed -i 's/ENABLED=0/ENABLED=1/' /etc/default/haproxy
```

This line modifies the HAproxy init script configuration to ensure that HAproxy
# by
  [ **hassan boudraa**](https://github.com/GENESESHB)
