print("Using Axe")
Target.Cancel()
tool = Items.FindByID(0x0F43,0,Player.Backpack.Serial,0)
if tool is not None:
    Items.UseItem(tool)
    