#!/bin/bash
PKGVER=0.1.2
PKGOLD=0.1.1

# prepare

if [ -d /opt/boostchanger-v$PKGOLD]; then
    rm -r /opt/boostchanger-v$PKGOLD
    rm /usr/bin/boostchanger-py
    rm /usr/share/applications/boostchanger-py.desktop
    rm /usr/share/pixmaps/boostchanger-py.png
    rm /home/$SUDO_USER/.config/autostart
    echo "The old version of Boost Changer has been deleted"
fi
# install plyer package for notifications
pip install plyer

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