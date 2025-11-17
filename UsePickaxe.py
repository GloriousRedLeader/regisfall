print("Using Pickaxe")
Target.Cancel()
tool = Items.FindByID(0x0E86,0,Player.Backpack.Serial,0)
if tool is not None:
    Items.UseItem(tool)
    