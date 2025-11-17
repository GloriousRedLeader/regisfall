print("Attempts to unlock nearby chest")

from System.Collections.Generic import List
from System import Byte, Int32
import sys

texts = Journal.GetTextByType("System")
for text in texts:
    print(text)
    
sys.exit()

while True:
    Journal.Clear()
    
    Misc.Pause(5000)
    print(Journal.SearchByType("You dig some iron", "System"))
    
    
    
#texts = Journal.GetTextByType("System")
#print(Journal.SearchByType("This does not", "System"))

#for text in texts:
#    print(text)
    

#sys.exit()

    
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
    
    print(chests[0].Name)

    lockpicks = Items.FindByID(0x14FC,0,Player.Backpack.Serial,0)
    if lockpicks is None:
        print("Not enough lockpicks")
        sys.exit()
    
    
    Items.UseItem(lockpicks)
    Target.WaitForTarget(3000)
    Target.TargetExecute(chests[0])   
    #if Journal.Search("This does not appear"):
    if Journal.SearchByType("This does not appear", "System"):
        print("NOT LOCKED")
    else:
        print("Locked")

    
    print("Waiting")
    Misc.Pause(5000)
