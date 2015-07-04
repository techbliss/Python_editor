Ida Pro python Editor v1

Python language.
Run Scripts within ida.

todo
python autocompletion

I always hated the Old Run script command, so i set up making my own editor for ida pro.

I had to rebuild PyQt4 for ida, so it had all the stuff i needed.

NEW BUILD.

PyQt-win-gpl-4.11.4

https://mega.co.nz/#!TxtTALqa!VgV9IE7QhnvpWUlPakL8DxfjZMu06w-RmFwE4bklZ4I
extract to spesified folder in the archive.

also you have to a newer sip version to get my PyQt4 build to work, the hexray PyQt4 build is years old.

Sip for PyQt4

extract sip archive anywhere, goto root folder, and do.

nmake install

or copy build manuelly.

Download plugin.
extarct to Ida Pro plugins folder.

use hotkey Alt+E and find it under File menu.


