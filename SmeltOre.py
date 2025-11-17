print("Smelt Ore")

from System.Collections.Generic import List
from System import Byte, Int32
import sys

FORGE_ITEM_IDS = [0x0FB1]

filter = Items.Filter()
filter.OnGround = True
filter.RangeMax = 2
filter.Graphics = List[Int32](FORGE_ITEM_IDS) 
forges = Items.ApplyFilter(filter)

if forges is None or len(forges) == 0:
    print("No forges nearby")
    sys.exit()


ores = Items.FindAllByID(0x19B9, -1,  Player.Backpack.Serial, 0) 
for ore in ores:
    Items.UseItem(ore)
    Target.WaitForTarget(3000)
    Target.TargetExecute(forges[0])
    Misc.Pause(750)
