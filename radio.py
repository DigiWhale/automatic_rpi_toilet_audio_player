import RPi.GPIO as GPIO
import time
import pygame
import alsaaudio
from get_latest_video import *

# m = alsaaudio.Mixer()
# current_volume = m.getvolume() # Get the current Volume
# m.setvolume(100) # Set the volume to 70%.

switch = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
  if GPIO.input(switch):
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/latest_video.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.pause()
    while pygame.mixer.music.get_busy() == True:
      if GPIO.input(switch):
        pygame.mixer.music.unpause()
      else:
        pygame.mixer.music.pause()
    try:
      processor()
    except:
      pass

