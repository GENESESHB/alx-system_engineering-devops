![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

# 0x0C-web_server

# RESOURCES 👨‍💻

# TASKS 💻

! Here's an explanation of each line in the Bash script:

```bash
#!/usr/bin/env bash
```
- This line is called a shebang. It tells the system that the script should be executed using the Bash shell, which is typically located at `/usr/bin/env bash`. It's the interpreter directive for the script.

```bash
# Transfers a file from Holberton's client to another.
# Accepts four arguments:
#+    The path to the file to be transferred.
#+    The IP of the server to transfer the file to.
#+    The username that scp connects with.
#+    The path to the SSH private key that scp uses.
```
- These lines are comments that provide an explanation of what the script does and the arguments it accepts. Comments in Bash start with `#` and are ignored by the shell but help humans understand the code.

```bash
if [ $# -lt 4 ]
then
  echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
```
- This block of code starts an `if` statement. It checks the number of command-line arguments passed to the script using `$#`. If the number of arguments is less than 4, it means not enough arguments were provided.

```bash
  echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
```
- If there are not enough arguments, this line prints a usage message to the standard output, informing the user of the correct way to use the script.

```bash
else
```
- If there are at least 4 arguments, the script continues to this `else` block.

```bash
  scp -o StrictHostKeyChecking=no -i "$4" "$1" "$3@$2":~
```
- This line is the core of the script. It uses the `scp` command to securely copy a file from the local machine (specified by `$1`) to a remote server (specified by `$2`) using the username `$3` and the SSH private key located at the path `$4`. The `StrictHostKeyChecking=no` option disables strict host key checking for SCP to avoid interactive prompts.

- `" $3@$2":~` specifies the destination path on the remote server. It uses the provided username (`$3`) and IP address (`$2`) to specify the destination directory as the home directory (`~`) of the remote user.

This script essentially checks if it has been provided with the correct number of command-line arguments. If not, it provides usage instructions. If the correct number of arguments is given, it uses SCP to transfer a file to the specified remote server using the provided username and SSH key.

# 	1

This Bash script is designed to configure a new Ubuntu machine by installing the Nginx web server, ensuring it listens on port 80, and serving a web page that returns the "Hello World!" string. Let's break down the script step by step:

1. **Shebang and Comments:**
   ```bash
   #!/usr/bin/env bash
   # Configures a new ubuntu machine by installing
   # Nginx where it should be listening on port 80
   # Serve a page that would return a Hello World string
   ```
   - The script starts with a shebang line (`#!/usr/bin/env bash`) that specifies the interpreter to be used (Bash).
   - Comments are used to provide a brief description of the script's purpose.

2. **Updating and Installing Nginx:**
   ```bash
   echo -e "Updating and installing Nginx.\n"
   sudo apt-get update -y -qq && \
       sudo apt-get install nginx -y
   ```
   - This section updates the package list (`apt-get update`) and installs Nginx (`apt-get install nginx`) with the `-y` flag to automatically confirm installation prompts.
   - `-qq` is used for quiet output.
   - `&&` is used to execute the second command if the first one succeeds.

3. **Setting up Some Minor Stuff:**
   ```bash
   echo -e "\nSetting up some minor stuff.\n"
   ```
   - This section includes miscellaneous setup tasks.

4. **Starting Nginx Service:**
   ```bash
   sudo service nginx start
   ```
   - This command starts the Nginx service.

5. **Allowing Nginx on Firewall:**
   ```bash
   sudo ufw allow 'Nginx HTTP'
   ```
   - This allows HTTP traffic (port 80) through the Ubuntu firewall (`ufw`) for Nginx.

6. **Setting Ownership and Permissions:**
   ```bash
   sudo chown -R "$USER":"$USER" /var/www/html
   sudo chmod -R 755 /var/www
   ```
   - These commands set the ownership and permissions for the `/var/www/html` directory to allow the current user (`$USER`) to edit the website files.

7. **Backup Default Index and Create New Index:**
   ```bash
   cp /var/www/html/index.nginx-debian.html /var/www/html/index.nginx-debian.html.bckp
   echo -e "Hello World!" | dd status=none of=/var/www/html/index.nginx-debian.html
   ```
   - The script creates a backup of the default Nginx index file.
   - It then uses `dd` to create a new index file with the content "Hello World!".

8. **Restarting Nginx:**
   ```bash
   sudo service nginx restart
   ```
   - This command restarts the Nginx service to apply the configuration changes.

9. **Completion Message:**
   ```bash
   echo -e "\nCompleted. ✅\n"
   ```
   - This line prints a completion message with a checkmark emoji.

When you run this script on a new Ubuntu machine, it automates the installation and configuration of Nginx to serve a "Hello World!" page on port 80.
