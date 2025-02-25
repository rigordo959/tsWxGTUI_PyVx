# File: ".logs/bmp/README_BMP.txt"
# "Time-stamp: <01/05/2015  2:14:20 AM rsg>"

This "bmp" directory contains those Splash Screen(s) generated by:

  "/tsWxGTUI_Py2x/tsLibGUI/tsWxPkg/src/tsWxGraphicalTextUserInterface.py.

A Splash Screen is displayed during the launch of a GUI-style
application program. It identifies the application`s author(s),
copyright(s) and licence(s) using information defined in:

  "/tsWxGTUI_Py2x/tsLibGUI/tsWxPkg/src/tsWxGlobals.py"

Splash Screens are named for the display size (in character columns and
rows/lines), terminal/emulator type, and host operating system.

  Examples:

          Basic Multi-Color ("wxPython" transformation maps
            68-color palette into 8 or 16 built-in colors)

   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-5.0.bmp"         (Placeholder for
                                                            Windows 2000)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-5.1.bmp"         (Windows XP)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-5.2.bmp"         (Placeholder for
                                                            Windows XP x64)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-6.0.bmp"         (Placeholder for
                                                            Windows Vista)
   "SplashScreen-[60x15_CYGWIN]-cygwin_nt-6.1.bmp"         (Windows 7)
   "SplashScreen-[60x15_LINUX]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[60x15_XTERM]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[80x25_XTERM]-darwin.bmp"                 (Mac OS 10.9.1)
   "SplashScreen-[96x40_XTERM]-linux.bmp"                  (Fedora 21)
   "SplashScreen-[96x40_XTERM]-linux.bmp"                  (Ubuntu 12.04)
   "SplashScreen-[128x50_XTERM]-freebsd.bmp"               (PC-BSD 9.2)
   "SplashScreen-[128x50_XTERM]-sunos.bmp"                 (OpenIndiana 151a8)
   "SplashScreen-[60x15_XTERM-COLOR]-cygwin_nt-6.1.bmp"    (Windows 7)
   "SplashScreen-[80x15_XTERM-16COLOR]-cygwin_nt-6.3.bmp"  (Windows 8.1)
   "SplashScreen-[80x15_XTERM-88COLOR]-cygwin_nt-6.3.bmp"  (16x16 color
                                                            pair limit
                                                            for Windows 8.1)
   "SplashScreen-[80x15_XTERM-256COLOR]-cygwin_nt-6.3.bmp" (16x16 color
                                                            pair limit
                                                            for Windows 8.1)
   "SplashScreen-[80x15_XTERM-256COLOR]-cygwin_nt-6.4.bmp" (16x16 color
                                                            pair limit
                                                            for Windows 10)

      Non-Color ("wxPython" transformation maps 68-color palette
      into black with one shade of the default color for displays
      having only a white, orange or green phosphor).

   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[80x40_VT100]-cygwin_nt-5.0.bmp"          (Placeholder for
                                                            Windows 2000)
   "SplashScreen-[80x40_VT100]-cygwin_nt-5.1.bmp"          (Windows XP)
   "SplashScreen-[80x40_VT100]-cygwin_nt-5.2.bmp"          (Placeholder for
                                                            Windows XP x64)
   "SplashScreen-[80x40_VT100]-cygwin_nt-6.0.bmp"          (Placeholder for
                                                            Windows Vista)
   "SplashScreen-[80x15_VT100]-cygwin_nt-6.1.bmp"          (Windows 7)
   "SplashScreen-[80x15_VT100]-cygwin_nt-6.2.bmp"          (Windows 8)
   "SplashScreen-[80x15_VT220]-cygwin_nt-6.3.bmp"          (Windows 8.1)
   "SplashScreen-[80x15_VT220]-cygwin_nt-6.4.bmp"          (Windows 10)

      #########################################################
      # Advanced Multi-Color support is still evolving....    #
      #                                                       #
      # Terminal/Emulator standards support an undocumented   #
      # maximum of 256 color pairs. This inference resulted   #
      # from the following observations.                      #
      #                                                       #
      # Under Python 2.x and Python 3.x, most xterm-88color   #
      # and xterm-256color terminal emlators produced the     #
      # wrong colors marred by spurious umderline artifacts.  #
      #                                                       #
      # Under Python 3.3.0 with a Yosemite Mac OS X Terminal  #
      # utility, there were 256 color pairs and a 16-color    #
      # palette that worked.                                  #
      #                                                       #
      # Also, under the Python 2.7.6 with the GNOME Desktop   #
      # for CentOS 7.0 Linux, there were 256 color pairs and  #
      # a 16-color palette that worked    .                   #
      #                                                       #
      # For the color pair matrix used by the "tsWxGTUI"      #
      # Toolkit, the Advanced Multi-Color support emulates    #
      # xterm-16color and associated mapping of the wxPython  #
      # 68-color palette into the built-in 16 colors.         #
      #########################################################

   if (COLOR_PAIRS > 256) and       (USE_256_COLOR_PAIR_LIMIT):    # As set in tsWxGlobals.py

      Advanced Multi-Color ("wxPython" emulation maps
      68-color palette into 16 of 88 or 16 of 256 colors)

   elif (COLOR_PAIRS == 256)         # As reported by curses

      Advanced Multi-Color ("wxPython" emulation maps
      68-color palette into 16 of 88 or 16 of 256 colors)

   else:

      Advanced Multi-Color ("wxPython" emulation maps
      68-color palette into 71 of 88 or 140 of 256 colors)

   Base Name     Size    Type   Host OS       File Ext.    Notes
   ------------- -------------- -------------------------  ------------------
   "SplashScreen-[80x15_XTERM-88COLOR]-cygwin_nt-6.3.bmp"  (Windows 8.1)
   "SplashScreen-[80x25_XTERM-88COLOR]-darwin.bmp"         (Mac OS 10.9.1)
   "SplashScreen-[96x40_XTERM-88COLOR]-linux.bmp"          (Fedora 20)
   "SplashScreen-[80x15_XTERM-256COLOR]-cygwin_nt-6.3.bmp" (Windows 8.1)
   "SplashScreen-[80x25_XTERM-256COLOR]-darwin.bmp"        (Mac OS 10.9.1)
   "SplashScreen-[96x40_XTERM-256COLOR]-linux.bmp"         (Fedora 20)

A new Splash Screen is built upon the first use of a uniquely sized
command line interface display by those host operating systems that
share this directory.

  NOTE:

    Previous terminal emulator used in a command line interface shell can
    alter the built-in color palette for subsequect terminal emulators.
    Examples:

    1) The final xterm sees no color palette change if the first one is
       xterm followed by xterm-color, vt100 and xterm.

    2) The final xterm sees a dim color palette change if the first one is
       xterm followed by by xterm-16color, vt100 and xterm.

Keeping a copy here avoids spending time to rebuild the same Splash
Screen each time a GUI-style application program is launched.

You may recover disk space by deleting those Splash Screens that
have outlived their usefulness.
