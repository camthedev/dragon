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

    def move_player(self, direction, spaces):
        if direction == "left":
            self.x = self.x - 1
            print "okay. moving " + direction + " " + str(spaces) + " spaces."
        elif direction == "right":
            self.x = self.x + 1
            print "okay. moving " + direction + " " + str(spaces) + " spaces."
        else:
            print ("i can't move " + direction)


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
        self.clear_previous_location()
        self.grid_contents[x] = "&"
        return ''.join(self.grid_contents)

    def clear_previous_location(self):
        self.grid_contents = ["." if gl=="&" else gl for gl in self.grid_contents]

def action_goto(p,g,target):
    print "Going to "+ target
    print "It appears that "+ target + " is on fire. I recommend running."



# def clear():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')


def print_status(p, g):
    # clear()
    print "-------"
    print "%s    -   gold: %s    -   hp: %s:%s" % (g.get_grid_string(p.x, p.y), p.gold, p.hp, p.maxhp)
    print "-------"


def action_helper():
    print "Each command should have two parts."
    print "An action you want to do, and a target you want to perform the action on"
    print "Some things you can do: buy, examine, goto, inventory, move, eat, use"
    print "Examples>>"
    print "   move left"
    print "   use map"
    print "   buy sword"
    print "   goto irontown"
    print ""
    print "You can also use: help, history, or quit"
    print ""
    # print "You could examine or use the hut and the river. Move quickly, you are getting hungry"


def input_action(p, g):
    action = None
    print "What do you do? (type 'help' for assistance)"
    full_action = raw_input()
    p.add_to_history(full_action)
    # needs to handle a null input

    if not " " in full_action:
        if full_action in ["buy", "examine", "goto", "inventory", "move", "eat", "use"]:
            print full_action + " what?"
        elif full_action == "help":
            action_helper()
        elif full_action == "history":
            p.show_history()
        elif full_action == "quit":
            sys.exit(0)
        else:
            print "i don't know how to " + full_action

        raw_input('Press enter to continue: ')
        return action

    action_split = full_action.split()

    if len(action_split) > 2:
        print("Try stating that another way.")
        action_helper()
        raw_input('Press enter to continue: ')
        return action
    else:
        action = action_split[0]
        action_target = action_split[1]

    if action == "move":
        p.move_player(action_target, 1)
    elif action == "goto":
        action_goto(p,g,action_target)
    # elif action == "examine hut":
    elif action == "examine":
        print "It's a fishing hut, with an old rod and some gold inside inside."
    # elif action == "use hut":
    elif action == "use":
        #if not fishingrod:
        print "You take the rod and the gold."
        self.gold + 3
        self.fishingrod = True
     #   elif fishingrod:
    #        print "nothing left"
    # elif action == "examine river":
    #     print "The river is flowing quite fast. You can see some fish inside"
    # elif action == "use river":
        #if fishingrod = "true"
            #print "You catch a fish"
            #fish = "true"
        #elif:
        # print "Not a good time to take a swim, bro"
    else:
        print "i don't know how to " + action
        raw_input('Press enter to continue: ')
    # time.sleep(1)
    return action



# main program
p = player()
g = grid()

username = raw_input('Enter your name: ')
p.name = username
print "Welcome to Dragon Quest, " + p.name
print "As the game begins, you wake up in a forest, not knowing how you got there"
print "To your left is a river, to your right is a hut"

action = None

while action != "quit":
    # clear()
    print_status(p, g)
    action = input_action(p, g)





