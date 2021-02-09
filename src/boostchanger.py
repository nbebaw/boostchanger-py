from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os
import functions
import aboutWindow

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Get the absolute path of the directory
path = os.path.dirname(os.path.abspath(__file__))
# Add icons
icon = QIcon(os.path.join(path, "icons/icon.png"))
OnIcon = QIcon(os.path.join(path, "icons/on.png"))
OffIcon = QIcon(os.path.join(path, "icons/off.png"))
exitIcon = QIcon(os.path.join(path, "icons/exit.png"))
aboutIcon = QIcon(os.path.join(path, "icons/about.png"))
energyIcon = QIcon(os.path.join(path, "icons/energy.png"))

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setToolTip("Boost Changer")
tray.setVisible(True)

# Creating the options
menu = QMenu()

about = QAction("About")
MainWindow = QMainWindow()
ui = aboutWindow.Ui_MainWindow()
ui.setupUi(MainWindow)

# make About window center of screen
qr = MainWindow.frameGeometry()
cp = QDesktopWidget().availableGeometry().center()
qr.moveCenter(cp)
MainWindow.move(qr.topLeft())
about.triggered.connect(MainWindow.show)
about.setIcon(aboutIcon)

# Turbo boost ON
boostOn = QAction("Turbo boost ON")
boostOn.triggered.connect(functions.turboOn)
boostOn.setIcon(OnIcon)

# Turbo boost OFF
boostOff = QAction("Turbo boost OFF")
boostOff.triggered.connect(functions.turboOff)
boostOff.setIcon(OffIcon)

# new menu for energy performance in the main menu
energyMenu = QMenu("Energy performance")
powerSave = QAction("Power Save")
powerSave.triggered.connect(functions.powerSave)
balance = QAction("Balance")
balance.triggered.connect(functions.balance)
balancePerformance = QAction("Balance Performance")
balancePerformance.triggered.connect(functions.balancePerformance)
performance = QAction("Performance")
performance.triggered.connect(functions.performance)

energyMenu.addAction(powerSave)
energyMenu.addAction(balance)
energyMenu.addAction(balancePerformance)
energyMenu.addAction(performance)
energyMenu.setIcon(energyIcon)

# Add all options on menu
menu.addAction(about)
menu.addMenu(energyMenu)
menu.addAction(boostOn)
menu.addAction(boostOff)

# Adding separator between the options and quit
menu.addSeparator()

# To quit the app
quit = QAction("Quit")
quit.setIcon(exitIcon)
quit.triggered.connect(app.quit)
menu.addAction(quit)

# adding options to the system tray
tray.setContextMenu(menu)

# Execute the entire app
app.exec_()
