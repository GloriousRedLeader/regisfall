print("Using Lockpick")

lockpicks = Items.FindByID(0x14FC,0,Player.Backpack.Serial,0)
if lockpicks is not None:
    Items.UseItem(lockpicks)
    