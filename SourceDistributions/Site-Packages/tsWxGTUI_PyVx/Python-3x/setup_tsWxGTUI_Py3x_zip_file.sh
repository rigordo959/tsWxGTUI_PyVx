#!/usr/bin/bash
#"Time-stamp: <03/17/2016  3:32:01 AM rsg>"
#
# create an archive file (e.g., ZIP file on Windows) containing
# your setup script setup.py, and your module (tsPlatformQuery.py)
# or package (tsLibCLI).
#
# zip options archive inpath inpath .
# zip -r /path/to/tsWxGTUI_PyVx-0.0.6.zip /path/to/tsWxGTUI_PyVx
#
# theDestination="dist"
theSource="tsWxGTUI_Py3x"
theVersion="0.0.6"
theExtension="zip"

# rm -rf ../$theDestination
# mkdir ../$theDestination
zip -r ../$theSource-$theVersion.$theExtension ./$theSource
