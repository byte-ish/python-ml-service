import os

def consolidate_code(base_dir, output_file):
    """
    Consolidate all Python files in the app package into a single text file.

    Args:
        base_dir (str): The base directory containing the app package.
        output_file (str): The path to the consolidated output file.
    """
    with open(output_file, "w", encoding="utf-8") as consolidated:
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as py_file:
                        consolidated.write(f"### File: {file_path} ###\n")
                        consolidated.write(py_file.read())
                        consolidated.write("\n\n")  # Add spacing between files
    print(f"Consolidated code written to {output_file}")

# Specify the directory containing the app package and the output file
base_directory = "app"  # Adjust this path if the app package is located elsewhere
output_file_path = "consolidated_code.txt"

# Run the consolidation
consolidate_code(base_directory, output_file_path)
