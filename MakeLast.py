# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-10-23
# Use at your own risk.

Player.HeadMessage(42, "Make Last Item")

# Assumes gump is already open and youve already made an item.
# This script  just presses make last until the tool dies.

from System import Byte, Int32
from System.Collections.Generic import List
import sys

craftGumpID = Gumps.CurrentGump()

while True:
    if not Gumps.HasGump(craftGumpID):
        print("You need to open the crafting gump and create one item")
        sys.exit()

    Gumps.SendAction(craftGumpID, 21)
    Gumps.WaitForGump(craftGumpID, 3000)
    Misc.Pause(650)
    