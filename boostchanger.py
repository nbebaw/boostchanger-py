from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

app = QApplication([])
app.setQuitOnLastWindowClosed(False)


# /sys/devices/system/cpu/intel_pstate/no_turbo
def turboOn():
    os.system("echo 0 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")

def turboOff():
    os.system("echo 1 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")

# Add icon
icon = QIcon("icon.png")

# Adding item on the menu bar
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Creating the options
menu = QMenu()
option1 = QAction("Turbo boost ON")
option1.triggered.connect(turboOn)
option2 = QAction("Turbo boost OFF")
option2.triggered.connect(turboOff)
menu.addAction(option1)
menu.addAction(option2)

# To quit the app
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# adding options to the system tray
tray.setContextMenu(menu)

app.exec_()