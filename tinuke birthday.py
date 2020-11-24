#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:45:48 2020

@author: babaniyi olaniyi

A program that areminds me of my sister's birthday
"""

from datetime import datetime
from threading import Timer
import random


x = datetime.today()

y = x.replace(day = x.day+1, hour = 10, minute = 0)

delta_t = y - x

secs = delta_t.seconds + 1

messages_list = ['On your special day I wish you only smiles and joy. May each minute of your life be filled with happiness and may this birthday be just perfect for you!',
  "To the best, most wonderful, most loving sister in the world on her birthday and every day. Happy Birthday!",
 "I hope you know how much I love you, my sis. Happy Birthday!"]

message = random.choice(messages_list)

def birthday(sister_name):
    print("Hey Babaniyi!, today is your sister", sister_name, "birthday, send her a message\n")
    print("Send the message below to your sister\n\n")
    print("--------------------------------------------------------")
    print(message)
    print("--------------------------------------------------------")

t = Timer(secs, birthday, ['Tinuke'])
t.start()



#_____________ Use codes with only Timer,
"""
 timer uses seconds of the day e.g Timer(30.0, birthday, [Tinuke]) - runs after 30 seconds
 If the function does not contain an argument e.g sister name, use  Timer(seconds, birthday)

 
 def hello():
    print "hello, world"

t = Timer(30.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed

"""