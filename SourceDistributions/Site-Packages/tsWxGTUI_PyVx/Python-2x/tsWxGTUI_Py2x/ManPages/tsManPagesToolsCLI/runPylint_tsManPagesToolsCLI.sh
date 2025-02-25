#!/usr/bin/bash
#"Time-stamp: <06/05/2013  5:46:57 AM rsg>"
# lookForErrors="E:"
# lookForWarnings="W:"
# lookFor=lookForErrors
rm -rf ../pylint
mkdir  ../pylint
mkdir  ../pylint/Errors
mkdir  ../pylint/Warnings

function makePyLint() {
  pylint $1.py | grep "E:" > ../pylint/Errors/$1.lst
  pylint $1.py | grep "W:" > ../pylint/Warnings/$1.lst
}

# test_multi_author_copyright
# test_tsCurses
# test_tsDiagnosticCurses
# test_tsParseAcceleratorTextLabel
# test_tsWxAcceleratorEntry
# test_tsWxAUI
# test_tsWxBoxSizer
# test_tsWxCheckBox
# test_tsWxCheckBoxEvent
# test_tsWxCliLinesOfCode
# test_tsWxDiagnostic
# test_tsWxDialogDemo
# test_tsWxDisplay
# test_tsWxEvents
# test_tsWxFieldMarkup
# test_tsWxFileCommander
# test_tsWxFrame
# test_tsWxGauge
# test_tsWxGraphicalTextUserInterface
# test_tsWxGridSizer
# test_tsWxKeyEvents
# test_tsWxLinesOfCode
# test_tsWxLogo
# test_tsWxMarkupDiagnostic
# test_tsWxMetrics
# test_tsWxMidiWindow
# test_tsWxMouseEvent
# test_tsWxOverlays
# test_tsWxPasswordEntryDialog
# test_tsWxPySimpleApp
# test_tsWxRadioBox
# test_tsWxRadioBoxEvent
# test_tsWxRSM
# test_tsWxScrollBar
# test_tsWxScrolled
# test_tsWxScrolled3Boxes
# test_tsWxScrolledWindow
# test_tsWxScrolledWindowDual
# test_tsWxSplashScreen
# test_tsWxStaticBoxSizer
# test_tsWxStaticLine
# test_tsWxStaticText
# test_tsWxStatusBar
# test_tsWxSystemSettings
# test_tsWxTaskBar
# test_tsWxTemplate
# test_tsWxTextCtrl
# test_tsWxTextEntryDialog
# test_tsWxVt100Widgets
# test_tsWxWidgets
# test_tsWxWidgetsMarkup
makePyLint ./configobj
makePyLint ./decorator
makePyLint ./threadpool
makePyLint ./tsApplication
makePyLint ./tsCommandLineEnv
makePyLint ./tsCommandLineInterface
makePyLint ./tsCommandLineParser
makePyLint ./tsConfig
makePyLint ./tsDecorators
makePyLint ./tsExceptions
makePyLint ./tsGraphicalTextUserInterface
makePyLint ./tsLogger
makePyLint ./tsOperatorSettingsParser
makePyLint ./tsOptionParser
makePyLint ./tsPlatformRunTimeEnvironment
makePyLint ./tsReAuthor
makePyLint ./tsReportUtilities
makePyLint ./tsReVersion
makePyLint ./tsSysCommands
makePyLint ./tsThreadPool
makePyLint ./tsTreeTrimLines
makePyLint ./tsTreeTrimShutil
makePyLint ./tsWx
makePyLint ./tsWxAcceleratorEntry
makePyLint ./tsWxAcceleratorTable
makePyLint ./tsWxApp
makePyLint ./tsWxBoxSizer
makePyLint ./tsWxButton
makePyLint ./tsWxCallLater
makePyLint ./tsWxCaret
makePyLint ./tsWxCheckBox
makePyLint ./tsWxChoice
makePyLint ./tsWxCliLinesOfCode
makePyLint ./tsWxColor
makePyLint ./tsWxColorDatabase
makePyLint ./tsWxCommandLineEnv
makePyLint ./tsWxControl
makePyLint ./tsWxControlWithItems
makePyLint ./tsWxCursor
makePyLint ./tsWxDebugHandlers
makePyLint ./tsWxDialog
makePyLint ./tsWxDisplay
makePyLint ./tsWxDoubleLinkedList
makePyLint ./tsWxEraseEvent
makePyLint ./tsWxEvent
makePyLint ./tsWxEventDaemon
makePyLint ./tsWxEventLoop
makePyLint ./tsWxEventLoopActivator
makePyLint ./tsWxEventQueueEntry
makePyLint ./tsWxEventTableEntry
makePyLint ./tsWxEvtHandler
makePyLint ./tsWxFlexGridSizer
makePyLint ./tsWxFocusEvent
makePyLint ./tsWxFrame
makePyLint ./tsWxGauge
makePyLint ./tsWxGlobals
makePyLint ./tsWxGraphicalTextUserInterface
makePyLint ./tsWxGridBagSizer
makePyLint ./tsWxGridSizer
makePyLint ./tsWxItemContainer
makePyLint ./tsWxKeyboardState
makePyLint ./tsWxKeyEvent
makePyLint ./tsWxLayout_h
makePyLint ./tsWxLayoutAlgorithm
makePyLint ./tsWxLayoutGTUI
makePyLint ./tsWxLinesOfCode
makePyLint ./tsWxListBox
makePyLint ./tsWxLog
makePyLint ./tsWxMenu
makePyLint ./tsWxMenuBar
makePyLint ./tsWxMouseEvent
makePyLint ./tsWxMouseState
makePyLint ./tsWxMultiFrameEnv
makePyLint ./tsWxNonLinkedList
makePyLint ./tsWxObject
makePyLint ./tsWxPanel
makePyLint ./tsWxPasswordEntryDialog
makePyLint ./tsWxPoint
makePyLint ./tsWxPyApp
makePyLint ./tsWxPyEventBinder
makePyLint ./tsWxPyOnDemandOutputWindow
makePyLint ./tsWxPySimpleApp
makePyLint ./tsWxPySizer
makePyLint ./tsWxRadioBox
makePyLint ./tsWxRadioButton
makePyLint ./tsWxRect
makePyLint ./tsWxReVersion
makePyLint ./tsWxScreen
makePyLint ./tsWxScrollBar
makePyLint ./tsWxScrollBarButton
makePyLint ./tsWxScrollBarGauge
makePyLint ./tsWxScrolled
makePyLint ./tsWxScrolledText
makePyLint ./tsWxScrolledWindow
makePyLint ./tsWxShowEvent
makePyLint ./tsWxSize
makePyLint ./tsWxSizer
makePyLint ./tsWxSizerFlags
makePyLint ./tsWxSizerItem
makePyLint ./tsWxSizerItemList
makePyLint ./tsWxSizerSpacer
makePyLint ./tsWxSlider
makePyLint ./tsWxSplashScreen
makePyLint ./tsWxStaticBox
makePyLint ./tsWxStaticBoxSizer
makePyLint ./tsWxStaticLine
makePyLint ./tsWxStaticText
makePyLint ./tsWxStatusBar
makePyLint ./tsWxSystemSettings
makePyLint ./tsWxTaskBar
makePyLint ./tsWxTextCtrl
makePyLint ./tsWxTextEditBox
makePyLint ./tsWxTextEntry
makePyLint ./tsWxTextEntryDialog
makePyLint ./tsWxTimer
makePyLint ./tsWxToggleButton
makePyLint ./tsWxTopLevelWindow
makePyLint ./tsWxValidator
makePyLint ./tsWxWindow
