# Razor Enhanced Scripts for Ultima Online by
#   GRL  
#   https://github.com/GloriousRedLeader/omgarturo
#   2025-09-19
# Use at your own risk.

Player.HeadMessage(42, "Auto Pet Feeder")

from System import Byte, Int32
from System.Collections.Generic import List

def get_pets(range = 10, checkLineOfSight = True, mobileId = None):
    pets = []
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = checkLineOfSight
    
    if mobileId is not None:
        fil.Bodies = List[Int32]([mobileId])
    
    blues = Mobiles.ApplyFilter(fil)    
    for blue in blues:
        if blue.CanRename:
            pets.append(blue)
    return pets



FOOD = [
    "pumpkin"
]

while True:

    pets = get_pets()

    if len(pets) > 0:
        for item in Player.Backpack.Contains:
            for f in FOOD:
                if f.lower() in item.Name.lower():
                    Items.Move(item, pets[0], 1)
                    break
        
        
    else:
        print("No pet nearby")
        break
        
    Misc.Pause(1500)