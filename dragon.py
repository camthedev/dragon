#!/usr/bin/env python

#dictionary
gold = "20"
x = "5"
y = "1"
maxhp = "30"
hp = "25"
fishingrod = "false"
avatar = "&"
location = "Fishing Hut"
incombat = "false"
fish = "false"
dead = "false"
# username = raw_input('Enter your name: ')
username = "bob"
action = None

# -----------------------

def get_compass(x, y):
    # if x == "5" and y == "1":
    # this needs to handle different x/y coordinates and update string
    compass_string = ".W..&...S"
    return compass_string

def print_status():
    print "-------"
    # print username + " is your name"
    print "%s    -   gold: %s    -   hp: %s:%s" % (get_compass(x,y), gold, hp, maxhp)
    print "You wake up in a forest, not knowing how you got there"
    print "To your left is a river, to your right is a hut"
    print "-------"


def action_helper():
    print "This program understands lots of commands"
    print "You could examine or use the hut and the river. Move quickly, you are getting hungry"
    raw_input('Press enter to continue: ')


def input_action():
    print "What do you do?"
    action = raw_input()

    if action == "examine hut":
        print ".W.....&S"
        print "It's a fishing hut, with an old rod and some gold inside inside."
    elif action == "use hut":
        print ".W.....&S"
        print "You take the rod and the gold."
        gold = "23"
        fishingrod = "true"

    elif action == "help":
        action_helper()
    elif action == "quit":
        sys.exit(0)
    else:
        print "i don't know how to " + action

    return action



# main program
while action != "quit":
    # clear()
    print_status()
    input_action()




















