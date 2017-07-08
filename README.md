# RaspberryPi-gettingStarted
A curated list of Raspberry Pi tools, projects, images and resources

<p align="center">
  <img src="https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/raspberry_pi.png"/>
</p>

### Gpio pinout
There are two ways of numbering the IO pins on a Raspberry Pi within RPi.GPIO. The first is using the BOARD numbering system. This refers to the pin numbers on the P1 header of the Raspberry Pi board. The advantage of using this numbering system is that your hardware will always work, regardless of the board revision of the RPi. You will not need to rewire your connector or change your code.

The second numbering system is the BCM numbers. This is a lower level way of working - it refers to the channel numbers on the Broadcom SOC. You have to always work with a diagram of which channel number goes to which pin on the RPi board. Your script could break between revisions of Raspberry Pi boards.

[raspberry-pi 3 schema](https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/pi3_gpio.png)

### Resources
* [Configure and connect using SSH](#configure-and-connect-using-ssh)
* [Autorun python script on boot using systemd](#autorun-python-script-on-boot-using-systemd)
* [Setup NGINX web server](#setup-nginx-web-server)
* [Remote desktop](#remote-desktop)
* [Https with CertBot](#https-with-certbot)
* [Tensorflow on raspberry](https://github.com/samjabrahams/tensorflow-on-raspberry-pi)

### Tutorials
*In these tutorials I'm using [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) library for python*
* [Led](https://github.com/TommyR22/RaspberryPi-gettingStarted/tree/master/tutorials/LED) - turn on with button or using PWM.
* [Temperature & Humidity sensor DHT11](https://github.com/TommyR22/RaspberryPi-gettingStarted/tree/master/tutorials/Temperature_Sensor_DHT11)
* [Control GPIO using Telegram]()

### Community
* [Stackexchange](https://raspberrypi.stackexchange.com/)
* [MagPi](https://www.raspberrypi.org/magpi/)

---

#### Configure and connect using SSH
##### Enable ssh
1. Enter `sudo raspi-config` in a terminal window.
2. Select `Interfacing Options`.
3. Navigate to and select `SSH`.
4. Choose `Yes`.
5. Select `Ok`.
6. Choose `Finish`.

##### Create SSH private/public key
1. `ssh-keygen -t rsa -C "your_email@youremail.com"` and follow instructions. This will generate two new keys public and private. Never post the contens of private key anywhere, this could lead to a huge security hole in your machine.
2. add key: `ssh-add -K <path_to_private_key>`. (ex: ~/.ssh/name_to_private_key)
3. on raspberry: `mkdir -p ~/.ssh`.
4. insert public key on raspberry: `cat ~/.ssh/id_rsa.pub<path_to_public_key> | ssh user_raspberry@<ip_raspberry> "mkdir -p ~/.ssh && cat >>  ~/.ssh/authorized_keys"`.
5. disable password login ssh to avoid brute force access, edit file: `sudo nano /etc/ssh/sshd_config`.
Edit this lines:
```
ChallengeResponseAuthentication no
PasswordAuthentication no (uncomment line)
UsePAM no
```
6. restart ssh service: `sudo /etc/init.d/ssh restart`.
7. *OPTIONAL*: consider to change ssh port for more security in `/etc/ssh/sshd_config` file.

##### Connection via ssh
`ssh user_raspberry@ip_raspberry -p <port_number>`.

##### Ssh tips
* **Coping file from PC-to-Raspberry**: `scp /path/to/local/file remote_user@remote_host:/path/to/remote/file` (ex:scp project.py pi@192.168.0.200:projects/).
* **Coping file from Raspberry-to-Pc**: `scp remote_user@remote_host:/path/to/remote/file /path/to/local/file`.

---

#### Autorun python script on boot using systemd
1. create config file service (**unit file**): `sudo nano /lib/systemd/system/name_of_service.service`.
2. add following text: 
 ```
[Unit]
Description=My Script Service
After=multi-user.target
# The units listed in this directive will be started before starting the current unit.
# multi-user is like runlevel 3, non graphical multi user mode with network.
#Documentation=https://link_to_documentation.com

[Service]
Type=idle
# idle = This indicates that the service will not be run until all jobs are dispatched
ExecStart=/usr/bin/python /home/pi/name_of_script.py
# this specifies the full path and the arguments of the command to be executed to start the process
Restart=on-abort
# This indicates the circumstances under which systemd will attempt to automatically restart the service.

[Install]
WantedBy=multi-user.target
# states the target or targets that the service should be started under. 
# systemctl list-units --type target (to list all currently loaded target units)
```
[official documentation unit file](https://www.freedesktop.org/software/systemd/man/systemd.unit.html) 

3. *OPTIONAL*: change the ExecStart with `ExecStart=/usr/bin/python /home/pi/name_of_script.py > /home/pi/name_of_script.log 2>&1` if you want to store output text in a log file.
4. add permission to file: `sudo chmod 644 /lib/systemd/system/name_of_service.service`
5. enable service and reboot raspberry: 
```
sudo systemctl daemon-reload
sudo systemctl enable name_of_service.service
sudo reboot
```
* check status of service: `sudo systemctl status name_of_service.service`
* start service: `sudo systemctl start name_of_service.service`
* stop service: `sudo systemctl stop name_of_service.service`
* log systemd service: `sudo journalctl -f -u name_of_service.service`

---

#### Setup NGINX web server
[NGINX official site](https://www.nginx.com/resources/wiki/)
1. install web server : `sudo apt-get install nginx`.
2. start server: `sudo /etc/init.d/nginx start`.
3. see the example page browsing: `http://localhost` or `http://ip_raspberry` from another device within the network.
* stop the server : `sudo /etc/init.d/nginx stop`.
* NGINX defaults its **web page location** to `/var/www/html`.
* restart server: `sudo service nginx restart`.
* **server config file** : `sudo nano /etc/nginx/sites-available/default` where you can change port and root location.
* `cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup` to backup server configuration file.
* "Available" sites are all stored as individual configuration files inside the directory /etc/nginx/sites-available

The *sites-available* folder is for storing all of your vhost configurations, whether or not they're currently enabled.

The *sites-enabled* folder contains symlinks to files in the sites-available folder. This allows you to selectively disable vhosts by removing the symlink.

##### nginx.conf
```
user www-data;
worker_processes 4;
pid /run/nginx.pid;

events {
        worker_connections 768;
        # multi_accept on;
}
```
**user** - Defines which Linux system user will own and run the nginx server. Most Debian-based distributions use www-data but this may be different in other distros. There are certain use cases that benefit from changing the user; for instance if you run two simultaneous web servers, or need another program’s user to have control over nginx.
**worker_process** - Defines how many threads, or simultaneous instances, of nginx to run.
**pid** - Defines where nginx will write its master process ID, or PID. The PID is used by the operating system to keep track of and send signals to the nginx process.

```
http {

    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    # server_tokens off;

    # server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    ##
    # Gzip Settings
    ##

    gzip on;
    gzip_disable "msie6";
```
**include** - The include statement at the beginning of this section includes the file *mime.types* located at */opt/nginx/conf/mime.types*.
**gzip** - The gzip directive tells the server to use on-the-fly gzip compression to limit the amount of bandwidth used and speed up some transfers.
```
 ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
}
```
Virtual Hosts are used to run more than one website or domain off of a single server. Note: according to the nginx website, virtual hosts are called Server Blocks on the nginx.
Nginx provides us with a layout for this file in the sites-available directory (/etc/nginx/sites-available), and we simply need to copy the text into a new custom file:
`sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/example.com`

Conf file `/etc/nginx/sites-available/default`:
```
server {
        listen 80 default_server;
        listen [::]:80 default_server ipv6only=on;

        root /var/www/html;
        access_log /var/www/appname/current/log/nginx.access.log;
        error_log /var/www/appname/current/log/nginx.error.log info;
  
        index index.html index.htm;

        # Make site accessible from http://localhost/
        server_name localhost;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ /index.html;
                # Uncomment to enable naxsi on this location
                # include /etc/nginx/naxsi.rules
        }
}
```

* To enable it we create a 'symbolic link' inside */etc/nginx/sites-enabled* to the file we just created:

`sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/example.com`

* To enable log: `access_log /srv/www/example.com/logs/access.log;`

* To remove vhost: `sudo rm /etc/nginx/sites-enabled/default`


---

#### Remote desktop
I'm using *tightvncserver*.
1. install vcn: `sudo apt-get install tightvncserver`.
2. `sudo apt-get remove xrdp`.This solve an issue for me.
3. `sudo apt-get install xrdp`.
4. now you can connect with a remote desktop client using raspberry's ip.

---

#### Https with certbot

<p align="center">
  <img src="https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/certbot.png"/>
</p>
Certbot is the next iteration of the Let's Encrypt Client; it obtains TLS/SSL certificates and can automatically configure HTTPS encryption on your server.

Certbot communicates with the Let’s Encrypt CA through a protocol called ACME. While there are many ACME clients available to choose from, Certbot continues to be the most popular choice for organizations and developers that run their own webservers.

1. Install [Certbot](https://certbot.eff.org/#debianjessie-nginx) for Debian 8(jessie). I suppose you have a web server like NGINX. 
```
wget https://dl.eff.org/certbot-auto
chmod a+x certbot-auto
```
3. setup a server name on nginx: 
`sudo nano /etc/nginx/sites-available/default`

edit this line:`server_name www.your_domain_name.com;`

2. certbot have some [plugins]https://certbot.eff.org/docs/using.html#getting-certificates-and-choosing-plugins) to automates both obtaining and installing certs. In this case I'm using NGINX's plugin:

`sudo ./certbot-auto --nginx`

Running this command will get a certificate for you and have Certbot edit your Nginx configuration automatically to serve it. If you're feeling more conservative and would like to make the changes to your Nginx configuration by hand, you can use the **certonly** subcommand.





