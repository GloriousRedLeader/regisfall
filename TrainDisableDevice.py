print("Attempts to unlock nearby chest")

from System.Collections.Generic import List
from System import Byte, Int32
import sys
    
while Player.GetSkillValue("Disable Device") < Player.GetSkillCap("Disable Device"):
    skill = Player.GetSkillValue("Disable Device")
    if skill < 30:
        print("You need at least 30 disable to device to use this")
        sys.exit()
        
    Journal.Clear()
    Misc.Pause(1000)
    chestName = None
    if skill < 50:
        chestName = "novice"
    elif skill < 70:
        chestName = "apprentice"
    elif skill < 90:
        chestName = "expert"
    elif skill < 100:
        chestName = "master"
        
    filter = Items.Filter()
    filter.OnGround = True
    filter.RangeMax = 2
    filter.Graphics = List[Int32]([0x09A8]) 
    filter.Name = chestName
    chests = Items.ApplyFilter(filter)
    
    if chests is None or len(chests) == 0:
        print("Stopping, need to be near a training chest")
        sys.exit()

    lockpicks = Items.FindByID(0x14FC,0,Player.Backpack.Serial,0)
    if lockpicks is None:
        print("Not enough lockpicks")
        sys.exit()
        
    # Re-lock the box because it is currently letting us see the third property
    # "0 Items, 0 Stones"
    if len(chests[0].Properties) == 3:
        filter = Items.Filter()
        filter.OnGround = True
        filter.RangeMax = 2
        filter.Graphics = List[Int32]([0x100E]) 
        keys = Items.ApplyFilter(filter)
        key = next(( k for k in keys if chestName in Items.GetPropStringByIndex(k.Serial, 2).lower() ), None  )
        
        Items.UseItem(key)
        Target.WaitForTarget(3000)
        Target.TargetExecute(chests[0])
        Misc.Pause(100)

    Items.UseItem(lockpicks)
    Target.WaitForTarget(3000)
    Target.TargetExecute(chests[0])
    Misc.Pause(3000)
    
    continue 
