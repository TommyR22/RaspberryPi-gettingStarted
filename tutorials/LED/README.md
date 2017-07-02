### LED
* *led_button.py* - turn on led when press button. 
* *led_pwm.py* - turn on led using PWM.

#### PWM
With **Pulse Width Modulation**(PWM) we can simulate analog voltages.
For many applications, such as controlling LED brightness, this approach works very well.
The implementation requires you to think in terms of a signal with a frequency and a duty cycle.
PWM is available as an output mode on the general-purpose I/O ports, controlled in either hardware or software (RPi.GPIO has only software).
The WiringPi library appears to support both hardware PWM output on one GPIO pin and software PWM on any of the other GPIO pins. Meanwhile the RPIO.PWM library does PWM by DMA on any GPIO pin.
If your application is tolerant of low-timing resolution and high jitter then you could use a software or DMA assisted timing loop. If you want higher precision / lower jitter PWM then you may need hardware assistance.

Consider a signal with a frequency of 100 Hz (freq = 1/Period). This signal would have a Period of 10 milliseconds (Period = 1/frequency). 
and the signal repeats itself every 10 milliseconds. If the signal had a duty cycle of 100%, it would be “High” 100% of the time, and “Low” 0% of the time. If it had a duty cycle of 50% it would be high 50% of the time and duty cycle 0% it's "Low" for all period.
(.5X10 milliseconds= 5 milliseconds) and low 50% of the time (.5X10 milliseconds = 5 milliseconds).
The Raspberry Pi can only simulate analog voltages between 0 and 3.3 volts because max output voltage is 3.3 v.It means that with a duty cycle of 100% we have 3.3v, with 50% 1.6v and with 0% 0v. So we can control led brightness or a motor's speed.

<p align="center">
  <img src="https://github.com/TommyR22/RaspberryPi-gettingStarted/blob/master/tutorials/LED/DutyCycle_WaveForms.png"/>
</p>

##### PWM with Rpi.GPIO
`p = GPIO.PWM(channel, frequency)` - create pwd instance.

`p.start(dc)` - where "dc" is the duty cycle (0.0 <= dc <= 100.0).

`p.ChangeFrequency(freq)` - where freq is the new frequency in Hz.

`p.ChangeDutyCycle(dc)` - where 0.0 <= dc <= 100.0.

`p.stop()`- stop pwd.








