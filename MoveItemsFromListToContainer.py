# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2024-11-21
# Use at your own risk. 

from System.Collections.Generic import List
import sys
from System import Byte, Int32

# Scans backpack for "of the three", "of wildfire", etc. 
# and moves to a container. This is just a dumper script.
# I like to turn in my arties on just one char, so my other
# chars use this to offload. Too lazy to click and drag
# or even use taz uo alt + click.

DUMP_CONTAINER = 0x40133427
DUMP_CONTAINER_2 = 0x40133427
RESOURCE_CONTAINER = 0x40133415

# You can add multiple destination containers, e.g. dump coins into 
# a barrel on porch of house 1 or a chest upstairs. It will check
# for the first one in range and use that.

ITEMS_TO_MOVE = [

    # Loot
    [ "dried herbs",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "gold coin",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "mandrake",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "kindling",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "knot grass",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "amaranth",              DUMP_CONTAINER, DUMP_CONTAINER_2],
   # [ "bone",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "lilypad",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "rauwolfia",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "brambles",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "fertile dirt",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "potion",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "nightshade",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "mandrake root",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "spiders' silk",              DUMP_CONTAINER, DUMP_CONTAINER_2], # '
    [ "garlic",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "sealed scroll",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "necklace",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "sulfurous ash",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "citrine",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "emerald",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "amethyst",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "black pearl",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "arcane gem",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "flawless sapphire",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "ginseng",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "bone",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "wire",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "blood moss",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "power crystal",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "sealed note",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "cranenene",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    [ "cranenene",              DUMP_CONTAINER, DUMP_CONTAINER_2],
    
    
    # Resources
    [ "ingots",              RESOURCE_CONTAINER],
    [ "empty bottle",              RESOURCE_CONTAINER],

]

print("Starting fuckery")

PAUSE_DELAY = 950

def move_items_from_container_recursive(container):
    for item in container.Contains:
        for s in ITEMS_TO_MOVE:
            foundAndMoved = False
            if item.Name is not None and s[0].lower() in item.Name.lower():
                for destContainerSerial in s[1:]:
                    
                    destContainer = Items.FindBySerial(destContainerSerial)
                    #if destContainer is not None and Player.DistanceTo(destContainer) < 2:
                    if destContainer is not None:
                        Items.Move(item, destContainerSerial, item.Amount);
                        Misc.Pause(PAUSE_DELAY)
                        foundAndMoved = True
                        break    
            if foundAndMoved:
                print(item.Name, " moved to ", destContainer.Name)

        if item.IsContainer:
            move_items_from_container_recursive(item)

# Unload players
move_items_from_container_recursive(Player.Backpack)