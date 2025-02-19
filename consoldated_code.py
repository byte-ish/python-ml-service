import os

def generate_code_structure_text(project_dir, output_file, ignore_folders=None):
    """
    Generate a text file containing the code structure of all Python files in a project,
    ignoring specified folders.

    Args:
        project_dir (str): Path to the root directory of the project.
        output_file (str): Path to the output text file.
        ignore_folders (list): List of folder names to ignore.
    """
    if ignore_folders is None:
        ignore_folders = []

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("# Project Code Structure with Comments\n")
            f.write("# This file contains the code of all Python files in the project, "
                    "annotated with comments describing their structure.\n\n")

            for root, dirs, files in os.walk(project_dir):
                # Remove ignored folders from the traversal
                dirs[:] = [d for d in dirs if d not in ignore_folders]

                for file in files:
                    if file.endswith(".py"):
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, project_dir)

                        # Write the file header
                        f.write(f"\n### File: {relative_path} ###\n\n")

                        with open(file_path, "r", encoding="utf-8") as code_file:
                            for line in code_file:
                                f.write(line)

                        f.write("\n\n")
        print(f"Code structure saved to {output_file}")
    except Exception as e:
        print(f"Error generating code structure: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your project directory and output file
    project_directory = "/Users/ish/PycharmProjects/python-ml-microservice/python-ml-microservice/app"
    output_text_file = "project_code_structure.txt"

    # Specify folders to ignore
    folders_to_ignore = ["__pycache__", "tests", "migrations"]

    generate_code_structure_text(project_directory, output_text_file, folders_to_ignore)