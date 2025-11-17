import time

# Plug in a serial of a monster or ideally an alt to attack
ALT_CHAR_SERIAL_TO_ATTACK = 0x0001964A

Player.HeadMessage(455, "start fc test")

HAS_PROTECTION = Player.BuffsExist("Protection")
FC_VAL = Player.FasterCasting
for i in range(0 , 10):
    Target.Cancel()
    Misc.Pause(2000)
    start = time.time()
    Spells.CastMagery("Energy Bolt")
    Target.WaitForTarget(5000)
    Target.TargetExecute(0x0001964A)
    total = time.time() - start
    print("number", i, "fc", FC_VAL, "protection", HAS_PROTECTION, "total", total)