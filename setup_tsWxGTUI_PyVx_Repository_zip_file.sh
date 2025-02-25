#!/usr/bin/bash
#"Time-stamp: <07/07/2015  6:55:05 PM rsg>"
#
# create an archive file (e.g., ZIP file on Windows) containing
# your setup script setup.py, and your module (tsPlatformQuery.py)
# or package (tsLibCLI).
#
# zip options archive inpath inpath .
# zip -r /path/to/tsWxGTUI_PyVx-0.0.0.zip /path/to/tsWxGTUI_PyVx
#
theDestination="dist"
theSource="tsWxGTUI_PyVx_Repository"
theVersion="0.0.0"
theExtension="zip"

rm -rf ../$theDestination
mkdir ../$theDestination
zip -r ../$theDestination/$theSource-$theVersion..$theExtension ../$theSource
