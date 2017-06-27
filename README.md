# RaspberryPi-gettingStarted
A curated list of Raspberry Pi tools, projects, images and resources

<p align="center">
  <img src="https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/raspberry_pi.png"/>
</p>

### Gpio pinout
[raspberry-pi 3 schema](https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/pi3_gpio.png)

### Resources
* [Configure and connect using SSH](#configure-and-connect-using-ssh)
* [Autorun python script on boot using systemd](#autorun-python-script-on-boot-using-systemd)
* [Tensorflow on raspberry](https://github.com/samjabrahams/tensorflow-on-raspberry-pi)

### Tutorials
**In these tutorials I'm using [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) library for python**
* [LED](#led)

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
1. `ssh-keygen -t rsa -C "your_email@youremail.com"` and follow instructions.
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
`ssh user_raspberry@ip_raspberry -p <port_number>`

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



