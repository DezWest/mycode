#!/usr/bin/env python

import sys

def exit_game ():
    print("You Lose")
    sys.exit ()

#player intro & welcome
print("Welcome to Labrynth")
 
print("Choose your best skill")
skill = input("Type 'clairvoyance' or 'precognition': ")

if skill == "clairvoyance":
    input("Power to sense and communicate with paranormal activity")
elif skill == "precognition":
    input("Power to sense opposing danger")
else:
    exit_game ()
#The game starts

print("You wake up in an all white space scared and alone with two doors in front of you. Would you like to go left or right?")
choice = input("Type 'left' or 'right' to proceed")

if choice == "left":
    choice == input("You step through the door and fall to your death")
    exit_game ()

elif choice == "right": 
    choice == input("You safely pass through the door safely")
else:
    exit_game ()

print("You continue into the next room. You notice what seems to be a dark figure standing in front of a door. Your selected skill is activated")

choice = input("Type 'clairvoyance' or 'precognition' to proceed")

if choice == "clairvoyance":
    choice == input("You ask the being to reveal itself. The being emerges from the shadow and asks what do you want? You respond with 'I am looking for a way home can you show me?' The being moves and under him reveals a secret path in which you go through")

elif choice == "precognition":
    choice == input("You recognize the being as a threat and try to avoid it. The being instantly takes notice and moves towards you. You run around the being in an attempt to escape. You run through the door the being was standing in front of and fall into the abyss. YOU HAVE DIED! Should have chosen the better power!")
    sys.exit ()
else:
    exit_game ()
