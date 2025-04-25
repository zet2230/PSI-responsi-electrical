# Delay diganti2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
enable_pin = 2
coil_A_1_pin = 27
coil_A_2_pin = 22
coil_B_1_pin = 23
coil_B_2_pin = 24
 
# adjust if different
StepCount = 4
Seq = [0,0,0,0]
Seq[0] = [1,0,0,0]
Seq[1] = [0,0,1,0]
Seq[2] = [0,1,0,0]
Seq[3] = [0,0,0,1]
#Seq[4] = [1,0,0,0]
#Seq[5] = [1,0,1,0]
#Seq[6] = [0,0,1,0]
#Seq[7] = [0,1,1,0]
 
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
       for j in range(StepCount):
           setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
           print(j)
           time.sleep(delay)
       #time.sleep(0.01)
 
def backward(delay, steps):
    for i in range(steps):
       for j in reversed(range(StepCount)):
          setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
          time.sleep(delay)

def one_step(delay):
    for j in range(StepCount):
        setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
        time.sleep(delay)
 
if __name__ == '__main__':
    while True:
        delay = 1.5       #Time Delay (ms)
        steps = 100          #How many steps forward?
        forward(delay/1000, int(steps))
