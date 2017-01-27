import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)


while(True):
	button=GPIO.input(4)

	if(button):
		pygame.init()
		pygame.mixer.music.load("badswap.wav")
		pygame.mixer.music.play()