from Rectangle import *

class Format:
    def __init__(self, arr):
        self.arr = arr

    def spawn(self, team=1, angles = DEF_POINT):
        txt = ""
        for i in range(len(self.arr)):
            txt += str((f"\n{{\n"
                        f"\"classname\" \"gametype_player\"\n"
                        f"\"spawnflags\" \"{team}\"\n"
                        f"\"origin\" {self.arr[i].toString()}\n"
                        f"\"angles\" {angles.toString()}\n"
                        f"}}"))
        return txt

    def booster(self, up=800, forward=200, angle=0):
        txt = ""
        for i in range(len(self.arr)):
            txt += str((f"\n{{\n"
                        f"\"classname\" \"booster\"\n"
                        f"\"up\" \"{up}\"\n"
                        f"\"forward\" \"{forward}\"\n"
                        f"\"angle\" \"{angle}\"\n"
                        f"\"origin\" {self.arr[i].toString()}\n"
                        f"}}"))
        return txt

    def accelerator(self, angles=DEF_POINT, speed=800):
        txt = ""
        for i in range(len(self.arr)):
            txt += str((f"\n{{\n"
                        f"\"classname\" \"accelerator\"\n"
                        f"\"speed\" \"{speed}\"\n"
                        f"\"origin\" {self.arr[i].toString()}\n"
                        f"\"angles\" {angles.toString()}\n"
                        f"}}"))
        return txt

    def bspmodel(self, instance='instances/colombia/npc_jump1', angles=DEF_POINT):
        txt = ""
        for i in range(len(self.arr)):
            txt += str((f"\n{{\n"
                    f"\"classname\" \"misc_bsp\"\n"
                    f"\"bspmodel\" \"{instance}\"\n"
                    f"\"origin\" {self.arr[i].toString()}\n"
                    f"\"angles\" {angles.toString()}\n"
                    f"}}"))
        return txt


    def button(self, modelNum=0, angle=DEF_POINT, target="target1", health=1, damage=1000):
        txt = ""
        for i in range(len(self.arr)):
            txt += str((f"\n{{\n"
                        f"\"classname\" \"func_button\"\n"
                        f"\"model\" \"{modelNum}\"\n"
                        f"\"origin\" {self.arr[i].toString()}\n"
                        f"\"angle\" {angle.toString()}\n"
                        f"\"target\" \"{target}\"\n"
                        f"\"health\" \"{health}\"\n"
                        f"\"damage\" \"{damage}\"\n"
                        f"}}"))
        return txt

    def door(self, modelNum=0, angle=-1, targetname="target1", speed=1, lip=800, damage=1000, wait=2):
        txt = ""
        for i in range(len(self.arr)):
            txt += str((f"\n{{\n"
                        f"\"classname\" \"func_door\"\n"
                        f"\"model\" \"{modelNum}\"\n"
                        f"\"origin\" {self.arr[i].toString()}\n"
                        f"\"angle\" {angle}\n"
                        f"\"targetname\" \"{targetname}\"\n"
                        f"\"speed\" \"{speed}\"\n"
                        f"\"lip\" \"{lip}\""
                        f"\"damage\" \"{damage}\"\n"
                        f"\"wait\" \"{wait}\"\n"
                        f"}}"))
        return txt
