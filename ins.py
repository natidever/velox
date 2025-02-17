import subprocess

''' Script that automate installing python packages and adding them the requirements file '''
def install_and_update_requirements(package_name, requirements_file="requirements.txt"):
    # Install the package
    subprocess.run(["pip", "install", package_name], check=True)

    # Get the installed package version
    result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
    package_list = result.stdout.splitlines()

    # Find the installed package line
    package_line = next((pkg for pkg in package_list if pkg.lower().startswith(package_name.lower() + "==")), None)

    if not package_line:
        print(f"Package '{package_name}' not found in installed packages.")
        return

    # Read existing requirements.txt
    try:
        with open(requirements_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    # Check if the package already exists
    updated = False
    with open(requirements_file, "w") as file:
        for line in lines:
            if line.lower().startswith(package_name.lower() + "=="):
                file.write(package_line + "\n")  # Update package version
                updated = True
            else:
                file.write(line)

        if not updated:
            file.write(package_line + "\n")  # Append new package

    print(f"Updated '{requirements_file}' with {package_line}")


# Example usage
if __name__ == "__main__":
    package = input("Enter package name to install and update in requirements.txt: ")
    install_and_update_requirements(package)
