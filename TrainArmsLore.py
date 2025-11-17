print("Train Arms Lore")

itemSerial = Target.PromptTarget("Pick an item to lore")
item = Items.FindBySerial(itemSerial)
if item is not None:
    while True:
        Player.UseSkill("Arms Lore")
        Target.WaitForTarget(3000)
        Target.TargetExecute(item)
        Misc.Pause(750)