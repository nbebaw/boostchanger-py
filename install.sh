#!/bin/bash
PKGVER=0.0.3
WGET=/usr/bin/wget
TAR=/usr/bin/tar

# prepare
if [ -f $WGET ]; then
    wget https://github.com/nbebaw/boostchanger-py/releases/download/v$PKGVER/boost_changer-$PKGVER.tar.gz
else
    echo "To install boostchanger you need ( wget ). Please install it and try again. e.g: sudo apt install wget OR sudo pacman -S wget"
fi

if [ -f $TAR ]; then
    tar -xvf boost_changer-$PKGVER.tar.gz
else
    echo "To install boostchanger you need ( tar ). Please install it and try again. e.g: sudo apt install tar OR sudo pacman -S tar"
fi

# package
cp -r boost_changer-$PKGVER/src /opt
mv /opt/src /opt/boostchanger-v$PKGVER
install -Dm755 boost_changer-$PKGVER/build/boostchanger-py.sh /usr/bin/boostchanger-py
install -Dm 644 boost_changer-$PKGVER/build/boostchanger-py.desktop /usr/share/applications/boostchanger-py.desktop
install -Dm 644 boost_changer-$PKGVER/build/boostchanger-py.png /usr/share/pixmaps/boostchanger-py.png

# add boostchanger to autostart
cp boost_changer-$PKGVER/build/boostchanger-py.desktop ~/.config/autostart
chown $USER:$USER ~/.config/autostart/boostchanger-py.desktop

# Clean up
rm boost_changer-$PKGVER.tar.gz
rm -r boost_changer-$PKGVER