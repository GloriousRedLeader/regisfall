from System.Collections.Generic import List
from math import ceil
import sys
import threading, atexit
from System import Byte, Int32


filter = Items.Filter()
filter.Movable = 0
filter.OnGround = True
filter.RangeMax = 2
filter.Graphics = List[Int32]([0x1070]) 
dummies = Items.ApplyFilter(filter)


while True:
    for dummy in dummies:
        print("dummy: ", dummy.Name)
        Items.UseItem(dummy)
        Misc.Pause(750)