import importlib.util
import subprocess

# Check if a package is installed
def package_installed(package_name):
    return importlib.util.find_spec(package_name) is not None

# Install a package using pip
def install_package(package_name):
    subprocess.check_call(["pip", "install", package_name])

# Check and install required packages
required_packages = ["termcolor", "colorama"]
for package in required_packages:
    if not package_installed(package):
        install_package(package)

# Execute the main script
exec(open("0000.py").read())
