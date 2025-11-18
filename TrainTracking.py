print("Train Tracking")

from System.Collections.Generic import List
from System import Byte, Int32
import sys
    
TRACKING_GUMP_ID = 2
TRACK_PLAYERS_GUMP_ID = 7

while Player.GetSkillValue("Tracking") < Player.GetSkillCap("Tracking"):
    Player.UseSkill("Tracking")
    Gumps.WaitForGump(TRACKING_GUMP_ID, 3000)
    Gumps.SendAction(TRACKING_GUMP_ID, 4)
    Gumps.WaitForGump(TRACK_PLAYERS_GUMP_ID, 3000)
    Gumps.CloseGump(TRACK_PLAYERS_GUMP_ID)
    Misc.Pause(4000)
