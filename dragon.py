#!/usr/bin/env python

import sys
import os
import time


class player:
    def __init__(self):
        self.gold = 20
        self.x = 4
        self.y = 1
        self.maxhp = 30
        self.hp = 25
        self.inventory = []
        self.history = []
        self.name = None

    def add_to_history(self, command_string):
        self.history.append(command_string)

    def show_history(self):
        for item in self.history:
            print item
        raw_input('Press enter to continue: ')

    def move_player(self, direction, spaces):
        return None



class grid:
    def __init__(self):
        self.max_x = 9
        self.max_y = 1
        self.grid_contents = []
        for num in range(1, self.max_x):
            icon = "."
            self.grid_contents.append(icon)

        self.grid_contents[0] = "W"
        self.grid_contents[7] = "S"

    def get_grid_string(self, x, y):
        self.grid_contents[x] = "&"
        return ''.join(self.grid_contents)




# fishingrod = False
# location = "Fishing Hut"
# incombat = False
# fish = False
# dead = False


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# def build_grid(max_x, max_y):


def print_status(p, g):
    # clear()
    print "-------"
    print "%s    -   gold: %s    -   hp: %s:%s" % (g.get_grid_string(p.x, p.y), p.gold, p.hp, p.maxhp)
    print "You wake up in a forest, not knowing how you got there"
    print "To your left is a river, to your right is a hut"
    print "-------"


def action_helper():
    print "This program understands lots of commands:"
    print ">>>>> examine, goto, help, history, inventory, move, eat, use"
    print ""
    print "You could examine or use the hut and the river. Move quickly, you are getting hungry"
    raw_input('Press enter to continue: ')


def input_action(p):
    print "What do you do? (type 'help' for assistance)"
    full_action = raw_input()
    p.add_to_history(full_action)
    action = full_action.split()


    if action == "examine hut":
        print "It's a fishing hut, with an old rod and some gold inside inside."
    elif action == "use hut":
      #  if not fishingrod:
        print "You take the rod and the gold."
        # gold + 3
        #    fishingrod = True
     #   elif fishingrod:
    #        print "nothing left"
    elif action == "examine river":
        print "The river is flowing quite fast. You can see some fish inside"
    elif action == "use river":
        #if fishingrod = "true"
            #print "You catch a fish"
            #fish = "true"
        #elif:
        print "Not a good time to take a swim, bro"
    elif action == "help":
        action_helper()
    elif action == "history":
        p.show_history()
    elif action == "quit":
        sys.exit(0)
    else:
        print "i don't know how to " + action

    # time.sleep(1)
    return action



# main program
p = player()
g = grid()

username = raw_input('Enter your name: ')
p.name = username
print p.name + " is your name"

action = None

while action != "quit":
    # clear()
    print_status(p, g)
    action = input_action(p)




















