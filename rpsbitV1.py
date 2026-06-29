# Made by Ezel K. A rock, paper, scissors app for the micro:bit V2.
# Read the file labelled 'rpsbitV2_description.txt' in this repo to learn how to use this app and install this app onto your micro:bit.
# Copyright (C) 2026 Ezel K.
# Licensed under the MIT License (see LICENSE file).

from microbit import *
import music
import random

user = 0
robot = 0

rock = Image('09990:'
             '99999:'
             '99999:'
             '99999:'
             '09990:')

paper = Image('09990:'
              '09990:'
              '09990:'
              '09990:'
              '09990:')

scissors = Image('90009:'
                 '09090:'
                 '00900:'
                 '99099:'
                 '99099:')

display.show(Image.HAPPY)
music.play(music.BA_DING)
sleep(625)
music.play(['c'])
display.scroll(3)
music.play(['c'])
display.scroll(2)
music.play(['c'])
display.scroll(1)
display.show(Image.HAPPY)
music.play(music.JUMP_UP)
while user == 0:
  if button_a.is_pressed():
    user=2
  elif button_b.is_pressed():
    user=3
  elif pin2.is_touched():
    user=1
robot=random.randint(1,3)
if user == 1:
  if robot == 1:
    sleep(750)
    display.show(rock)
    sleep(750)  
    display.show(Image.ASLEEP)
    music.play(['c','c','c'])
  elif robot == 2:
    sleep(750)
    display.show(paper)
    sleep(750) 
    display.show(Image.NO)
    music.play(music.DADADADUM)
  elif robot == 3:
    sleep(750)
    display.show(scissors)
    sleep(750) 
    display.show(Image.YES)
    music.play(music.POWER_UP)
elif user == 2:
  if robot == 2:
    sleep(750)
    display.show(paper)
    sleep(750) 
    display.show(Image.ASLEEP)
    music.play(['c','c','c'])
  elif robot == 3:
    sleep(750)
    display.show(scissors)
    sleep(750) 
    display.show(Image.NO)
    music.play(music.DADADADUM)
  elif robot == 1:
    sleep(750)
    display.show(rock)
    sleep(750) 
    display.show(Image.YES)
    music.play(music.POWER_UP)
elif user == 3:
  if robot == 2:
    sleep(750)
    display.show(paper)
    sleep(750) 
    display.show(Image.YES)
    music.play(music.POWER_UP)
  elif robot == 3:
    sleep(750)
    display.show(scissors)
    sleep(750) 
    display.show(Image.ASLEEP)
    music.play(['c','c','c'])
  elif robot == 1:
    sleep(750)
    display.show(rock)
    sleep(750) 
    display.show(Image.NO)
    music.play(music.DADADADUM)
