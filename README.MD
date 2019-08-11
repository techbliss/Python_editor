**Ida Pro python Editor**
[![](https://img.shields.io/badge/Twitter--blue.svg?maxAge=2592000)](https://twitter.com/zadow28) ![Python version](https://img.shields.io/badge/python-2.7-brightgreen.svg?maxAge=2592000) ![Python version](https://img.shields.io/badge/Ida-plugin-red.svg?maxAge=2592000) ![PyQ5t](https://img.shields.io/badge/PyQt5-5.6-orange.svg) ![PyQ5t](https://img.shields.io/badge/PyQt4-4.8-yellow.svg)

**what it Does:**
I always hated the Old Run script command, so i set up making my own editor for ida pro.
Just like the ida one but much nicer and better
Python language.
Run Scripts files and apps within ida.


**prerequisites**

ida pro or ida pro demo

PyQt4/or PyQt5 depends on ida pro version.

**It needs Qscilla module(Qsci.pyd), not provided by hex-ray, but found in the links under.**

**Pyqt4 installer**

[Pyqt4](http://www.techbliss.org/threads/pyqt-win-gpl-4-11-qt-4-4-8-7-for-ida-pro-total-package-installer-by-storm-shadow.768/)

**Pyqt5 installer**

[Pyqt5](https://www.techbliss.org/threads/ida-pro-pyqt5-5-6-2-x32-complete-installer-package-by-storm-shadow.909/#post-3114)

[Pyqt5 ida pro 7.0](https://www.techbliss.org/threads/ida-pro-7-0-pyqt5-total-package-by-storm-shadow.950/)

**PyQt5 for 7.2 is shipped within the package**

**IMPORTANT!
you have to take Qt5Core.dll , Qt5Gui.dll, Qt5widgets.dll from PyQt5 package and overwrite the ones in ida pro 7.0 folder**

**build yourself**

```
https://github.com/techbliss/Ida_Pro_Ultimate_Qt_Build_Guide
```


if you need help with this.
Contact me here [Techbliss](http://www.techbliss.org/threads/ida-pro-prebuild-pyqt4-ida-pro_pyqt5-regular-python-2-7x86.683/)



Running other Qt apps within the editor

you have to remember to remove
usually in bottom of Qt file

```
app = QtGui.QApplication(sys.argv)
```
and
```
sys.exit(app.exec_())
```

**Install**

Download plugin.
extract to Ida Pro plugins folder.So its idafolder\plugins\codeeditor
or it wont work

**Tip!**
Use hit hotkey Alt+E twize to load the editor.

**Current Changelog 1.7**
```
Updatetet for ida pro 7.2
```

**Hotkeys**
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



![d](https://cloud.githubusercontent.com/assets/3592375/11515674/4e940c26-987f-11e5-805c-3cbef0069c99.png)


**autocomplete**

![ida](https://cloud.githubusercontent.com/assets/3592375/20944032/3fd0b9e4-bc02-11e6-9072-1c447f935267.png)

**Plugin Manager**

[![Plugin Manager](https://j.gifs.com/gL52pD.gif)](https://www.youtube.com/watch?v=4rB6hddsVs4)

profile code for speed issues

```
    177 function calls in 0.038 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:330(retranslateUi)
        1    0.012    0.012    0.038    0.038 <string>:4(<module>)
        1    0.000    0.000    0.000    0.000 <string>:458(MyWindow)
        9    0.000    0.000    0.000    0.000 <string>:80(_fromUtf8)
        2    0.000    0.000    0.000    0.000 <string>:91(_translate)
        1    0.000    0.000    0.000    0.000 <string>:94(Ui_MainWindow)
        1    0.005    0.005    0.013    0.013 <string>:96(setupUi)
        2    0.000    0.000    0.000    0.000 {built-in method SendScintilla}
       19    0.000    0.000    0.000    0.000 {built-in method addAction}
        1    0.000    0.000    0.000    0.000 {built-in method addPixmap}
       19    0.000    0.000    0.000    0.000 {built-in method addSeparator}
        1    0.000    0.000    0.000    0.000 {built-in method addToolBar}
        1    0.000    0.000    0.000    0.000 {built-in method addWidget}
        1    0.000    0.000    0.000    0.000 {built-in method exec_}
        3    0.006    0.002    0.006    0.002 {built-in method load}
        1    0.000    0.000    0.000    0.000 {built-in method markerDefine}
        1    0.000    0.000    0.000    0.000 {built-in method prepare}
        2    0.000    0.000    0.000    0.000 {built-in method resize}
        1    0.000    0.000    0.000    0.000 {built-in method setAutoCompletionSource}
        3    0.000    0.000    0.000    0.000 {built-in method setAutoCompletionThreshold}
        2    0.000    0.000    0.000    0.000 {built-in method setAutoFillBackground}
        1    0.000    0.000    0.000    0.000 {built-in method setAutoIndent}
        1    0.000    0.000    0.000    0.000 {built-in method setBraceMatching}
        1    0.000    0.000    0.000    0.000 {built-in method setCentralWidget}
        1    0.000    0.000    0.000    0.000 {built-in method setContentsMargins}
        1    0.000    0.000    0.000    0.000 {built-in method setDefaultFont}
        1    0.000    0.000    0.000    0.000 {built-in method setEolFill}
        1    0.000    0.000    0.000    0.000 {built-in method setFamily}
        1    0.000    0.000    0.000    0.000 {built-in method setFixedPitch}
        1    0.000    0.000    0.000    0.000 {built-in method setFont}
        1    0.000    0.000    0.000    0.000 {built-in method setFrameShape}
        1    0.000    0.000    0.000    0.000 {built-in method setIconSize}
        1    0.000    0.000    0.000    0.000 {built-in method setLexer}
        1    0.000    0.000    0.000    0.000 {built-in method setMarginSensitivity}
        1    0.000    0.000    0.000    0.000 {built-in method setMarginWidth}
        1    0.000    0.000    0.000    0.000 {built-in method setMarginsFont}
        1    0.000    0.000    0.000    0.000 {built-in method setMarkerBackgroundColor}
        5    0.000    0.000    0.000    0.000 {built-in method setObjectName}
        1    0.000    0.000    0.000    0.000 {built-in method setPointSize}
       19    0.000    0.000    0.000    0.000 {built-in method setShortcut}
        1    0.000    0.000    0.000    0.000 {built-in method setSpacing}
       19    0.000    0.000    0.000    0.000 {built-in method setStatusTip}
        1    0.000    0.000    0.000    0.000 {built-in method setStyleSheet}
        1    0.000    0.000    0.000    0.000 {built-in method setTabWidth}
        1    0.000    0.000    0.000    0.000 {built-in method setToolButtonStyle}
        1    0.000    0.000    0.000    0.000 {built-in method setToolTip}
        1    0.000    0.000    0.000    0.000 {built-in method setWhatsThis}
        1    0.000    0.000    0.000    0.000 {built-in method setWindowIcon}
        2    0.000    0.000    0.000    0.000 {built-in method setWindowTitle}
        1    0.013    0.013    0.013    0.013 {built-in method show}
        1    0.000    0.000    0.000    0.000 {built-in method width}
        1    0.001    0.001    0.001    0.001 {connectSlotsByName}
        2    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 {instance}
       20    0.000    0.000    0.000    0.000 {method 'connect' of 'PyQt5.QtCore.pyqtBoundSignal' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {nt.getcwd}
        2    0.000    0.000    0.000    0.000 {setAttribute}
        2    0.000    0.000    0.000    0.000 {translate}```







