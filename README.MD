Ida Pro python Editor v2

what it Does:
Just like the ida one but much nicer and better
Python language.
Run Scripts within ida.



todo
python auto completion  CHECK
better path recognition


I always hated the Old Run script command, so i set up making my own editor for ida pro.

I had to rebuild PyQt4 for ida, so it had all the stuff i needed.

NEW BUILD.

PyQt-win-gpl-4.11.4

[https://mega.co.nz/#!TxtTALqa!VgV9IE7QhnvpWUlPakL8DxfjZMu06w-RmFwE4bklZ4I]


extract to specified folder in the archive.

Also you have to a newer sip version to get my PyQt4 build to work, the hexray PyQt4 build is years old.

Sip for PyQt4
sip 4.16.4

[https://mega.co.nz/#!i81kFQRR!hrg_1MsIJoojrP6c8vfvSWaaqiBbyjcjFhHmuJ43N9U]


Extract sip archive anywhere, goto root folder, and do.

name install

or copy build manually.

if you need help with this.
Contact me here [http://www.techbliss.org/threads/ida-pro-prebuild-pyqt4-ida-pro_pyqt5-regular-python-2-7x86.683/]




Download plugin.
extract to Ida Pro plugins folder.

use hotkey twice Alt+E and find it under File menu.



Changelog v2
Totaly new interface.

<pre>
1. Hotkeys:
2.  NewFile:            Ctrl+N
3.  OpenFile:           Ctrl+O
4.  SaveFile:           Ctrl+S
5.  RunScript:          Ctrl+E
6.  Undo:               Ctrl+Z
7.  Redo:               Ctrl+Y
8.  SelectALL:          Ctrl+A
9.  Paste:              Ctrl+V
10. ResetFolding:       Ctrl+R
11. CircleFolding:      Ctrl+C
12. PlainFolding:       Ctrl+P
13. Hex-ray Home:       Ctrl+W
14. Python API:         Ctrl+I
15. Open git python:    Ctrl+G
16. Author:             Ctrl+B</pre>


Tip!
Use hit hotkey Alt+E twize to load the editor.

![vdpqq](https://cloud.githubusercontent.com/assets/3592375/8509437/f6b4b458-22a2-11e5-9e45-16ea23bb5c5e.jpg)


