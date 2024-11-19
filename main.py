import subprocess
import sys

# Path to your compiled Go program
gomat_executable = "./go_built"  # Update the path if necessary

# Get the argument string from the Python script's input
if len(sys.argv) < 2:
    print("Usage: python script.py '<arguments_as_string>'")
    sys.exit(1)

arguments = sys.argv[1]  # Get the arguments string passed to the Python script

# Combine the Go executable and the argument string
command = f"{gomat_executable} {arguments}"

try:
    # Run the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    # Check the exit code of the process
    if result.returncode == 0:
        print("Output from gomat:")
        print(result.stdout)  # The output of your Go program
    else:
        print("Error occurred:")
        print(result.stderr)  # Any error messages from your Go program
except FileNotFoundError:
    print(f"Error: {gomat_executable} not found.")
except Exception as e:
    print(f"An error occurred: {e}")