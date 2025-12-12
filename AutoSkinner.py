# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-10-23
# Use at your own risk.

Player.HeadMessage(42, "Starting Auto Skiner")

# ##########################################################
# #                                                        #
# #              INLINED DEPENDENCIES                      #
# #                                                        #
# #  DO NOT EDIT THIS SECTION - AUTO-GENERATED CODE        #
# #                                                        #
# #  These are dependencies from fm_core that have been    #
# #  automatically inlined. For user-editable code,        #
# #  scroll down to the bottom of this file.               #
# #                                                        #
# ##########################################################

from System import Byte, Int32
from System.Collections.Generic import List
import sys

DAGGER_STATIC_ID = 0x0F52

GATHERERS_PACK_GRAPHIC_ID = 0xAD77

LEATHER_STATIC_ID = 0x1081

PILE_OF_HIDES_STATIC_ID = 0x1079

SCISSORS_GRAPHIC_ID = 0x0F9F

# ##########################################################
# #                                                        #
# #                 USER EDITABLE CODE                      #
# #                                                        #
# #  This is the original script code that you can         #
# #  modify and customize. Edit the parameters, logic,     #
# #  and function calls below as needed for your setup.    #
# #                                                        #
# #  The dependencies above have been automatically        #
# #  inlined and should not be modified.                   #
# ##########################################################

# Auto skinner
# 
# Original author: https://razorenhanced.net/dokuwiki/doku.php?id=toolscripts
# 
# Mine is much worse than the original. It requires Lootmaster or at least auto open corpses
# as this script will no longer open corpses. It will attempt to carve the corpse forever.
# It only carves corpses within 1 tiles.
# You need a plain dagger.
# You need scissors.

# Store leather in a Gatherers pack if it is found. This is a container that reduces leather
# weight by 50%. It is obtained from the huntmaster challenge monthly rewards.
# This must be placed in top level of backpack.
gatherersPack = Items.FindByID(GATHERERS_PACK_GRAPHIC_ID, -1, Player.Backpack.Serial, 0)
leatherContainerSerial = gatherersPack.Serial if gatherersPack is not None else Player.Backpack.Serial
   
dagger = Items.FindByID(DAGGER_STATIC_ID, 0, Player.Backpack.Serial, 0)
if dagger is None:
    print("You should get a dagger")
    sys.exit()

scissors = Items.FindByID(SCISSORS_GRAPHIC_ID, 0, Player.Backpack.Serial, 0)
if scissors is None:
    print("You should get some scissors")
    sys.exit()
    
def cut_leather(scissors, leatherContainerSerial):
    hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, leatherContainerSerial, 0)
    if hides is not None:
        Items.UseItem(scissors)
        Target.WaitForTarget(1000)
        Target.TargetExecute(hides)
        Misc.Pause(100)

from collections import deque

class NumberCache:
    def __init__(self, max_size=30):
        self.cache = deque(maxlen=max_size)  # Auto-cycles when full
    
    def add(self, number):
        """Add a number to the cache"""
        self.cache.append(number)  # Automatically removes oldest when at maxlen
    
    def contains(self, number):
        """Check if number is in cache"""
        return number in self.cache
    
    def get_all(self):
        """Get all cached numbers"""
        return list(self.cache)
        
cache = NumberCache(max_size = 30)

while True:
    while Player.Visible:
        skin = Items.Filter()
        skin.Enabled = True
        skin.RangeMin = 0
        skin.RangeMax = 2
        skin.IsCorpse = True
        corpses = Items.ApplyFilter(skin)
        for corpse in corpses:
            if cache.contains(corpse.Serial) or not Player.Visible:
                continue
                
            Items.UseItem(dagger)
            Target.WaitForTarget(1000)
            Target.TargetExecute(corpse)
            Misc.Pause(750)
            Items.UseItem(corpse)
            Misc.Pause(750)
            hides = Items.FindByID(PILE_OF_HIDES_STATIC_ID, -1, corpse.Serial, 0)
            if hides is not None:
                Items.Move(hides, leatherContainerSerial, hides.Amount)
                Misc.Pause(650)
                cut_leather(scissors, leatherContainerSerial)
            cache.add(corpse.Serial)
        cut_leather(scissors, leatherContainerSerial)
        
        Misc.Pause(250)

    Misc.Pause(1000)