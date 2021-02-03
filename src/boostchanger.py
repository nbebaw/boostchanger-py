from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from os import system
from plyer import notification

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# /sys/devices/system/cpu/intel_pstate/no_turbo

def turboOn():
    system("echo 0 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")
    notification.notify(
        # title="Turbo boost",
        message="Turbo boost is now ON",
        app_name="Boost Changer",
    )


def turboOff():
    system("echo 1 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")
    notification.notify(
        # title="Turbo boost",
        message="Turbo boost is now OFF",
        app_name="Boost Changer",
    )


# Add icons
icon = QIcon("icons/icon.png")
OnIcon = QIcon("icons/on.png")
OffIcon = QIcon("icons/off.png")
exitIcon = QIcon("icons/exit.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setToolTip("Boost Changer")
tray.setVisible(True)

# Creating the options
menu = QMenu()
option1 = QAction("Turbo boost ON")
option1.triggered.connect(turboOn)
option1.setIcon(OnIcon)
option2 = QAction("Turbo boost OFF")
option2.triggered.connect(turboOff)
option2.setIcon(OffIcon)
menu.addAction(option1)
menu.addAction(option2)

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
