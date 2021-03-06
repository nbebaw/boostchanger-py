import os
from plyer import notification
import subprocess

# Intel or AMD ?
vendor=subprocess.getoutput("cat /proc/cpuinfo | grep -m1 'vendor_id' | awk '{ print $3 }'")
if (vendor == "GenuineIntel"):
    turbo = open("/sys/devices/system/cpu/intel_pstate/no_turbo", "r")
    energy = open(
        "/sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference", "r")
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
        os.system(
            "echo power | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
        notification.notify(
            message="Energy performance: Power Save",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )


    def balance():
        os.system(
            "echo balance_power | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
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
        os.system(
            "echo performance | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference")
        notification.notify(
            message="Energy performance: Performance",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )
else:
    turbo = open("/sys/devices/system/cpu/cpufreq/boost", "r")
    energy = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor", "r")
    lineTurbo = turbo.readline().split("\n", 1)[0]
    lineEnergy = energy.readline().split("\n", 1)[0]
    path = os.path.dirname(os.path.abspath(__file__))

    # Notify user about the status off turbo boost when app starts
    if (lineTurbo == "1"):
        notification.notify(
            message="Turbo boost is ON",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png"),
        )
    else:
        notification.notify(
            message="Turbo boost is OFF",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    # Notify user about the status off energy performance when app starts
    if (lineEnergy == "conservative"):
        notification.notify(
            message="Energy performance: Conservative",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )
    elif (lineEnergy == "ondemand"):
        notification.notify(
            message="Energy performance: Ondemand",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )
    elif (lineEnergy == "userspace"):
        notification.notify(
            message="Energy performance: userspace",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )
    elif (lineEnergy == "powersave"):
         notification.notify(
            message="Energy performance: Power Save",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )
    elif (lineEnergy == "performance"):
         notification.notify(
            message="Energy performance: Performance",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )
    else:
        notification.notify(
            message="Energy performance: Schedutil",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    # Turbo Boost
    def turboOn():
        os.system("echo 1 | pkexec tee /sys/devices/system/cpu/cpufreq/boost")
        notification.notify(
            message="Turbo boost is now ON",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    def turboOff():
        os.system("echo 0 | pkexec tee /sys/devices/system/cpu/cpufreq/boost")
        notification.notify(
            message="Turbo boost is now OFF",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    # Energy Performance
    def conservativeAMD():
        os.system("echo conservative | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        notification.notify(
            message="Energy performance: Conservative",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    def ondemandAMD():
        os.system("echo ondemand | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        notification.notify(
            message="Energy performance: Ondemand",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    def userspaceAMD():
        os.system("echo userspace | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        notification.notify(
            message="Energy performance: Userspace",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    def powerSaveAMD():
        os.system("echo powersave | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        notification.notify(
            message="Energy performance: Power Save",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    def performanceAMD():
        os.system("echo performance | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        notification.notify(
            message="Energy performance: Performance",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )

    def schedutilAMD():
        os.system("echo schedutil | pkexec tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
        notification.notify(
            message="Energy performance: Schedutil",
            app_name="Boost Changer",
            app_icon=os.path.join(path, "icons/icon.png")
        )