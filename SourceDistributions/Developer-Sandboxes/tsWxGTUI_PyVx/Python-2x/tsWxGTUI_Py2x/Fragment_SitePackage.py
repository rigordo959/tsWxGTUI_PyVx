#!/usr/bin/env python
#
__doc__ = '''
This file demonstrates the import sequence for building block components 
of the TeamSTARS "tsWxGTUI_PyVx" Toolkit:

    1st stage (required) --- Command Line Interface (CLI) Library
    2nd stage  (optioal) --- Graphical-style User Interface (GUI) Library
    3rd stage (launcher) --- tsCommandLineEnv or tsWxMultiFrameEnv
'''

separator = '''
-------------------------------------------------------------------------
'''

import sys

YourApplicationName = sys.argv[0]

__title__ = YourApplicationName

print('%s' % separator)

print('\n\n__title__=%s' % __title__)
print('\n\n__doc__=%s' % __doc__)

print('%s' % separator)

# Python-based CLI Mode
try:

    CLImode = True
    print('\n\nCLImode=%s' % CLImode)

    # from tsWxGTUI_Py2x import tsLibCLI
    # print('\n\ntsLibCLI: %s' % dir(tsLibCLI))

    from tsWxGTUI_Py2x.tsLibCLI import tsExceptions as tse
    print('\n\ntse: %s' % dir(tse))

    from tsWxGTUI_Py2x.tsLibCLI import tsLogger as Logger
    print('\n\nLogger: %s' % dir(Logger))

    from tsWxGTUI_Py2x.tsLibCLI import tsOperatorSettingsParser
    print('\n\ntsOperatorSettingsParser: %s' % dir(tsOperatorSettingsParser))

    from tsWxGTUI_Py2x.tsLibCLI import tsDoubleLinkedList
    print('\n\ntsDoubleLinkedList: %s' % dir(tsDoubleLinkedList))

    from tsDoubleLinkedList \
         import DoubleLinkedList
    print('\n\nDoubleLinkedList: %s' % dir(DoubleLinkedList))

    if CLImode:

        from tsWxGTUI_Py2x.tsLibCLI import tsCommandLineEnv
        print('\n\ntsCommandLineEnv: %s' % dir(tsCommandLineEnv))
        from tsCommandLineEnv \
             import CommandLineEnv

        print('\n\nCommandLineEnv: %s' % dir(CommandLineEnv))

except ImportError, importCode:

    CLImode = False
    print('\n\nCLImode=%s' % CLImode)

    fmt1 = '%s: ImportError ' % str(__title__)
    fmt2 = '(tsLibCLI); '
    fmt3 = 'importCode=%s' % str(importCode)
    msg = fmt1 + fmt2 + fmt3

    print(msg)

    raise tse.PROGRAM_EXCEPTION(
      tse.APPLICATION_TRAP,
      msg)

print('%s' % separator)

if CLImode:

    # wxPython-style, nCurses-based GUI Mode
    try:

        GUImode = True
        print('\n\nGUImode=%s' % GUImode)

        # from tsWxGTUI_Py2x import tsLibGUI
        # print('\n\ntsLibGUI: %s' % dir(tsLibGUI))

        from tsWxGTUI_Py2x.tsLibGUI import tsWx as wx
        print('\n\nwx: %s' % dir(wx))

        from tsWxGTUI_Py2x.tsLibGUI import tsWxMultiFrameEnv
        print('\n\ntsWxMultiFrameEnv: %s' % dir(tsWxMultiFrameEnv))

        from tsWxMultiFrameEnv import MultiFrameEnv
        print('\n\nMultiFrameEnv: %s' % dir(MultiFrameEnv))

    except ImportError, importCode:

        GUImode = False
        print('\n\nGUImode=%s' % GUImode)

        fmt1 = '%s: ImportError ' % __title__
        fmt2 = '(tsLibGUI); '
        fmt3 = 'importCode=%s' % str(importCode)
        msg = fmt1 + fmt2 + fmt3

        print(msg)

        raise tse.UserInterfaceException(
            tse.CHARACTER_GRAPHICS_NOT_AVAILABLE,
            msg)

print('%s' % separator)
