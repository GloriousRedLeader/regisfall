print("Train Detecting Hidden")

from System.Collections.Generic import List
from System import Byte, Int32
import sys
    
while Player.GetSkillValue("Detecting Hidden") < Player.GetSkillCap("Detecting Hidden"):
    Player.UseSkill("Detecting Hidden")
    Target.WaitForTarget(3000)
    Target.TargetExecute(Player.Serial)
    Misc.Pause(4000)
