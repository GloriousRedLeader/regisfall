# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/regisfall
#   2025-11-16
# Use at your own risk. 

Player.HeadMessage(42, "Item Dumper")

from System.Collections.Generic import List
import sys
from System import Byte, Int32

# Easy item dumper. Thats all this is. Configure item names and desired containers in the list below.
# Bind to a hotkey. And youre set. Why use this over razors agent? Well, Im not sure. I suppose because
# this is a single interface where you can define MULTIPLE containers for an item. E.g.
# If youre at the bank, drop it into a bag there, or if youre at yoru house, drop it in a chest there.

VALUABLE_CONTAINER = 0x4004C686
MAP_CONTAINER = 0x400B946C
RESOURCES_CONTAINER = 0x40133415
FARM_CONTAINER = 0x40133427
LOADOUT_CONTAINER = 0x4012484B
RARE_CONTAINER = 0x40124850

# You can add multiple destination containers, e.g. dump coins into 
# a barrel on porch of house 1 or a chest upstairs. It will check
# for the first one in range and use that.

ITEMS_TO_MOVE = [

    # Rares
    [ "covered chair",              RARE_CONTAINER],
    [ "skull with candle",              RARE_CONTAINER],
    [ "rope",              RARE_CONTAINER],
    [ "0000",              RARE_CONTAINER],

    # Valuables
    [ "gold coin",              VALUABLE_CONTAINER],
    [ "sealed scroll",          VALUABLE_CONTAINER],
    [ "necklace",              VALUABLE_CONTAINER],
    [ "citrine",              VALUABLE_CONTAINER],
    [ "emerald",              VALUABLE_CONTAINER],
    [ "amethyst",              VALUABLE_CONTAINER],
    [ "arcane gem",              VALUABLE_CONTAINER],
    [ "power crystal",              VALUABLE_CONTAINER],
    [ "sealed note",              VALUABLE_CONTAINER],
    [ "wire",              VALUABLE_CONTAINER],
    [ "diamond",              VALUABLE_CONTAINER],
    [ "sapphire",              VALUABLE_CONTAINER],
    [ "ruby",              VALUABLE_CONTAINER],
    [ "tourmaline",              VALUABLE_CONTAINER],
    [ "amber",              VALUABLE_CONTAINER],
    [ "plans",              VALUABLE_CONTAINER],
    [ "rubie",              VALUABLE_CONTAINER],
    [ "recipe",              VALUABLE_CONTAINER],
    [ "weapon augment",              VALUABLE_CONTAINER],
    [ "conquest token",              VALUABLE_CONTAINER],
    [ "arcane essence",              VALUABLE_CONTAINER],
    
    # Maps
    [ "treasure map",              MAP_CONTAINER],
    
    # Resources
    # [ "bone",              RESOURCES_CONTAINER],
    [ "ingots",              RESOURCES_CONTAINER],
    [ "boards",              RESOURCES_CONTAINER],
    [ "cut leather",              RESOURCES_CONTAINER],
    [ "tool kit",              RESOURCES_CONTAINER],
    [ "saw",              RESOURCES_CONTAINER],
    #[ "pickaxe",              RESOURCES_CONTAINER],
    [ "boards",              RESOURCES_CONTAINER],
    [ "logs",              RESOURCES_CONTAINER],
    [ "feather",              RESOURCES_CONTAINER],
    [ "pile of wool",              RESOURCES_CONTAINER],
    [ "bale of cotton",              RESOURCES_CONTAINER],
    [ "smith's hammer",              RESOURCES_CONTAINER], # '
    [ "ore",              RESOURCES_CONTAINER],
    [ "dragon scale",              RESOURCES_CONTAINER],
    [ "bloodroot",              RESOURCES_CONTAINER],
    [ "dragon's blood",              RESOURCES_CONTAINER], # '
    
    
    # Farm
    [ "dried herbs",              FARM_CONTAINER],
    [ "kindling",              FARM_CONTAINER],
    [ "knot grass",              FARM_CONTAINER],
    [ "amaranth",              FARM_CONTAINER],
    [ "lilypad",              FARM_CONTAINER],
    [ "rauwolfia",              FARM_CONTAINER],
    [ "brambles",              FARM_CONTAINER],
    [ "fertile dirt",             FARM_CONTAINER],
    [ "cut of raw ribs",             FARM_CONTAINER],
    [ "raw bird",             FARM_CONTAINER],
    [ "nettlebloom",             FARM_CONTAINER],
    [ "mountain sage",             FARM_CONTAINER],
    [ "wild tobacco",             FARM_CONTAINER],
    [ "seed",             FARM_CONTAINER],
    [ "green thorns",             FARM_CONTAINER],
    [ "grave weed",             FARM_CONTAINER],
    [ "broadleaf",             FARM_CONTAINER],
    [ "tundra moss",             FARM_CONTAINER],
    [ "kingsfoil",             FARM_CONTAINER],
    
    # LOADOUT_CONTAINER
    [ "mandrake",              LOADOUT_CONTAINER],
    [ "potion",              LOADOUT_CONTAINER],
    [ "nightshade",              LOADOUT_CONTAINER],
    [ "mandrake root",              LOADOUT_CONTAINER],
    [ "spiders' silk",              LOADOUT_CONTAINER], # '
    [ "garlic",              LOADOUT_CONTAINER],
    [ "sulfurous ash",              LOADOUT_CONTAINER],
    [ "ginseng",              LOADOUT_CONTAINER],
    [ "black pearl",              LOADOUT_CONTAINER],
    [ "batwing",              LOADOUT_CONTAINER],
    [ "blood moss",              LOADOUT_CONTAINER],
    [ "empty bottle",              LOADOUT_CONTAINER],
    [ "bola balls",              LOADOUT_CONTAINER],
    [ "arrow",              LOADOUT_CONTAINER],
    [ "lockpick",              LOADOUT_CONTAINER],
    [ "clean bandage",              LOADOUT_CONTAINER],
    #[ "cooked bird",              LOADOUT_CONTAINER],
    [ "daemon bone",              LOADOUT_CONTAINER],
    [ "crossbow bolt",              LOADOUT_CONTAINER],
    [ "cranenene",              00000000],

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
                    if destContainer is not None and Player.DistanceTo(destContainer) <= 2:
                    #if destContainer is not None:                        
                        Items.Move(item, destContainerSerial, item.Amount);
                        Misc.Pause(PAUSE_DELAY)
                        foundAndMoved = True
                        break    
            if foundAndMoved:
                print(item.Name, " moved to ", destContainer.Name, " x ", item.Amount)
                break
                

        if item.IsContainer:
            move_items_from_container_recursive(item)

# Unload players
move_items_from_container_recursive(Player.Backpack)

print("Done")