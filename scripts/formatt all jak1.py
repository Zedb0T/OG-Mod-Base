import os
import subprocess

def run_formatter_on_gc_files(root_dir):
    # Resolve relative path for formatter.exe
    script_dir = os.path.dirname(os.path.abspath(__file__))
    formatter_path = os.path.join(script_dir, "..", "out", "build", "Release", "bin", "formatter.exe")
    print(f"Formatter executable path: {formatter_path}")

    # Check if formatter.exe exists
    if not os.path.exists(formatter_path):
        print("Error: formatter.exe not found at", formatter_path)
        return

    print(f"Searching for .gc files in: {root_dir}")

    # Traverse all subdirectories for .gc files
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.gc'):
                gc_file_path = os.path.join(dirpath, filename)
                print(f"Found .gc file: {gc_file_path}")

                if not os.path.exists(gc_file_path):
                    print(f"Error: .gc file does not exist: {gc_file_path}")
                    continue

                # Command to run formatter.exe with the specified arguments
                command = [
                    formatter_path,
                    "-w", "-f", gc_file_path
                ]
                print(f"Running command: {' '.join(command)}")

                # Run the command
                try:
                    result = subprocess.run(
                        command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                    )
                    print(f"Formatted: {gc_file_path}")
                    print("Command output:", result.stdout)
                except subprocess.CalledProcessError as e:
                    print(f"Error formatting {gc_file_path}: {e}")
                    print("Command output:", e.stdout)
                    print("Command error:", e.stderr)
                except Exception as ex:
                    print(f"Unexpected error while formatting {gc_file_path}: {ex}")

# Root directory for .gc files relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
root_directory = os.path.join(script_dir, "..", "goal_src", "jak1")

if os.path.exists(root_directory):
    print(f"Root directory exists: {root_directory}")
else:
    print(f"Error: Root directory does not exist: {root_directory}")

run_formatter_on_gc_files(root_directory)
