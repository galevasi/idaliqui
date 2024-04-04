import subprocess

# Function to execute a Python script
def execute_script(script_path):
    try:
        # Run the Python script and capture the output
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        # Print the stdout and stderr of the script execution
        print(f"Output:\n{result.stdout}")
        if result.stderr:
            print(f"Errors:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        # Handle the exception if the script execution fails
        print(f"An error occurred while executing the script: {e}")

# Replace 'your_script.py' with the path to the Python script you want to execute
execute_script('your_script.py')
