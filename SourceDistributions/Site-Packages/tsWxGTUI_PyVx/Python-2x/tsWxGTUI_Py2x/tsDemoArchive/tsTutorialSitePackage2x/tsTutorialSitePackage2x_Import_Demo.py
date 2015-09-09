#! /usr/bin/env python
# "Time-stamp: <05/13/2015  3:27:19 AM rsg>"
'''
tsSitePackage_Import_Demo.py - Module to demonstrates the import
sequence for building block components of a TeamSTARS
"tsWxGTUI_PyVx" Toolkit site-package:

    1st stage (required) --- Command Line Interface (CLI)
                             Library
    2nd stage  (optioal) --- Graphical-style User Interface (GUI)
                             Library
    3rd stage (launcher) --- tsCommandLineEnv or tsWxMultiFrameEnv.
'''
#################################################################
#
# File: tsSitePackage_Import_Demo.py
#
# Purpose:
#
#     Module to demonstrates the import sequence for building
#     block components of a TeamSTARS "tsWxGTUI_PyVx" Toolkit
#     site-package:
#
#     1st stage (required) --- Command Line Interface (CLI)
#                              Library
#     2nd stage  (optioal) --- Graphical-style User Interface (GUI)
#                              Library
#     3rd stage (launcher) --- tsCommandLineEnv or tsWxMultiFrameEnv.
#
# Usage (example):
#
#    python tsSitePackage_Import_Demo.py
#
# Capabilities:
#
#    None.
#
# Limitations:
#
#    None.
#
# Notes:
#
#    None.
#
# Classes:
#
#    None.
#
# Methods:
#
#    None.
#
# Modifications:
#
#    None.
#
# ToDo:
#
#    None.
#
#################################################################

__title__     = 'tsSitePackage_Import_Demo'
__version__   = '1.0.0'
__date__      = '05/13/2015'
__authors__   = 'Richard S. Gordon'
__copyright__ = 'Copyright (c) 2015 ' + \
                '%s.\n\t\tAll rights reserved.' % __authors__
__license__   = 'GNU General Public License, ' + \
                'Version 3, 29 June 2007'
__credits__   = ''

__line1__ = '%s, v%s (build %s)' % (__title__, __version__, __date__)
__line2__ = 'Author(s): %s' % __authors__
__line3__ = '%s' % __copyright__

if len( __credits__) == 0:
    __line4__ = '%s' % __license__
else:
    __line4__ = '%s%s' % (__license__, __credits__)

__header__ = '\n\n%s\n\n  %s\n  %s\n  %s\n' % (__line1__,
                                               __line2__,
                                               __line3__,
                                               __line4__)

mainTitleVersionDate = __line1__

#--------------------------------------------------------------------------

separator = '''
-------------------------------------------------------------------------
'''

#--------------------------------------------------------------------------

import sys

#--------------------------------------------------------------------------

YourApplicationName = sys.argv[0]

print('%s' % separator)

print('\n\nName=%s' % YourApplicationName)
print('\n\nPurpose=%s' % __doc__)

print('%s' % separator)

# Python-based CLI Mode
print('\n%s' % '1st stage (required) --- ' + \
      'Command Line Interface (CLI) Library')
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

##    from tsWxGTUI_Py2x.tsLibCLI import tsDoubleLinkedList
##    print('\n\ntsDoubleLinkedList: %s' % dir(tsDoubleLinkedList))

    from tsWxGTUI_Py2x.tsLibCLI.tsDoubleLinkedList import DoubleLinkedList
##    from tsDoubleLinkedList \
##         import DoubleLinkedList
    print('\n\nDoubleLinkedList: %s' % dir(DoubleLinkedList))

    if CLImode:

        from tsWxGTUI_Py2x.tsLibCLI.tsCommandLineEnv import CommandLineEnv

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

print('\n%s' % '2nd stage  (optioal) --- ' + \
      'Graphical-style User Interface (GUI) library')

if CLImode:

    # wxPython-style, nCurses-based GUI Mode
    try:

        GUImode = True
        print('\n\nGUImode=%s' % GUImode)

        # from tsWxGTUI_Py2x import tsLibGUI
        # print('\n\ntsLibGUI: %s' % dir(tsLibGUI))

        from tsWxGTUI_Py2x.tsLibGUI import tsWx as wx
        print('\n\nwx: %s' % dir(wx))

        from tsWxGTUI_Py2x.tsLibGUI.tsWxMultiFrameEnv import MultiFrameEnv
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

print('\n%s' % '3rd stage (launcher) --- ' + \
      'tsCommandLineEnv or tsWxMultiFrameEnv.')
