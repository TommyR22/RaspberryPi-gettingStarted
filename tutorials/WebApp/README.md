# WebApp
In this example we can control GPIO over Internet with NGINX and FLASK.

# Communication
Here a diagram of information flow:
<p align="center">
  <img src="https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/tutorials/WebApp/webapp_on_raspberrypi.png"/>
</p>

To execute Python Code with respect to the HTTP Request we need uWSGI Server between our Web Server and Python Web Application. In this example we are going to use “uwsgi” which is one of the most popular uWSGI Servers.
