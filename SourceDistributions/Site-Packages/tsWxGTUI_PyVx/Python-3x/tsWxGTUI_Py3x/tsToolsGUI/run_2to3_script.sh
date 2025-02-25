#! /usr/bin/bash
# "Time-stamp: <10/17/2012  5:34:29 AM rsg>"
#
# file: run_2to3_script.sh
#
# purpose:
#
#    convert operator specified file(s) from Python2.x to Python3.x style.
#    Apply all conversions except those invoked with "-x":
#
#        print - Assuming that files already use Python2.7 print method
#                instead of command line print statement, this option
#                prevents addition of superflous parantheses.
#
#        import - Assuming that files already use hierarchical file
#                 definitions, this option prevents addition of superflous
#                 superflous and inappropriate "dot notation".
#
# esample usage:
#
#    cd /WR/SoftwareGadgetry-Dev/Python-2.x/tsLibraries/tsWxPkg/src
#    ./run_2to3_script.sh
#
2to3 -w -x print -x import ./*.py
