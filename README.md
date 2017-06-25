# RaspberryPi-gettingStarted
A curated list of Raspberry Pi tools, projects, images and resources

### Gpio pinout
[RaspberryPi 3](https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/pi3_gpio.png)

### Resources
[Configure and connect using SSH](#configure-and-connect-using-ssh)


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
7. OPTIONAL: consider to change ssh port for more security in `/etc/ssh/sshd_config` file.

##### Connection via ssh
`ssh user_raspberry@ip_raspberry -p <port_number>`

##### Ssh tips
* Coping file from PC-to-Raspberry: `scp /path/to/local/file remote_user@remote_host:/path/to/remote/file` (ex:scp project.py pi@192.168.0.200:projects/).
* Coping file from Raspberry-to-Pc: `scp remote_user@remote_host:/path/to/remote/file /path/to/local/file`.



