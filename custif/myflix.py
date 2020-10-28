#!/usr/bin/env python3
message = 'Never Have I ever '

fingers= 5

#Guess which wacky question is correct for DezWest. If you have any fingers left at the end YOU WIN


print("Never have I ever")
Q1 = input (" A) Been to Asia. B) Been to South America. [A/B]? : ")

if Q1 == "A":
    pass
    #message= "Keep fingers up"
elif Q1 == "B":
    fingers -= 1
    #message= "Put one finger down"

print("Never have I ever")
Q2 = input (" A) Flown a plane. B) Driven a car. [A/B]? : ")

if Q2 == "B":
    message= "Keep fingers up"
elif Q2 == "A":
    fingers -= 1#    message= "Put one finger down"

print("Never have I ever")
Q3 = input (" A) Gone Skiing. B) Gone Snowboarding. [A/B]? : ")

if Q3 == "B":
    message= "keep fingers up"
elif Q3 == "A":
    fingers -= 1#    message= "Put one finger down"

print("Never have I ever")
Q4 = input (" A) Stopped skynet from coming online. B) Traveled to a galaxy far far away. [A/B]? : ")

if Q4 == "A":
    message= " Keep fingers up"
elif Q4 == "B":
    fingers -= 1#    message= "Put one finger down"

print("Never have I ever")
Q5 = input (" A) Thought Lebron was better than Jordan. B) Dunked a basketball. [A/B]? : ")

if Q5 == "A":
    message= "Keep fingers up"
elif Q5 == "B":
    fingers -= 1#    message= "Put one finger down"

print("check the number of fingers left")
print(fingers)

if fingers == 5:
    print("You're boring")

elif fingers >= 3:
    print("You're all right.")

else:
    print("You're crazy!")
