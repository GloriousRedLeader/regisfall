import sys
from System.Collections.Generic import List
from System import Byte, Int32
import re
import os

Player.QuestButton()

sys.exit()


for i in range(1, 20):
    Player.ChatEmote(0, ": hey")
    #Player.EmoteAction("hey")
    #Player.ChatSay(": hey")
    #Player.ChatEmote(-1, "hey")
    Misc.Pause(2000)

sys.exit()


c123 = 0x40F71F41 
c125 = 0x40251A02
container = Items.FindBySerial(c125)
print(container.Contains.Count)

sys.exit()

def test():

    script_name = os.path.basename(__file__)
    print(script_name)
    #rune = int(re.search(r"RecallOrSacredJourneyRune(\d+)\.py", script_name).group(1))


#test()

sys.exit()

has = Player.BuffsExist("Blood Oath")
print(has)


sys.exit()

while True:
    
    Spells.Cast("Create Food")
    Misc.Pause(1500)
    
    
sys.exit()
def get_friends_by_names (friendNames = [], range = 8):
    fil = Mobiles.Filter()
    fil.Enabled = True
    fil.RangeMax = range
    fil.Notorieties = List[Byte](bytes([1, 2]))
    fil.IsGhost = False
    fil.Friend = False
    fil.CheckLineOfSight = True
    mobs = Mobiles.ApplyFilter(fil)

    #listValid = [m.Serial for m in mobs if m.Name in friendNames]

    if len(mobs) > 0:
        mobsList = List[type(mobs[0])]([mob for mob in mobs if mob.Name in friendNames])
        return mobsList    

for f in get_friends_by_names (friendNames = ["omg artie", "omg arturo"], range = 8):
    print(f.Name)
sys.exit()



# Number of times to beep and flash a message
HOW_MANY_TIMES_TO_BEEP = 5

# If you want a pulse just to let you know this script is running
# this is the number of milliseconds to remind you it is running.
# Set to a really high number if you do not want to deal with it.
HOW_OFTEN_TO_PING_MS = 5000

# Anything matching these strings will alert
STRINGS_TO_LOOK_FOR = [
    "The Master of the Hunt has",
    "You sense a dark presence",
    "a putrid steed",
    "a venom steed",
    "an inferno steed",
    "a blazing steed",
    "Barton"
]

Timer.Create( 'journalAlertPingTimer', 1 )

Journal.Clear()
while True:
    
    if Timer.Check( 'journalAlertPingTimer' ) == False:
        Player.HeadMessage( 58, "Journal Alert Running...")
        Timer.Create( 'journalAlertPingTimer', HOW_OFTEN_TO_PING_MS )
    
    for search in STRINGS_TO_LOOK_FOR:
        if Journal.Search(search):
            found = Journal.GetLineText(search,False)
            Journal.Clear()
            for i in range(0, HOW_MANY_TIMES_TO_BEEP):
                Misc.Beep()
                Player.HeadMessage( 28, "^^ Journal Alert: {} ^^".format(found) )
                Player.HeadMessage( 48, "^^ Journal Alert: {} ^^".format(found) )
                Misc.Pause(1000) 

    Misc.Pause(1000) 

sys.exit()

# Add ItemIDs here (NOT Serials). Use razor to inspect the items. Look for ItemID.
# You can add many different ItemIDs - or just a single one like below.
thingsToClick = [
    0x0E7C, # CUB Chest
]

while True:
    filter = Items.Filter()
    filter.Movable = 0
    filter.OnGround = True
    filter.RangeMax = 2
    items = Items.ApplyFilter(filter)

    for item in items:
        if item.ItemID in thingsToClick:
            Items.UseItem(item)
            Misc.Pause(750)

    Misc.Pause(750)

sys.exit()


#from Scripts.omgarturo.fm_core.core_mobiles import get_enemies
#from Scripts.omgarturo.fm_core.core_mobiles import get_pets
#from Scripts.omgarturo.fm_core.core_player import move_all_items_from_container
#from Scripts.omgarturo.fm_core.core_items import AXE_STATIC_IDS, LOG_STATIC_IDS, TREE_STATIC_IDS
#from Scripts.omgarturo.fm_core.core_player import find_in_container_by_id
#from Scripts.omgarturo.fm_core.core_player import move_item_to_container
#from Scripts.omgarturo.fm_core.core_spells import get_fc_delay
#from Scripts.omgarturo.fm_core.core_spells import SUMMON_FAMILIAR_DELAY
#from Scripts.omgarturo.fm_core.core_spells import FC_CAP_NECROMANCY
#from Scripts.omgarturo.fm_core.core_rails import go_to_tile
#from Scripts.omgarturo.fm_core.core_items import get_corpses
#from Scripts.omgarturo.fm_core.core_rails import get_tile_in_front

from System.Collections.Generic import List
from System import Byte, Int32
#from Scripts.omgarturo.fm_core.core_items import BOD_STATIC_ID
#from Scripts.omgarturo.fm_core.core_items import BOD_BOOK_STATIC_ID

#from System.Collections.Generic import List
import sys
#from System import Byte, Int32
#import time
import re
#import os


#https://github.com/matsamilla/Razor-Enhanced/blob/master/NoxBodFiles/Smithbodgod.py

# This stuff is used to detect keypresses like mouse for movement
#import ctypes
#from ctypes import wintypes
#user32 = ctypes.WinDLL('user32', use_last_error=True)
#user32.GetAsyncKeyState.restype = wintypes.SHORT
#user32.GetAsyncKeyState.argtypes = [wintypes.INT]

from Scripts.omgarturo.fm_core.core_player import find_first_in_container_by_ids

from Scripts.omgarturo.fm_core.core_items import BOD_STATIC_ID
from Scripts.omgarturo.fm_core.core_items import BOD_BOOK_STATIC_ID

from Scripts.omgarturo.fm_core.core_items import INGOT_STATIC_IDS
from Scripts.omgarturo.fm_core.core_items import RESOURCE_HUE_DEFAULT
from Scripts.omgarturo.fm_core.core_items import GINSENG
from Scripts.omgarturo.fm_core.core_crafting import RECIPES, parse_large_bod, parse_small_bod

myPetSerial = 0x000EA1F0
#for item in Items.FindBySerial(Mobiles.FindBySerial(myPetSerial).Backpack.Serial).Contains:
for item in Mobiles.FindBySerial(myPetSerial).Backpack.Contains:
    print(item.Name)
    



sys.exit()


card =  Items.FindAllByID(0x9C14,0x0491,Player.Backpack.Serial, 0).pop()

print(card)

sys.exit()


Items.UseItem(0x4172B870)

sys.exit()

print("hello")

while True:
    Player.ChatSay("forward")
    Misc.Pause(3000)


item = Items.FindBySerial(0x40FE0F85)
if "confusion blast" in item.Name.lower():
    print("its in!!!")
for prop in item.Properties:
        print("\t", prop.ToString(), "(", prop.Number, ")")  

sys.exit()

PROD_ID_LARGE_BULK_ORDER = 1060655
PROP_ID_SMALL_BULK_ORDER = 1060654 
PROP_ID_AMOUNT_TO_MAKE = 1060656
PROP_ID_BOD_EXCEPTIONAL = 1045141
PROP_ID_ITEM_TEXT = 1060658
PROP_ID_ITEM_EXCEPTIONAL = 1060636

containers = [0x40110D39, 0x400D7BB0]

large = []
names = []
for container in containers:
    bods = Items.FindAllByID(BOD_STATIC_ID, -1, container, 1)
    for bod in bods:
        tmpNames = []
        isLargeBod = False
        for prop in bod.Properties:
            # large
            if prop.Number == PROD_ID_LARGE_BULK_ORDER:
                isLargeBod = True
            
            if prop.Number in range(PROP_ID_ITEM_TEXT, PROP_ID_ITEM_TEXT + 6):    
                propList = prop.ToString().split(": ")
                recipeName = propList[0].strip() # buckler looks like "buckler : <amount>" instead of "buckler: <amount>"
                names.append(recipeName)
                tmpNames.append(recipeName)
                #amountMade = int(propList[1])
                #smallBodItems.append({ "name": recipeName, "amountMade": amountMade })
        if isLargeBod:
            for tmpName in tmpNames:
                large.append(tmpName)

names = set(names) 
large = set(large)

hasRecipes = []
for name in names:
    for recipe in RECIPES:
        if recipe.recipeName == name:
            hasRecipes.append(name)

            
noRecipes = list(names - set(hasRecipes))
#for name in names:
#    print("\tomg: ", name)

i = 1
for noRecipe in noRecipes:
    isPartOfLarge = "YES" if noRecipe in large else "NO"
    print("\t#{}\t{}\t{}".format(i, isPartOfLarge, noRecipe))
    i = i + 1

print(" ")    
print("Has Recipe: {}".format(len(hasRecipes)))    
print("No Recipe: {}".format(len(noRecipes)))
print("Total {}".format(len(names)))
    

#i = 2
#for x in range(2, 500):
#    if x % 7 == 0:
#        print(x + 2)

sys.exit()

FIRE_BEETLE_MOBILE_ID = 0x00A9
BLUE_BEETLE_MOBILE_ID = 0x0317

pets = []
fil = Mobiles.Filter()
fil.Bodies = List[Int32]([BLUE_BEETLE_MOBILE_ID, FIRE_BEETLE_MOBILE_ID])
fil.Enabled = True
fil.RangeMax = 5
fil.Notorieties = List[Byte](bytes([1, 2]))
fil.IsGhost = False
fil.Friend = False
fil.CheckLineOfSight = True
blues = Mobiles.ApplyFilter(fil)    
for blue in blues:
    if blue.CanRename:
        pets.append(blue)


for pet in pets:
    print(pet.Name, hex(pet.MobileID))
sys.exit()

print("BLUE BEETLE")
BLUE_BEETLE = 0x000EA1F0
mobile = Mobiles.FindBySerial(BLUE_BEETLE)
for prop in mobile.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")") 
print("Backpack", mobile.Backpack.Contains)    
print("Size of backpack", len(mobile.Backpack.Contains))
print("Weight of backpack", mobile.Backpack.Weight)


print("FIRE BEETLE")
FIRE_BEETLE = 0x0003FE96
mobile = Mobiles.FindBySerial(FIRE_BEETLE)
for prop in mobile.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")") 
print("Backpack", mobile.Backpack.Contains)    
print("Size of backpack", len(mobile.Backpack.Contains))
print("Weight of backpack", mobile.Backpack.Weight)
    
sys.exit()

item = Items.FindBySerial(0x40B76767)
for prop in item.Properties:
        print("\t", prop.ToString(), "(", prop.Number, ")")  

sys.exit()

staff = Items.FindByName("oak gnarled staff", -1, 0x406766F0,0)
print(staff)

sys.exit()

PROP_ID_ITEM_EXCEPTIONAL = 1060636
PROP_ID_EXCEPTIONAL = 1045141
PROP_ID_ITEM_TEXT = 1060658

#i = Items.FindByName("confusion blast", -1, 0x406766F0, 0)
#print(i)
#if i is not None:
#    print("HSDFSD")
items = Items.FindBySerial(0x406766F0).Contains
for item in items:
    print(item.Name)
    for prop in item.Properties:
            print("\t", prop.ToString(), "(", prop.Number, ")")    
    #if any(prop.Number == PROP_ID_ITEM_EXCEPTIONAL for prop in item.Properties):
    #    print("Exceptional {}".format(item.Name))
    #print(Items.GetPropStringByIndex(item,1))
    #print(item.Name, "(", item.Amount, ")")
    #if "confusion blast".lower() in item.Name.lower() and item.Amount > 1:
    #    print("\tSplitting stack of {} ({})".format("Greater Poison potion", item.Amount))
        #Items.Move(source,destination,amount,x,y)
        #x = item.Position.X + 1 if item.Position.X < 50 else item.Position.X - 1
        #Items.Move(item, 0x406766F0, 1, item.Position.Y, x)
        #Items.Move(item, 0x406766F0, 1, item.Position.X, item.Position.Y)
        
sys.exit()

#recipes = map(lambda recipe: recipe.itemName, RECIPES)
item = Items.FindByName("corpse skin", -1, Player.Backpack.Serial, 0)
print(item)

sys.exit()


while True:
    Player.ChatSay("forward")
    Misc.Pause(3000)


smallBodItems = [
    { "name": "food", "crane": 1 },
    { "name": "dogs", "crane": 2 },
    { "name": "cats", "crane": 3 },
    
]

part1 = "|".join(sorted(list(map(lambda smallBodItem: smallBodItem["name"], smallBodItems))))
print(part1)

sys.exit()
item = Items.FindByID(GINSENG, RESOURCE_HUE_DEFAULT, 0x408CC21E, -1)
print(item)
sys.exit()

print("Clumsy (scroll)")
item = Items.FindBySerial(0x404ED3E2)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")
    
print("Greater Confusion Blast potion (potion)")
item = Items.FindBySerial(0x404E79AB)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")

print("Lesser Poison potion (potion)")
item = Items.FindBySerial(0x40FDB01C)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")
    
print("Greater Heal potion (bod)")
item = Items.FindBySerial(0x404E6A32)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")
    
print("Greater Heal potion (potion)")
item = Items.FindBySerial(0x404E7253)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")    
    

    
print("Leather Sleeves")
item = Items.FindBySerial(0x404B10EE)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")    
    
sys.exit()

PROP_ID_ITEM_TEXT = 1060658
l = range(PROP_ID_ITEM_TEXT, PROP_ID_ITEM_TEXT + 4)

print(PROP_ID_ITEM_TEXT + 4)
if 1060662  in range(PROP_ID_ITEM_TEXT, PROP_ID_ITEM_TEXT + 4):
    print("YES")
else:
    print("no")
print(l)
#if prop.Number in range(PROP_ID_ITEM_TEXT, PROP_ID_ITEM_TEXT + 4):    



sys.exit()


MACE_STATIC_ID = 0x0F5C
ALL_CRAFTED_ITEM_IDS = [MACE_STATIC_ID]

Player.HeadMessage(455, "start")

LBOD = 0x403935EA
SBOD = 0x4038EA7F

print("Large with 5")
item = Items.FindBySerial(0x403ECDF4)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")

print("Large")
item = Items.FindBySerial(LBOD)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")
    
print("Small")
item = Items.FindBySerial(SBOD)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")  
  
print("Small")
item = Items.FindBySerial(0x40393676)
for prop in item.Properties:
    print("\t", prop.ToString(), "(", prop.Number, ")")     
    
    #if prop.ToString() == "exceptional":
    #    print("YAY")

sys.exit()


#Items.Move(0x40899FB1, 0x406766F0, 0)
Misc.WaitForContext(0x400E972D, 10000)
Misc.ContextReply(0x400E972D, 2) # all
Misc.WaitForContext(0x400E972D, 10000)
Misc.ContextReply(0x400E972D, 1) # cloth

Misc.WaitForContext(0x400E972D, 10000)
Misc.ContextReply(0x400E972D, 0) # ingots