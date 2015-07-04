# Created by: Storm Shadow http://www.techbliss.org

# WARNING! All changes made in this file will be lost!

import re
import idaapi
import idc
from idc import *
from idaapi import *
import idautils

class ripeye(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "Python Editor"
    wanted_name = "Python Editor"
    wanted_hotkey = ""



    def init(self):
        idaapi.msg("Python Editor Is Found GoTo File Menu \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        idaapi.add_menu_item("File/", "Code editor", "Alt-E", 0, self.popeye, ())




    def run(self, arg = 0):
        idaapi.msg("Python Editor Loaded Shortcut Alt+E to Load")

        self.AddMenuElements()

    def popeye(self):
        g = globals()
        idahome = idaapi.idadir("plugins\\Code editor")
        IDAPython_ExecScript(idahome +  "\\pyeditor.py", g)



def PLUGIN_ENTRY():
    return ripeye()