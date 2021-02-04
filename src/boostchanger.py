from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
import os
from plyer import notification

app = QApplication([])
app.setQuitOnLastWindowClosed(False)


def turboOn():
    os.system("echo 0 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")
    notification.notify(
        # title="Turbo boost",
        message="Turbo boost is now ON",
        app_name="Boost Changer",
    )


def turboOff():
    os.system("echo 1 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")
    notification.notify(
        # title="Turbo boost",
        message="Turbo boost is now OFF",
        app_name="Boost Changer",
    )


# Get the absolute path of the directory
path = os.path.dirname(os.path.abspath(__file__))
# Add icons
icon = QIcon(os.path.join(path, "icons/icon.png"))
OnIcon = QIcon(os.path.join(path, "icons/on.png"))
OffIcon = QIcon(os.path.join(path, "icons/off.png"))
exitIcon = QIcon(os.path.join(path, "icons/exit.png"))

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setToolTip("Boost Changer")
tray.setVisible(True)

# Creating the options
menu = QMenu()

# Turbo boost ON
boostOn = QAction("Turbo boost ON")
boostOn.triggered.connect(turboOn)
boostOn.setIcon(OnIcon)

# Turbo boost OFF
boostOff = QAction("Turbo boost OFF")
boostOff.triggered.connect(turboOff)
boostOff.setIcon(OffIcon)

# new menu for energy performance in the main menu
energyMenu = QMenu("Energy performance")
powerSave = QAction("Power Save")
balance = QAction("Balance")
balancePerformance = QAction("Balance Performance")
performance = QAction("Performance")

energyMenu.addAction(powerSave)
energyMenu.addAction(balance)
energyMenu.addAction(balancePerformance)
energyMenu.addAction(performance)

# Add all options on menu
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
