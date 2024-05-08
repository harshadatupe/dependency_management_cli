"""
This module handles all dependency management operations based on the language.
"""

# Python standard library imports
import subprocess
import os

# Local application imports
from .utils import handle_error


@handle_error
def install_dependencies(requirements_file, language, venv_path):
    """
    Installs dependencies.
    """
    if language == 'python':
        pip_executable = 'pip'
        if venv_path:
            pip_executable = f"{venv_path}/bin/pip"  # For Linux and MacOS
        subprocess.run([pip_executable, 'install', '-r', requirements_file], check=True)
    
    elif language == 'cpp':
        subprocess.run(['conan', 'install', '-r', requirements_file], check=True)

@handle_error
def uninstall_dependency(package, language, venv_path):
    """
    Uninstalls dependencies.
    """
    if language == 'python':
        pip_executable = 'pip'
        if venv_path:
            pip_executable = f"{venv_path}/bin/pip"  # For Linux and MacOS
        subprocess.run([pip_executable, 'uninstall', '-y', package], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'uninstall', '-y', package], check=True)

@handle_error
def list_dependencies(language, venv_path):
    """
    Lists dependencies.
    """
    if language == 'python':
        pip_executable = 'pip'
        if venv_path:
            pip_executable = f"{venv_path}/bin/pip"  # For Linux and MacOS
        subprocess.run([pip_executable, 'list'], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'list'], check=True)

@handle_error
def update_dependencies(requirements_file, language, venv_path):
    """
    Updates dependencies.
    """
    if language == 'python':
        pip_executable = 'pip'
        if venv_path:
            pip_executable = f"{venv_path}/bin/pip"  # For Linux and MacOS
        subprocess.run([pip_executable, 'install', '--upgrade', '-r', requirements_file], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'update', '-r', requirements_file], check=True)

@handle_error
def lock_dependencies(requirements_lock_file, language, venv_path):
    """
    Build a lockfile to lock current dependencies.
    """
    if language == 'python':
        if venv_path:
            python_executable = f"{venv_path}/bin/python"
            subprocess.run([f"{venv_path}/bin/pip", "freeze"], stdout=open(requirements_lock_file, "w"), check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'lock', '-r', requirements_lock_file, '-o', lock_file], check=True)


@handle_error
def ensure_pipreqs_installed(pip_executable):
    """
    Ensure pipreqs is installed in the virtual environment.
    """
    # Check if pipreqs is installed
    try:
        subprocess.run([pip_executable, 'pipreqs', '--version'], 
        check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        # If not installed, install it
        print("pipreqs is not installed. Installing now...")
        subprocess.run([pip_executable, 'install', 'pipreqs'], check=True)


@handle_error
def remove_unused_dependencies(language, venv_path):
    """
    Remove unused dependencies.
    """
    if language == 'python':
        pip_executable = 'pip'
        if venv_path:
            pip_executable = f"{venv_path}/bin/pip"

        # Ensure pipreqs is installed
        ensure_pipreqs_installed(pip_executable)

        # Get current requirements
        current_reqs = subprocess.run([pip_executable, 'freeze'], capture_output=True, text=True)
        current_packages = set([line.split('==')[0] for line in current_reqs.stdout.splitlines()])

        # Get used dependencies based on import statements
        pipreqs_executable = 'pipreqs'
        used_reqs = subprocess.run([pipreqs_executable, '.'], capture_output=True, text=True)
        used_packages = set([line.split('==')[0] for line in used_reqs.stdout.splitlines()])

        # Uninstall unused dependencies
        unused_packages = current_packages - used_packages
        for package in unused_packages:
            subprocess.run([pip_executable, 'uninstall', '-y', package], check=True)
        if unused_packages:
            print("The following unused packages have been removed:")
            for package in unused_packages:
                print(f" - {package}")
        else:
            print("No unused packages to remove.")
    elif language == 'cpp':
        # Get the Conan dependency tree
        conan_executable = 'conan'
        if venv_path:
            conan_executable = f"{venv_path}/bin/conan"
        
        # Fetch the full dependency graph for the project
        dependency_graph = subprocess.run([conan_executable, 'info', '.'], capture_output=True, text=True)
        
        # Parse the dependency tree
        dependency_json = json.loads(dependency_graph.stdout)
        
        # Find unused dependencies
        unused_dependencies = set()
        # Custom logic to identify unused dependencies based on your C++ project's structure
        
        if unused_dependencies:
            print("The following unused C++ packages have been removed:")
            for unused_dep in unused_dependencies:
                subprocess.run([conan_executable, 'remove', '--force', unused_dep], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f" - {unused_dep}")
        else:
            print("No unused C++ packages to remove.")
