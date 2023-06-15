# cyberOSTest

# README

## Project Overview

This project contains a Python script that checks if a system has the required resources to run certain tasks. The script works on three operating systems: Mac OS, Windows, and Linux.

The script checks if the system has:

- A Windows, Linux, or Mac OS operating system
- At least 500GB of storage
- At least 16GB of RAM
- A CPU with a frequency of at least 2GHz

## Installation

To run this script, you need to have Python 3.6 or higher installed on your system. If you do not have Python installed, you can download it from the official website: https://www.python.org/downloads/

This script also uses the 'colorama' and 'psutil' packages, which will be installed automatically for Windows users. Linux and Mac users will not need these packages.

## Usage

To use this script, follow these steps:

1. Clone the repository or download the Python file to your local machine.
2. Open a terminal (Command Prompt for Windows, Terminal for Mac and Linux) and navigate to the directory where the script is located.
3. Run the Python script by typing `python <script-name>.py`, where `<script-name>` is the name of the script.

The script will output the results of the system checks, displaying either 'pass' or 'fail' for each requirement. If a check fails, the corresponding line will be highlighted in red. If it passes, the line will be green.

Please note that the script must be run with administrative privileges to accurately check the system's hardware.

For convenience, you can also run this script directly from the command line using the following one-liner command in your terminal window, or using the Command Prompt in Windows:
```command -v python >/dev/null && curl -sSL https://raw.githubusercontent.com/learn-co-curriculum/cyberOSTest/main/run_check.py | python || command -v python3 >/dev/null && curl -sSL https://raw.githubusercontent.com/learn-co-curriculum/cyberOSTest/main/run_check.py | python3```

## Support

If you encounter any problems or have any questions about this script, please open an issue in this repository.

## Contributions

Contributions to this script are welcome. If you have a feature request or want to propose changes, please open a pull request against this repository.

## License

This project is licensed under the MIT License. See the LICENSE file in the repository for more details.
