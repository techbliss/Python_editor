**Ida Pro python Editor v4**
[![](https://img.shields.io/badge/Twitter--blue.svg?maxAge=2592000)](https://twitter.com/zadow28) ![Python version](https://img.shields.io/badge/python-2.7-brightgreen.svg?maxAge=2592000) ![Python version](https://img.shields.io/badge/Ida-plugin-red.svg?maxAge=2592000)

**what it Does:**
I always hated the Old Run script command, so i set up making my own editor for ida pro.
Just like the ida one but much nicer and better
Python language.
Run Scripts within ida.
now examples script are working.

**API:**
If you run the app strait in windows there is code recognition.
api from ida dont works as yet!


**todo**
Debugger
I had to rebuild PyQt4 for ida, so it had all the stuff i needed.
Either download complete package here
```
http://www.techbliss.org/threads/pyqt-win-gpl-4-11-qt-4-4-8-7-for-ida-pro-total-package-installer-by-storm-shadow.768/
```

build yourself

```
https://github.com/techbliss/Ida_Pro_Ultimate_Qt_Build_Guide
```

or copy supplied Qsci.pyd in

```
C:\Python27\Lib\site-packages\PyQt4
```

if you need help with this.
Contact me here [Techbliss](http://www.techbliss.org/threads/ida-pro-prebuild-pyqt4-ida-pro_pyqt5-regular-python-2-7x86.683/)



Runing other Qt apps within the editor

you have to remmeber to remove
usually in buttom of Qt file
```
app = QtGui.QApplication(sys.argv)
```
and
```
sys.exit(app.exec_())
```


Download plugin.
extract to Ida Pro plugins folder.So its idafolder\plugins\codeeditor
or it wont work

Tip!
Use hit hotkey Alt+E twize to load the editor.


**Changelog v4**
```
Clean up code
Zoom -/+
Font box
Getting redy for debugger feature
```

**Changelog v3**
```
APi working
better path recognition
apit on/off toggle
run full python programs.
```

```
 ###################################################
 #              Author Storm Shadow                # 
 #                   Hotkeys                       # 
 #         NewFile:            Ctrl+N              #
 #         OpenFile:           Ctrl+O              #
 #         SaveFile:           Ctrl+S              #
 #         RunScript:          Ctrl+E              #
 #         Undo:               Ctrl+Z              #
 #         Redo:               Ctrl+Y              #
 #         SelectALL:          Ctrl+A              #
 #         Paste:              Ctrl+V              #
 #         Font:               Ctrl+F              #
 #         ResetFolding:       Ctrl+R              #
 #         CircleFolding:      Ctrl+C              #
 #         PlainFolding:       Ctrl+P              #
 #         HEX-ray Home:       Ctrl+W              #
 #         Ida Pro Python SDK  Ctrl+I              #
 #         IDAPROPythonGit:    Ctrl+G              #
 #         Author:             Ctrl+B              #
 #         Enable Reg:         Alt+E               #
 #         Disable Reg:        Alt+D               #
 #         Zoom in             Ctrl+Shift+ +       #
 #         Zoom Out            Ctrl+Shift+ -       #
 #         Profile Code        Ctrl+Shift+ E       #
 ###################################################
 #              IDA PRO python Editor              #
 ###################################################
```






![v2](https://cloud.githubusercontent.com/assets/3592375/8766467/26a85fe2-2e39-11e5-9c75-a97259a7a7ad.png)



![d](https://cloud.githubusercontent.com/assets/3592375/11515674/4e940c26-987f-11e5-805c-3cbef0069c99.png)







