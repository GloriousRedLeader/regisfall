Player.HeadMessage(42, "Apply Poison to Weapon")

from System import Byte, Int32
from System.Collections.Generic import List
import sys
import time

kryss = Player.GetItemOnLayer("RightHand")

if kryss is None:
    kryss = Player.GetItemOnLayer("LeftHand")

if kryss is None:
    print("No weapon found")
    sys.exit()
    
#print(Items.GetPropValue(kryss, "Greater Poison Charges"))
#sys.exit()    
poison = Items.FindByID(0x0F0A, 0, Player.Backpack.Serial, 0)
if poison is None:
    print("No poison found")
    sys.exit()
    
Player.UseSkill("Poisoning")
Target.WaitForTarget(3000)
Target.TargetExecute(poison)
Target.WaitForTarget(3000)
Target.TargetExecute(kryss)
sys.exit()
    
for p in Items.GetProperties(kryss.Serial, 3000):
    print(p)
    
print("*************************")
for p in kryss.Properties:
    print(p)
    
print("*************************")
print("*************************")
for p in Items.GetPropStringList(kryss.Serial):
    print(p)
    
    
print("*************************")
print("*************************")
print(Items.GetPropValue(kryss, "regular poison charges"))