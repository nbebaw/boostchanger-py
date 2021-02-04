#!/bin/bash
PKGVER=0.0.4

# package
cp -r src /opt
mv /opt/src /opt/boostchanger-v$PKGVER
install -Dm755 build/boostchanger-py.sh /usr/bin/boostchanger-py
install -Dm 644 build/boostchanger-py.desktop /usr/share/applications/boostchanger-py.desktop
install -Dm 644 build/boostchanger-py.png /usr/share/pixmaps/boostchanger-py.png

# add boostchanger to autostart
cp build/boostchanger-py.desktop /home/$SUDO_USER/.config/autostart
chown $SUDO_USER:$SUDO_USER /home/$SUDO_USER/.config/autostart/boostchanger-py.desktop

echo "Boost Changer is successfully installed"