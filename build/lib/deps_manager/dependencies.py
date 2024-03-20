import subprocess
from .utils import handle_error

@handle_error
def install_dependencies(language, requirements_file):
    if language == 'python':
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'install', '-r', requirements_file], check=True)

@handle_error
def uninstall_dependency(language, package):
    if language == 'python':
        subprocess.run(['pip', 'uninstall', '-y', package], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'uninstall', '-y', package], check=True)

@handle_error
def list_dependencies(language):
    if language == 'python':
        subprocess.run(['pip', 'list'], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'list'], check=True)

@handle_error
def update_dependencies(language, requirements_file):
    if language == 'python':
        subprocess.run(['pip', 'install', '--upgrade', '-r', requirements_file], check=True)
    elif language == 'cpp':
        subprocess.run(['conan', 'update', '-r', requirements_file], check=True)

@handle_error
def lock_dependencies(language, requirements_file, lock_file):
    if language == 'python':
        subprocess.run(['pip', 'freeze', '--all', '--exclude-editable', '--exclude-pip'], check=True, stdout=lock_file)
    elif language == 'cpp':
        subprocess.run(['conan', 'lock', '-r', requirements_file, '-o', lock_file], check=True)