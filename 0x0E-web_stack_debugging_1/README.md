#            0x0E-web_stack_debugging_1
![covre](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg)


#RESSOURCES 🚀
[Network basics](https://intranet.alxswe.com/concepts/33)
[Web stack debugging](https://intranet.alxswe.com/concepts/68)

# TASKS 🧠

# 0️⃣


1. **`#!/usr/bin/env bash`** :
   Cette ligne est appelée **shebang**. Elle indique le chemin de l'interpréteur de commandes à utiliser pour exécuter le script. Dans ce cas, elle indique que le script doit être exécuté avec Bash.

2. **`rm /etc/nginx/sites-enabled/default`** :
   Cette commande `rm` est utilisée pour supprimer des fichiers ou des liens symboliques. Dans ce cas, elle supprime le lien symbolique `/etc/nginx/sites-enabled/default`. Dans les configurations Nginx d'Ubuntu, le fichier `default` est un lien symbolique pointant vers le fichier de configuration du site par défaut. Cette ligne supprime ce lien symbolique.

3. **`ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default`** :
   Cette commande `ln -s` crée un nouveau lien symbolique. Elle crée un lien symbolique nommé `default` dans le répertoire `sites-enabled`, pointant vers le fichier de configuration `default` dans le répertoire `sites-available`. Cela configure Nginx pour utiliser le fichier de configuration par défaut.

4. **`service nginx restart`** :
   Cette commande redémarre le service Nginx. Après avoir supprimé le lien symbolique par défaut et créé un nouveau lien symbolique pointant vers un fichier de configuration valide, redémarrer le service Nginx applique les nouvelles configurations.

En résumé, ce script est utilisé pour configurer un serveur Nginx pour écouter sur le port 80 en supprimant le lien symbolique par défaut (qui pointe probablement vers une configuration incorrecte ou inexistante) et en créant un nouveau lien symbolique pointant vers le fichier de configuration correct. Ensuite, le service Nginx est redémarré pour appliquer les modifications de configuration

# 1️⃣

1. **`#!/usr/bin/env bash`**:
   This is the **shebang** line. It tells the system that this script should be interpreted and executed by the Bash shell, located at `/usr/bin/env bash`.

2. **`# Configures an Nginx server to listen on port 80.`**:
   This is a comment. Comments in Bash scripts start with the `#` symbol and are ignored by the shell. Comments are used for providing explanations and context to human readers of the script.

3. **`ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default`**:
   This line creates a symbolic link (`ln -s`) named `default` in the `/etc/nginx/sites-enabled/` directory, pointing to the configuration file located at `/etc/nginx/sites-available/default`. In Nginx, the `sites-available` directory typically contains available site configurations, and the `sites-enabled` directory contains enabled site configurations. By creating a symbolic link, you enable a particular site configuration without duplicating the configuration file.

   - `-s` flag: creates a symbolic link.
   - `-f` flag: removes existing destination files if they exist and are not symbolic links.

4. **`service nginx start`**:
   This line starts the Nginx service on the system. The `service` command is used to control services in Unix-based systems. In this case, it starts the Nginx service.

5. **`kill "$(pgrep 'nginx' | head -1)"`**:
   This line finds the process ID (PID) of the first `nginx` process (`pgrep 'nginx' | head -1`) and sends a SIGTERM signal to that process, effectively stopping the Nginx service. 

   - `pgrep 'nginx'`: finds the PID of the `nginx` process.
   - `head -1`: selects the first PID returned by `pgrep`.
   - `kill`: sends a signal to a process. By default, `kill` sends a SIGTERM signal, which is a request for termination. The specified PID is terminated, and the Nginx process stops.

This script essentially creates a symbolic link for the Nginx configuration, starts the Nginx service, and then stops the Nginx service immediately after it starts. Please note that this script might not be very practical in a real-world scenario since it starts and stops Nginx immediately without allowing it to serve any requests.
