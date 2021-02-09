#!/bin/bash

PKGVER=0.1.1
# package delete
rm -r /opt/boostchanger-v$PKGVER
rm /usr/bin/boostchanger-py
rm /usr/share/applications/boostchanger-py.desktop
rm /usr/share/pixmaps/boostchanger-py.png

# remove autostart
rm /home/$SUDO_USER/.config/autostart