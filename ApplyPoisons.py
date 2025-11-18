Player.HeadMessage(42, "Apply Poison to Weapon")

from System import Byte, Int32
from System.Collections.Generic import List
import sys
import time

kryss = Player.GetItemOnLayer("RightHand")

if kryss is None:
    print("No weapon found")
    sys.exit()
    
for p in Items.GetProperties(kryss.Serial, 3000):
    print(p)