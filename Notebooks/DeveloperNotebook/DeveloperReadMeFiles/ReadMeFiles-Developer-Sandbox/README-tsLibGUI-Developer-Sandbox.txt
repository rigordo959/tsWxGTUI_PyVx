#-----------------------------------------------------------
#"Time-stamp: <06/24/2015  4:19:38 AM rsg>"
#-----------------------------------------------------------

================= File: README-tsLibGUI.txt ================

   +----+----+  TeamSTARS "tsWxGTUI_PyVx" Toolkit
   | ts | Wx |      with Python 2x & Python 3x based
   +----+----+         Command Line Interface (CLI)
   | G T U I |      and "Curses"-based "wxPython"-style, 
   +---------+         Graphical-Text User Interface (GUI)
 
   Get that cross-platform, pixel-mode "wxPython" feeling
   on character-mode 8-/16-color (xterm-family) & non-color
   (vt100-family) terminals and terminal emulators.

   You can find this and other plain-text files in the
   Toolkit subdirectory named "./DeveloperReadMeFiles".

===================== TABLE OF CONTENTS ====================

1. Package Organization
2. tsWxPkg

=================== PACKAGE ORGANIZATION ===================

1. Package Organization

  The library of building blocks is organized, by the
  functional scope of each component, into a collection of
  "packages". When appropriate, any package may import and
  use the services of any other tsLibGUI package.
 
  Source code is contained in the associated ["src"] sub-
  directory. Depending on its complexity, the source code
  of a package may also be sub-divided and organized into
  a set of one or more source files.
 
  Unit/Integration Test code is contained in the associated
  ["test"] sub-directory. Depending on its complexity, the
  test code of a package may also be sub-divided and organ-
  ized into a set of one or more test files.

========================== tsWxPkg =========================

2. tsWxPkg

   Collection of approximately 100 Classes that use the
   services of the Python Curses module to create a
   character-mode emulation of their pixel-mode "wxPython"
   Class counterparts. The collection includes widgets for
   frames, dialogs, panels, buttons, check boxes, radio
   boxes/buttons and scrollable text windows. It includes
   box and grid sizers. It also includes classes to emulate
   the host operating system theme-based color palette
   management, task bar, mouse click and window focus
   control services used/expected by "wxPython".

   CAUTION: Several classes are barely more than place hold-
            ers. They do not appear in the "tsDemoArchive".

            The ones listed below are not only highly func-
            tional, but have been in use for several years
            and have been enhanced whenever appropriate.

            For details, refer to the modification and to-do
            comments in the source code for the class/module.

   2.1 tsWx.py

       Module to load all symbols that should appear within
       the "wxPython" wx emulation namespace. Included are
       various classes, constants, functions and methods
       available for use by applications built with compo-
       nents from the "wxPython" emulation infrastructure.

   2.2 tsWxGlobals.py

       Module to emulate wxPython configuration constants
       and provide a means for site-specific style defini-
       tions.

       It provides a centralized mechanism for modifying/
       restoring those configuration constants that can be
       interogated at runtime by those software components
       having a "need-to-know". The intent being to avoid
       subsequent searches to locate and modify or restore
       a constant appropriate to the current configuration.

       It also provides a theme-based mechanism for modify-
       ing/restoring those configuration constants as appro-
       priate for various organizations and products.

       ThemeWxPython illustrates the monochrome color scheme
       features of the "wxWidgets" organization and its
       "wxPython" product.

       ThemeTeamSTARS illustrates the multi-color scheme
       features of the "TeamSTARS"/"Software Gadgetry"
       organization and its "tsWxGTUI" Toolkit product.

   2.3 tsWxGraphicalTextUserInterface - Module uses the
       Standard Python Curses API to emulate typical host
       operating system GUI window manager services.

       It initializes, manages and shuts down input (from the
       keyboard and mouse) and output to a two-dimensional
       display screen.

       It captures and logs the initial and run time GUI
       configuration to facilitate troubleshooting.

   2.4 Non-color (vt100 and vt220) - The character-mode
       Graphical-style User Interface emulation is tradi-
       tionally mouseless but new host terminal application
       programs (such as Cygwin's Mintty and Linux's Xterm
       and UDxterm) enable xterm-style mouse input to be
       synthesized.

       Depending on the single phosphor (white, orange,
       green etc.) used in the terminal, this results in the
       rendering of text and shape outlines in "Black"
       (phosphor "OFF") on "White" (phosphor "ON") or
       "White" on "Black" as appropriate for the host
       platform operating system.

       As a consequence, application source code references
       to the 68-color "wxPython" palette are ignored.

   2.5 Curses-style 8-color, 64-color-pair (cygwin, linux,
       xterm and xterm-color) - The character-mode Graph-
       ical-style User Interface emulation supports a mouse
       and maps the 68-color "wxPython" palette into the 8-color or
       16-color "Curses" / "nCurses" palette. This results
       in the rendering of text and shapes with 64 (8x8) or
       256 (16x16) color pairs depending on the operator
       designated terminal emulator.

       Microsoft Windows 2000 with SPK2, when used with Cygwin
       1.7.1, supports only 8-colors but does not support a
       mouse with either the pre-mintty "cygwin" or "xterm"
       terminals. More recent Cygwin releases no longer sup-
       port Microsoft Windows 2000.

   2.6 Curses-style Multi-color (cygwin, linux, xterm,
       xterm-color, xterm-16color) - The character-mode Graph-
       ical-style User Interface emulation supports a mouse
       and maps the 68-color "wxPython" palette into the 8-color or
       16-color "Curses" / "nCurses" palette. This results
       in the rendering of text and shapes with 64 (8x8) or
       256 (16x16) color pairs depending on the operator
       designated terminal emulator.

       Microsoft Windows 2000 with SPK2, when used with Cygwin
       1.7.1, supports only 8-colors but does not support a
       mouse with either the pre-mintty "cygwin" or "xterm"
       terminals. More recent Cygwin releases no longer sup-
       port Microsoft Windows 2000.

   2.7 wxPython-style Multi-color (xterm, xterm-color, xterm-
       16colorxterm-88color and xterm-
       256color)

       The "USE_256_COLOR_PAIR_LIMIT" control option switch
       in the "tsWxGlobals.py" module, when True, also applies
       the xterm-16color palette to the xterm-88color and
       xterm-256color terminal emulators.

       The character-mode Graphical-style User
       Interface emulation supports a mouse and configures
       and initializes the Red-Green-Blue settings for an
       extended 68-color "wxPython" palette. This results
       in the rendering of text and shapes with 5041 (71x71)
       or 19600 (140x140) color pairs depending on the
       operator designated terminal emulator.

   2.8 tsWxEventLoop - Module uses the Standard Python
       Curses API to receive keyboard and mouse events.

       It maps the Curses events into their wxPython
       equivalents.

       It enhances the Standard Python Curses API by:
       scanning the stack of tiled and overlaid wxPython
       GUI objects and identifying the one visible enough
       in the screen position to have triggered the event;
       it dispatches the event to the appropriate "wxPython"-
       style event handler.

   2.9 tsWxMultiFrameEnv - Module to enable an application
       using a Command Line Interface (CLI) to launch and
       use the same character-mode terminal with a Graphi-
       cal-style User Interface (GUI).

       It uses application specified configuration keyword-
       value pair options to initialize any application
       specific logger(s).

       It wraps the CLI, underlying the GUI, and the GUI
       with exception handlers to control the exit codes
       and messages used to coordinate other application
       programs.

   2.10 tsWxPyOnDemandOutputWindow - Module that can be used
       for redirecting Python "stdout" and "stderr" streams.
       It will do nothing until something is written to the
       stream at which point it will write the text to the
       toolkit created "Redirected Output: stdout/stderr"
       frame located just below the application generated
       frames and dialogs, scrolling previous output up
       and off the associated screen area to make room for
       the new output.

   2.11 tsWxTaskBar - Module to create a task icon (button)
       for each top level window (frame, dialog etc.) in a
       toolkit created "Tasks" frame located just below the
       "Redirected Output: stdout/stderr" frame. One or more
       task icons appear within the "Tasks" frame and respond
       to mouse clicks. When the mouse clicks on a task icon,
       the focus for the associated application frame or
       dialog will be raised from background (partially or
       fully hidden) to foreground (fully visible).

   2.12 "wxPython"-style Widgets - Modules to emulate the
       "wxPython"-style frame, dialog, button, checkbox,
       gauge, menu bar, radio box, scroll bar, status bar etc.

   2.13 "wxPython"-style Sizers - Module to emulate the
       "wxPython"-style box and grid sizer, which facili-
       tate the subdivision and layout of display screen
       area.

======================= End-Of-File ========================
