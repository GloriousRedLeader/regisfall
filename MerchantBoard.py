# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-10-23
# Use at your own risk.

Player.HeadMessage(42, "Merchant Board Turn In")
print("Close all gumps")

from System.Collections.Generic import List
from System import Byte, Int32
import sys

ITEMS_TO_MOVE = [
    #"nightshade", 
    "nettlebloom", 
    "mountain sage", 
    #"leather", 
    #"spined leather", 
    #"iron ingots", 
    #"tin ingots", 
    #"copper ingots", 
    #"oak boards", 
    #"pine boards", 
    #"redwood boards", 
    #"bandages", 
    #"wool", 
    "fertile dirt", 
    #"empty bottle", 
    "pumpkin", 
    "apple", 
    #"dagger", 
    "scimitar", 
    "katana", 
    #"metal box", 
    "platemail gloves", 
    "plate helm", 
    "spiked shield", 
    "clock parts", 
    "hinge", 
    "tinker tools", 
    "pitcher", 
    "candelabra", 
    "manacle", 
    "wooden club", 
    "wooden shield", 
    "gnarled staff", 
    "longbow", 
    "crossbow", 
    "shaft", 
    "fish", 
    "dough", 
    "sweet dough", 
    "shirt", 
    "boots", 
    "cloth gloves", 
    #"hooded robe", 
    "leather arms", 
    "leather legs", 
    "bone gloves", 
    "bone helm", 
    "bone arms", 
    "bone leggings", 
]

filter = Items.Filter()
filter.OnGround = True
filter.RangeMax = 3
filter.Graphics = List[Int32]([0x1E5E]) 
boards = Items.ApplyFilter(filter)

BOARD_GUMP_ID = 9
SELL_GUMP_ID = 20
PAUSE_DELAY_MS = 750

board = None
if boards is not None and len(boards) > 0:
    board = boards[0]

if board is None:
    print("You are not near a board!")
    sys.exit()
    
# These are dynamic probably based on sell lists
boardGumpId = None
sellGumpId = None

Items.UseItem(board)
Misc.Pause(1000)
boardGumpId = Gumps.CurrentGump()

if not Gumps.HasGump(boardGumpId):
    print("Could not find the board gump, try again")
    sys.exit()
    
Gumps.SendAction(boardGumpId, 1)
Misc.Pause(1000)
sellGumpId = Gumps.CurrentGump()

if not Gumps.HasGump(sellGumpId):
    print("Internal error, try again")
    sys.exit()
    
print("boardGumpId ", boardGumpId)
print("sellGumpId ", sellGumpId)

while True:
    Gumps.CloseGump(boardGumpId)
    Gumps.CloseGump(sellGumpId)
    Items.UseItem(board)
    Gumps.WaitForGump(boardGumpId, 3000)
    Gumps.SendAction(boardGumpId, 1)
    Misc.Pause(PAUSE_DELAY_MS)
    Gumps.WaitForGump(sellGumpId, 3000)
    Gumps.SendAction(sellGumpId, 1)
    Target.WaitForTarget(3000)
    Misc.Pause(PAUSE_DELAY_MS)
    soldAnItem = False
    for item in Player.Backpack.Contains:
        for s in ITEMS_TO_MOVE:
            if item.Name is not None and s.lower() in item.Name.lower():
                Journal.Clear()
                print("Selling item ", item.Name)
                Target.TargetExecute(item)
                Target.WaitForTarget(3000)
                Misc.Pause(750)
                soldAnItem = True
                break

    if not soldAnItem:
        print("Ending")
        break
    else:
        print("Going again")
            
Target.Cancel()
