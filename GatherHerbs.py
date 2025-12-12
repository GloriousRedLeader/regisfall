from System.Collections.Generic import List
from System import Byte, Int32
import sys

Player.HeadMessage(42, "Starting Herb Collector")

HERBS = [
    "A Wild Nightshade Plant",
    "A Wild Mandrake Plant", 
    "A Wild Ginseng Plant", 
    "Graveweed Plant", 
    "A Wild Garlic Plant", 
    "Mountain Sage Plant", 
    "Wild Nettlebloom", 
    "Bloodroot Plant", 
    "0000", 
    "0000", 
]

PAUSE_DELAY_MS = 352

while True:
    while Player.Visible:
    
    
        filter = Items.Filter()
        filter.OnGround = True
        filter.RangeMax = 3
        items = Items.ApplyFilter(filter)
        
        
        for item in items:
            for herb in HERBS:
                if item.Name == herb:
                    Items.UseItem(item)
                    Misc.Pause(PAUSE_DELAY_MS)

        Misc.Pause(PAUSE_DELAY_MS)
        