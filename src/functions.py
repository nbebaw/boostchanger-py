import os
from plyer import notification


turbo = open("/sys/devices/system/cpu/intel_pstate/no_turbo", "r")
energy = open("/sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference", "r")
lineTurbo = turbo.readline().split("\n", 1)[0]
lineEnergy = energy.readline().split("\n", 1)[0]
path = os.path.dirname(os.path.abspath(__file__))

# Notify user about the status off turbo boost when app starts
if (lineTurbo == "1"):
    notification.notify(
        message="Turbo boost is OFF",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png"),
    )
else:
    notification.notify(
        message="Turbo boost is ON",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )

# Notify user about the status off energy performance when app starts
if (lineEnergy == "power"):
    notification.notify(
        message="Energy performance: Power Save",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )
elif (lineEnergy == "balance_power"):
    notification.notify(
        message="Energy performance: Balance",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )
elif (lineEnergy == "balance_performance"):
    notification.notify(
        message="Energy performance: Balance Performance",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )
else:
    notification.notify(
        message="Energy performance: Performance",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )

# Turbo Boost

def turboOn():
    os.system("echo 0 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")
    notification.notify(
        message="Turbo boost is now ON",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )


def turboOff():
    os.system("echo 1 | pkexec tee /sys/devices/system/cpu/intel_pstate/no_turbo")
    notification.notify(
        message="Turbo boost is now OFF",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )

# Energy Performance

def powerSave():
    os.system("echo power | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
    notification.notify(
        message="Energy performance: Power Save",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )


def balance():
    os.system("echo balance_power | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
    notification.notify(
        message="Energy performance: Balance",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )


def balancePerformance():
    os.system("echo balance_performance | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
    notification.notify(
        message="Energy performance: Balance Performance",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )


def performance():
    os.system("echo performance | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
    notification.notify(
        message="Energy performance: Performance",
        app_name="Boost Changer",
        app_icon=os.path.join(path, "icons/icon.png")
    )
