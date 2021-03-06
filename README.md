# Boost Changer - PYTHON
![GitHub](https://img.shields.io/github/license/nbebaw/boostchanger-py) ![GitHub all releases](https://img.shields.io/github/downloads/nbebaw/boostchanger-py/total) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/nbebaw/boostchanger-py)
## :bangbang: This App is now only for Linux :bangbang:

### :heavy_exclamation_mark: This App needs root rights. When and why? :heavy_exclamation_mark:

Boost Changer is a tray application and made to control the frequencies of <b>Intel CPUs and AMD CPUs</b>. It can also manage the processor's energy consumption through Energy-Performance Preference.

In generall this app does not need root rights but when you hit the Turn Off or On button a popup window will ask you about your root password.

#### why?

- In your Kernel there is a file called <code>/sys/devices/system/cpu/intel_pstate/no_turbo</code>.
> To turn off or on your turbo boost you have to change this file and that is what this app does.<br>

- In your Kernel there is a file called <code>/sys/devices/system/cpu/intel_pstate/max_perf_pct</code>.
> when you change the energy performance in Boost Changer you have to change this file and that is what this app does.

#### :pushpin: This app will only work on a real machine. :pushpin:

## What it isn't
This is just a GUI application and it is not meant to replace 
[TLP](https://linrunner.de/en/tlp/tlp.html), [powertop](https://01.org/powertop) or 
any other power management / energy consumption service. It is meant just to 
provide quick access to ``sysfs`` settings related to Intel Processors and 
in fact it can run on top of TLP.

## Installation

### Download, extract and setup
```bash
# Download
wget https://github.com/nbebaw/boostchanger-py/releases/download/v0.1.4/boost_changer-0.1.4.tar.gz

# Extract
tar -xvf boost_changer-0.1.4.tar.gz

# Setup
cd boost_changer-0.1.4
sudo ./install.sh
```

## New features for future releases
For v0.2.0

1 = High Prio |  2 = Middle Prio |  3 = Low Prio
Feature | Prio
--- | ---
Make a window of the application as an alternative to the tray | 2

