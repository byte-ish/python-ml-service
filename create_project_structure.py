import os

# Define the project structure
project_structure = {
    "microservice": {
        "app": {
            "models": ["__init__.py", "ml_model.py"],
            "routes": ["__init__.py", "healthcheck.py", "prediction.py"],
            "services": ["__init__.py", "prediction_service.py"],
            "tests": ["__init__.py", "test_healthcheck.py", "test_prediction.py"],
            "__init__.py": None,
            "main.py": None,
        },
        "Dockerfile": None,
        "requirements.txt": None,
        "README.md": None,
    }
}

# Function to create files and directories
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # Create directories
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        elif isinstance(content, list):  # Create multiple files in a directory
            os.makedirs(path, exist_ok=True)
            for filename in content:
                with open(os.path.join(path, filename), "w") as file:
                    pass  # Create empty file
        else:  # Create individual files
            with open(path, "w") as file:
                if content is not None:
                    file.write(content)

# Create the project structure
create_project_structure(".", project_structure)

print("Project structure created successfully.")