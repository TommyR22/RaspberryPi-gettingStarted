# RaspberryPi-gettingStarted
A curated list of Raspberry Pi tools, projects, images and resources

### Gpio pinout
[RaspberryPi 3](https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/images/pi3_gpio.png)

### Resources
[Connect using SSH](#connect-using-ssh)


#### Connect using SSH
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
```ChallengeResponseAuthentication no
PasswordAuthentication no (uncomment line)
UsePAM no```


