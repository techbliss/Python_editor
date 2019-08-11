# Created by: Storm Shadow http://www.techbliss.org
import os, sys
import ida_idaapi, ida_kernwin, ida_idaapi, ida_loader
import idc
from idc import *
from ida_diskio import *
from ida_idaapi import *
from ida_loader import *
import sys
sys.path.insert(0 , ida_diskio.idadir("plugins\\Code editor\\icons"))
import ico
from ico import *

PLUGIN_VERSION = "1.6"
IDAVERISONS    = "IDA PRO 7.2+"
AUTHORS        = "Storm Shadow"
DATE           = "2019"
TWITTER        = "Twitter @zadow28"

def banner():
    banner_options = (PLUGIN_VERSION, AUTHORS, DATE, TWITTER, IDAVERISONS)
    banner_titles = "Python Editor v%s - (c) %s - %s - %s - %s" % banner_options

# print plugin banner
    print("---[" + banner_titles + "]---\n")

banner()

# 1) Create the handler class
class MyEditorHandler(ida_kernwin.action_handler_t):
    def __init__(self):
        ida_kernwin.action_handler_t.__init__(self)

    # Run editor when invoked.
    def activate(self, ctx):
        g = globals()
        idahome = ida_diskio.idadir("plugins\\Code editor")
        tupac = str(idahome + "\\pyeditor.py")
        ida_kernwin.load_custom_icon(":/ico/python.png")
        load_and_run_plugin(tupac, True)
    def update(self, ctx):
        return ida_kernwin.AST_ENABLE_ALWAYS

class ripeye(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_FIX
    comment = "Run me"
    help = "Python Editor"
    wanted_name = "Python Editor"
    wanted_hotkey = "" #the tooltip horkey goes away when setting it here DONT DO it! and only is shown in File/Plugins menu


    def editor_menuaction(self):
        action_desc = ida_kernwin.action_desc_t(
            'my:editoraction',  # The action name. This acts like an ID and must be unique
            'Python Editor!',  # The action text.
            MyEditorHandler(),  # The action handler.
            'Ctrl+H',  # Optional: the action shortcut DO IT  HERE!
            'Script editor',  # Optional: the action tooltip (available in menus/toolbar)
            ida_kernwin.load_custom_icon(":/ico/python.png")  # hackish load action icon , if no custom icon use number from 1-150 from internal ida
        )

        # 3) Register the action
        ida_kernwin.register_action(action_desc)

        ida_kernwin.attach_action_to_menu(
            'Edit/Editor...',  # The relative path of where to add the action
            'my:editoraction',  # The action ID (see above)
            ida_kernwin.SETMENU_APP)  # We want to append the action after the 'Manual instruction...

        form = ida_kernwin.get_current_tform()
        ida_kernwin.attach_action_to_popup(form, None, "my:editoraction", None)

    def init(self):
        """
        This is called by IDA when it is loading the plugin.
        """
        #self._icon_id_file = ida_diskio.BADADDR
        # attempt plugin initialization
        try:
            self._install_plugin()

        # failed to initialize or integrate the plugin, log and skip loading
        except Exception as e:
            form = ida_kernwin.get_current_tform()
            pass

        return PLUGIN_KEEP


    def _install_plugin(self):
        """
        Initialize & integrate the plugin into IDA.
        """
        self.editor_menuaction()
        self._init()

    def term(self):
        pass

    def run(self, arg = 0):
        #we need the calls again if we wanna load it via File/Plugins/editor
        ida_kernwin.msg("Python Editor Loaded to menu \n use Alt+E hot key to quick load ")
        hackish = MyEditorHandler()
        hackish.activate(self)

def PLUGIN_ENTRY():
    return ripeye()