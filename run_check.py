import os
import subprocess
import sys
import platform

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}.")
        raise e


# Detect the operating system
os_type = platform.system()

if os_type == 'Darwin':  # Mac OS
    # Run the Python script
    # ANSI color codes
    NC = '\033[0m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'
    
    def evaluate_test(command, comparator, required_value):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
            result = result.stdout.decode('utf-8').strip()
            # Compare the output with the required value
            if comparator(result, required_value):
                return "pass", True
            else:
                return "fail", False
        except subprocess.CalledProcessError:
            return "fail", False
    
    def print_table_results(name, command, comparator=lambda x, y: True, required_value=None):
        result, success = evaluate_test(command, comparator, required_value)
        color = GREEN if success else RED
        print(f"{name:<30} => [ {color}{result if result else 'fail'}{NC} ]")
    
    def print_delimiter():
        print(f"{BLUE}{'*'*40}{NC}")
    
    def print_header(header):
        print(f"\n{CYAN}{'*'*12} {header} {'*'*12}{NC}\n")
    
    # Validation
    print_header("VALIDATING SETUP")
    print_delimiter()
    
    # 1. Windows or Linux
    os_comparator = lambda x, y: x == 'Linux' or x.startswith('MINGW')
    print_table_results("Windows or Linux", "uname -s", comparator=os_comparator)
    print_delimiter()
    
    # 2. At least 500GB storage
    print_table_results("At least 500GB storage", "df -k / | tail -n 1 | awk '{print $4}'", comparator=lambda x, y: int(x) >= y, required_value=500*1024*1024)  # Comparing in KB
    print_delimiter()
    
    # 3. At least 16GB RAM
    print_table_results("At least 16GB RAM", "sysctl -n hw.memsize", comparator=lambda x, y: int(x) >= y, required_value=16*1024*1024*1024)  # Comparing in Bytes
    print_delimiter()
    
    # 4. 2GHz+ Processor
    def cpu_speed_comparator(result, required_value):
        speed = result.split('@')[1].strip()
        speed = float(speed[:-3])  # Removing 'GHz' and converting to float
        return speed >= required_value
    
    print_table_results("2GHz+ Processor", "sysctl -n machdep.cpu.brand_string", comparator=cpu_speed_comparator, required_value=2.0)  # Comparing in GHz
    print_delimiter()
elif os_type in ['Windows']:  # Windows
    # Install dependencies
    install('colorama')
    install('psutil')
    # Run the Python script
    from colorama import init, Fore, Style
    import platform
    import os
    import psutil
    
    init(autoreset=True)
    
    # Use colorama colors
    class colors:
        OKGREEN = Fore.GREEN
        FAIL = Fore.RED
        OKBLUE = Fore.BLUE
        HEADER = Fore.CYAN
    
    def evaluate_test(test_name, test_func):
        """Print test name and pass/fail depending on whether test_func returns True."""
        result = test_func()
        status = colors.OKGREEN + "pass" if result else colors.FAIL + "fail"
        print(f"{test_name:30} => [ {status} ]{Style.RESET_ALL}")
    
    def check_os():
        """Check if the OS is either Windows or Linux."""
        return platform.system() in ['Windows', 'Linux']
    
    def check_storage():
        """Check if the machine has at least 500GB of storage."""
        return psutil.disk_usage('/')[0] / (2**30) >= 500
    
    def check_ram():
        """Check if the machine has at least 16GB of RAM."""
        return psutil.virtual_memory().total / (2**30) >= 16
    
    def check_cpu():
        """Check if the CPU has a frequency of at least 2GHz."""
        return psutil.cpu_freq().max >= 2000
    
    if __name__ == "__main__":
        print("\n" + colors.HEADER + "************ VALIDATING SETUP ************" + Style.RESET_ALL + "\n")
        print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)
    
        evaluate_test("Windows or Linux", check_os)
        print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)
    
        evaluate_test("At least 500GB storage", check_storage)
        print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)
    
        evaluate_test("At least 16GB RAM", check_ram)
        print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)
    
        evaluate_test("2GHz+ Processor", check_cpu)
        print(colors.OKBLUE + "******************************************" + Style.RESET_ALL)

elif os_type == 'Linux':  # Linux
    # ANSI color codes
    NC = '\033[0m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    CYAN = '\033[0;36m'

    def evaluate_test(command, comparator, required_value):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
            result = result.stdout.decode('utf-8').strip()
            # Compare the output with the required value
            if comparator(result, required_value):
                return "pass", True
            else:
                return "fail", False
        except subprocess.CalledProcessError:
            return "fail", False

    def print_table_results(name, command, comparator=lambda x, y: True, required_value=None):
        result, success = evaluate_test(command, comparator, required_value)
        color = GREEN if success else RED
        print(f"{name:<30} => [ {color}{result if result else 'fail'}{NC} ]")

    def print_delimiter():
        print(f"{BLUE}{'*'*40}{NC}")

    def print_header(header):
        print(f"\n{CYAN}{'*'*12} {header} {'*'*12}{NC}\n")

    # Validation
    print_header("VALIDATING SETUP")
    print_delimiter()

    # 1. Windows or Linux
    os_comparator = lambda x, y: x == 'Linux'
    print_table_results("Linux", "uname -s", comparator=os_comparator)
    print_delimiter()

    # 2. At least 500GB storage
    print_table_results("At least 500GB storage", "df -k / | tail -n 1 | awk '{print $4}'", comparator=lambda x, y: int(x) >= y, required_value=500*1024*1024)  # Comparing in KB
    print_delimiter()

    # 3. At least 16GB RAM
    print_table_results("At least 16GB RAM", "grep MemTotal /proc/meminfo | awk '{print $2}'", comparator=lambda x, y: int(x) >= y, required_value=16*1024*1024)  # Comparing in KB
    print_delimiter()

    # 4. 2GHz+ Processor
    print_table_results("2GHz+ Processor", "lscpu | awk '/CPU MHz/'", comparator=lambda x, y: float(x.split(':')[1].strip()) >= y, required_value=2000.0)  # Comparing in MHz
    print_delimiter()

else:
    print("Unsupported operating system: ", os_type)
