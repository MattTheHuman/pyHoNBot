#!/usr/bin/env python
"""
info.py - Phenny Information Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

from time import sleep
from hon.packets import ID

def doc(phenny, input): 
   """Shows a command's documentation, and possibly an example."""
   name = input.group(2)
   name = name.lower()

   if phenny.doc.has_key(name): 
      phenny.reply(phenny.doc[name][0])
      if phenny.doc[name][1]: 
         phenny.say('e.g. ' + phenny.doc[name][1])
doc.commands = ['doc']
doc.example = '.doc doc'
doc.priority = 'low'

def commands(phenny, input): 
   # This function only works in private message
   if input.origin[0] == ID.HON_SC_CHANNEL_MSG:
      phenny.reply("I only respond to this command in whisper. Type: /w " + phenny.nick + " .commands")
      return
   if isinstance(input.origin[1],int): return
   names = ', '.join(sorted(phenny.doc.iterkeys()))
   phenny.say('Commands I recognise:')
   for line in [names[i:i+245] for i in range(0, len(names), 245)]:
      phenny.say(line)
      sleep(1)
   phenny.say(("For help, do '.doc example' where example is the " + 
               "name of the command you want help for."))
commands.commands = ['commands']
commands.priority = 'low'

def help(phenny, input): 
   response = (
      'Hi, I\'m a bot. My name is {0}. Say ".commands" to me in private for a list '.format(phenny.config.nick) + 
      'of my commands. My owner is {0}.'.format(phenny.config.owner))
   phenny.reply(response)
help.commands = ['help']
help.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
