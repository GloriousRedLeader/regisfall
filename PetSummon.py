
# Context
Gumps.SendAction(0x28, 2001)
Misc.WaitForContext(0x00020561, 10000)

# Mounts
Misc.ContextReply(0x00020561, 2)
Gumps.WaitForGump(0x20, 10000)
Gumps.SendAction(0x20, 101)


Gumps.WaitForGump(0x28, 10000)
Misc.PetRename(0x0001AD7F, "Leopold")